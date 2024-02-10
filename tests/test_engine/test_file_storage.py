#!/usr/bin/python3

"""Unit tests for the FileStorage class."""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import models
import os
from models.user import User

class Test_FileStorage(unittest.TestCase):
    """test case for attributes of the class FilesStorage"""
    
    def test_attributes_assignement(self):
        self.assertIn("_FileStorage__objects", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIn("_FileStorage__file_path", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_new_key(self):
        """
        tests the new method within file storage
        Test with different types of class
        """
        base = models.storage.all().copy()
        for k, v in base.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        base = models.storage.all()
        self.assertEqual(type(base[f"BaseModel.{str(b1.id)}"]), type(b1))


    def test_allmethod_instance(self):
        """
        Tests for the all method of the file_storage.py
        Test type of the istance
        """
        base = FileStorage()
        self.assertEqual(type(base), FileStorage)

    def test_allmethod_type_dict(self):
        """Test if the return value is a dictionary"""
        self.assertEqual(type(models.storage.all()), dict)

    def tests_allmethod_empty_obj(self):
        """test case if that an empty object"""
        d = models.storage.all().copy()
        for k, v in d.items():
            del models.storage.all()[k]
        models.storage.save()
        self.assertEqual(models.storage.all(), {})

    def test_allmethod_one_obj(self):
        """Test case with one object"""
        d = models.storage.all().copy()
        for k, v in d.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        self.assertEqual(len(models.storage.all()), 1)

    def tests_allmethod_multiple_obj(self):
        """Test case with multiobject"""
        d = models.storage.all().copy()
        for k, v in d.items():
            del models.storage.all()[k]
        models.storage.save()
        b2 = BaseModel()
        b3 = BaseModel()
        b2.save()
        b3.save()
        self.assertEqual(len(models.storage.all()), 2)

    def test_reload_type(self):
        """Test the reload method type"""
        d = models.storage.all().copy()
        for k, v in d.items():
            del models.storage.all()[k]
        models.storage.save()
        u1 = User()
        u1.save()
        models.storage.reload()
        d = models.storage.all()
        for k, v in d.items():
            self.assertEqual(type(d[k]), type(u1))