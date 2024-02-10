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
    """test"""

    def setUp(self):
        """test"""
        self.temp_file, self.temp_file_path = tempfile.mkstemp()
        self.file_storage = FileStorage()
        FileStorage.__file_path = self.temp_file_path
        self.obj = BaseModel()

        with open(self.temp_file_path, 'w') as f:
            f.write('{}')

    def tearDown(self):
        """test"""
        try:
            os.remove(self.temp_file_path)
        except FileNotFoundError:
            pass

    def test_new(self):
        """test"""
        self.file_storage.new(self.obj)
        key = f'{self.obj.__class__.__name__}.{self.obj.id}'
        self.assertIn(key, self.file_storage.all())

    def test_all(self):
        """test"""
        self.file_storage.new(self.obj)
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)

    def test_save(self):
        """test"""
        self.file_storage.new(self.obj)
        self.file_storage.save()

    def test_reload(self):
        """test"""
        self.file_storage.new(self.obj)
        self.file_storage.save()
        self.file_storage.__objects = {}
        self.file_storage.reload()
        key = f'{self.obj.__class__.__name__}.{self.obj.id}'
        self.assertIn(key, self.file_storage.all())

    def test_reload_no_file(self):
        """test"""
        os.remove(self.temp_file_path)
        
    def test_class_dict(self):
        """test"""
        self.assertIsInstance(self.file_storage.class_dict(), dict)
        for model in [BaseModel, User, State, City, Place, Review, Amenity]:
            self.assertIn(model.__name__, self.file_storage.class_dict())

    def test_attribe(self):
        """test"""
        attribe = self.file_storage.attribe()
        self.assertIsInstance(attribe, dict)
        for class_name, attributes in attribe.items():
            for attr_name, attr_type in attributes.items():
                self.assertIsInstance(attr_name, str)
                self.assertIn(attr_type, [str, datetime, int, float, list])


if __name__ == '__main__':
    unittest.main()
