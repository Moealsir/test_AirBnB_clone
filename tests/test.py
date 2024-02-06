python
import unittest
import uuid
from datetime import datetime, timedelta
from your_module import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertTrue(hasattr(self.model, "id"), "BaseModel should have an id attribute")
        self.assertTrue(hasattr(self.model, "created_at"), "BaseModel should have a created_at attribute")
        self.assertTrue(hasattr(self.model, "updated_at"), "BaseModel should have an updated_at attribute")
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
    
    def test_str(self):
        string_representation = str(self.model)
        self.assertIn("[BaseModel] ({})".format(self.model.id), string_representation)
        self.assertIn("'updated_at'", string_representation)
        self.assertIn("'created_at'", string_representation)
        self.assertIn("'id'", string_representation)
    
    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at, "save() should update the updated_at attribute")
        self.assertLess(old_updated_at, self.model.updated_at, "updated_at should be more recent after save")
    
    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIn("updated_at", model_dict, "to_dict() should include 'updated_at'")
        self.assertIn("__class__", model_dict, "to_dict() should include '__class__'")
        self.assertIn("created_at", model_dict, "to_dict() should include 'created_at'")
        self.assertIn("id", model_dict, "to_dict() should include 'id'")
        self.assertEqual("BaseModel", model_dict["__class__"])
        self.assertEqual(self.model.created_at.isoformat(), model_dict["created_at"])
        self.assertEqual(self.model.updated_at.isoformat(), model_dict["updated_at"])
    
    def test_updated_at_set_on_init(self):
        acceptable_difference = timedelta(seconds=1)
        time_now = datetime.now()
        self.assertLessEqual(time_now - self.model.created_at, acceptable_difference)
        self.assertLessEqual(time_now - self.model.updated_at, acceptable_difference)

    def test_create_with_unique_ids(self):
        another_model = BaseModel()
        self.assertNotEqual(self.model.id, another_model.id, "Each BaseModel instance should have a unique id")

    def test_updated_at_on_save(self):
        initial_updated_at = self.model.updated_at
        time.sleep(1)  # Ensure a noticeable time gap between save calls
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at, "saved 'updated_at' should differ after save()")
        time_diff = self.model.updated_at - initial_updated_at
        self.assertTrue(time_diff.total_seconds() > 0, "updated_at should be increased after save call")

if __name__ == '__main__':
    unittest.main()
