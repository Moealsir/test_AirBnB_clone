#!/usr/bin/python3
"""testing BaseModel"""
import unittest
from unittest.mock import patch
import sys
sys.path.append('../')
from models.base_model import BaseModel
import uuid
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """test  class for BaseModel"""

    def setUp(self):
        """setup"""
        self.model = BaseModel()

    def tearDown(self):
        """tearDown"""
        del self.model

    def test_init_no_kwargs(self):
        """test  __init__ without kwargs"""
        self.assertIsNotNone(self.model.id)
        self.assertTrue(isinstance(self.model.id, str))
        self.assertTrue(isinstance(self.model.created_at, datetime))
        self.assertTrue(isinstance(self.model.updated_at, datetime))
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_init_with_kwargs(self):
        test_id = str(uuid.uuid4())
        test_time = datetime.now()
        test_kwargs = {
            'id': test_id,
            'created_at': test_time.isoformat(),
            'updated_at': test_time.isoformat(),
            '__class__': 'SomeClass'
        }
        model_with_kwargs = BaseModel(**test_kwargs)
        self.assertEqual(model_with_kwargs.id, test_id)
        self.assertEqual(model_with_kwargs.created_at, test_time)
        self.assertEqual(model_with_kwargs.updated_at, test_time)

    def test_str(self):
        """test str"""
        expected_str_format = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(expected_str_format, str(self.model))

    @patch('models.storage')
    def test_save(self, mock_storage):
        """test save"""
        previous_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, previous_updated_at)
        mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """test to dict"""
        model_dict = self.model.to_dict()
        expected_keys = {"id", "__class__", "created_at", "updated_at"}
        self.assertTrue(expected_keys.issubset(model_dict.keys()))
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())
        self.assertNotIn("_sa_instance_state", model_dict)

    def test_to_dict_with_extra_attribute(self):
        """test to_dict with extra attribute"""
        self.model.name = "Test Name"
        model_dict = self.model.to_dict()
        self.assertIn("name", model_dict)
        self.assertEqual(model_dict["name"], "Test Name")


if __name__ == '__main__':
    unittest.main()
