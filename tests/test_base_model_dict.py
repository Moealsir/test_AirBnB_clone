#!/usr/bin/python3
import unittest
from datetime import datetime, timedelta
import sys
sys.path.append('../')
from models.base_model import BaseModel 

class TestBaseModelEdgeCases(unittest.TestCase):

    def test_empty_object_initialization(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_initialization_with_invalid_arguments(self):
        with self.assertRaises(TypeError):
            BaseModel(invalid_arg=42)

    def test_updating_attributes(self):
        model = BaseModel()
        model.name = "Updated Name"
        self.assertEqual(model.name, "Updated Name")

    def test_equality_testing(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1, model2)

    def test_save_method(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > old_updated_at)

    def test_string_representation(self):
        model = BaseModel()
        model_str = str(model)
        self.assertIn('[BaseModel]', model_str)
        self.assertIn(str(model.id), model_str)

    def test_dictionary_conversion(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('updated_at', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('id', model_dict)

    def test_future_updated_at(self):
        model = BaseModel()
        model.updated_at = datetime.now() + timedelta(days=1)
        self.assertLessEqual(model.updated_at, datetime.now())

    def test_corner_cases_for_datetime_formatting(self):
        model = BaseModel()
        model.created_at = datetime.min
        model.updated_at = datetime.max
        model_dict = model.to_dict()
        self.assertRegex(model_dict['updated_at'],
                         r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}')
        self.assertRegex(model_dict['created_at'],
                         r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}')


if __name__ == '__main__':
    unittest.main()
