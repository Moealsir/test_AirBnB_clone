python
import unittest
import uuid
from datetime import datetime
from your_module import BaseModel  # Replace this with the actual path to your module

class TestBaseModel(unittest.TestCase):
    
    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id, "ID should not be None")
        self.assertTrue(isinstance(model.id, str), "ID should be a string")
        try:
            uuid.UUID(model.id, version=4)
        except ValueError:
            self.fail("ID should be a valid UUID4")
        self.assertTrue(isinstance(model.created_at, datetime), "created_at should be a datetime object")
        self.assertTrue(isinstance(model.updated_at, datetime), "updated_at should be a datetime object")
    
    def test_str(self):
        model = BaseModel()
        expected_string = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_string, "String representation should match expected format")
    
    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at, "updated_at should be updated on save")
        self.assertTrue(datetime.now() - model.updated_at < timedelta(seconds=1), "updated_at should be close to current time")
    
    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel', "__class__ should be in the dict with value 'BaseModel'")
        self.assertEqual(model_dict['id'], model.id, "ID should match")
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat(), "created_at should match and be isoformatted")
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat(), "updated_at should match and be isoformatted")
        
        # Testing if the dict is a true copy
        model.name = "My Model"
        self.assertNotIn('name', model.to_dict(), "Changes to the instance should not change the dict returned by to_dict")
    
    def test_to_dict_with_new_attributes(self):
        model = BaseModel()
        model.name = "New attribute"
        model_dict = model.to_dict()
        self.assertIn('name', model_dict, "New attributes should be included in the dict")
    
    def test_invalid_init(self):
        # Assuming 'from_json' is an alternative constructor not shown in the provided code
        with self.assertRaises(TypeError):
            BaseModel(id=123, created_at='now')
    
    # Assuming that if `BaseModel` could accept **kwargs in `__init__`, this test would be relevant
    def test_kwargs_init(self):
        data = {
            'id': 'some-valid-uuid',
            'created_at': datetime.now().isoformat(),
        }
        with self.assertRaises(TypeError):
            model = BaseModel(**data)

if __name__ == '__main__':
    unittest.main()
