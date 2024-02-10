#!/usr/bin/python3
"""test"""
import unittest
from unittest.mock import patch
import sys
sys.path.append('../')
from models.engine.file_storage import FileStorage 

import os
import tempfile
import json
from unittest.mock import mock_open, patch
from datetime import datetime

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import FileStorage



class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_storage = FileStorage()
        # Create a temporary directory and file to be used in tests
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_storage._FileStorage__file_path = os.path.join(self.temp_dir.name, 'file.json')

    def tearDown(self):
        # Close and remove the temporary directory and file
        self.temp_dir.cleanup()

    def test_new(self):
        """
        Test adding new object to storage.
        """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        key = f"BaseModel.{base_model.id}"
        self.assertIn(key, self.file_storage.all())

    def test_all(self):
        """
        Test getting all objects in storage.
        """
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)

    def test_save(self):
        """
        Test saving objects to file.
        """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        key = f"BaseModel.{base_model.id}"
        self.assertTrue(os.path.exists(self.file_storage._FileStorage__file_path))
        with open(self.file_storage._FileStorage__file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            self.assertIn(key, data)

    def test_reload(self):
        """
        Test loading objects from file.
        """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        self.file_storage._FileStorage__objects = {}
        self.file_storage.reload()
        key = f"BaseModel.{base_model.id}"
        self.assertIn(key, self.file_storage.all())

    def test_reload_no_file(self):
        """
        Test reloading non-existing file should be handled without error.
        """
        # Create an empty file to simulate a missing file
        open(self.file_storage._FileStorage__file_path, 'w').close()

        # Delete the file to simulate the missing file scenario
        os.unlink(self.file_storage._FileStorage__file_path)

        # Reload should handle the missing file without error
        self.file_storage.reload()

    def test_class_dict(self):
        """
        Test class dictionary for serialization-deserialization.
        """
        classes = self.file_storage.class_dict()
        expected_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        self.assertDictEqual(classes, expected_classes)

    def test_attribe(self):
        """
        Test valid attributes and their types for classname.
        """
        attributes = self.file_storage.attribe()
        self.assertIn('BaseModel', attributes)
        self.assertIn('id', attributes['BaseModel'])
        self.assertIn('User', attributes)
        self.assertIn('email', attributes['User'])


if __name__ == '__main__':
    unittest.main()