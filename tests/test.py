import unittest
from datetime import datetime, timedelta
import sys
sys.path.append('../')  # Add the parent directory to Python path
from models.base_model import BaseModel   # Replace 'your_module' with the actual module name where BaseModel is defined
import uuid


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()
        self.model.name = "Test_Model"
        self.model.my_number = 42

    def tearDown(self):
        pass

    def test_instance_creation(self):
        self.assertTrue(hasattr(self.model, 'id'), "id attribute is missing")
        self.assertTrue(isinstance(self.model.id, uuid.UUID), "id is not of type uuid.UUID")
        self.assertTrue(hasattr(self.model, 'created_at'), "created_at attribute is missing")
        self.assertTrue(isinstance(self.model.created_at, datetime), "created_at is not of type datetime")
        self.assertTrue(hasattr(self.model, 'updated_at'), "updated_at attribute is missing")
        self.assertTrue(isinstance(self.model.updated_at, datetime), "updated_at is not of type datetime")

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('updated_at', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('id', model_dict)

    def test_save_method(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > old_updated_at)

    def test_str_method(self):
        model_str = str(self.model)
        self.assertIn('[BaseModel]', model_str)
        self.assertIn(str(self.model.id), model_str)

    def test_edge_case_empty_dict(self):
        empty_dict_model = BaseModel()
        empty_dict = empty_dict_model.to_dict()
        self.assertNotIn('name', empty_dict)
        self.assertNotIn('my_number', empty_dict)

    def test_object_equality(self):
        # Assuming **kwargs implementation in __init__ was intended but not implemented
        new_model = BaseModel(**self.model.to_dict())
        self.assertNotEqual(self.model, new_model)
        # Check that they are different objects
        self.assertFalse(self.model is new_model)
        # Check that they have the same string representation if __str__ used id and created_at
        self.assertEqual(str(self.model), str(new_model))

    def test_date_fields_are_iso_formatted(self):
        # Assuming created_at and updated_at exist as datetime objects
        dict_representation = self.model.to_dict()
        self.assertRegex(dict_representation['updated_at'], r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}')
        self.assertRegex(dict_representation['created_at'], r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}')

    def test_future_updated_at(self):
        # Check that updated_at is not set to a future date
        self.model.save()
        self.assertLessEqual(self.model.updated_at, datetime.now())

    def test_to_dict_contains_all_attributes(self):
        self.model.save()
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], str(self.model.id))
        self.assertIn('my_number', model_dict, "The attribute 'my_number' is not in the dictionary.")
        self.assertIn('name', model_dict, "The attribute 'name' is not in the dictionary.")


if __name__ == '__main__':
    unittest.main()
