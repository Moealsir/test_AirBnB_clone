import sys

import unittest
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        # Create a unique FileStorage instance for testing
        self.storage = FileStorage()

        # Create a test BaseModel instance
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up after each test."""
        # Delete the test JSON file if it exists
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_save_reload(self):
        """Test saving and reloading objects."""
        # Save the test BaseModel instance
        self.storage.new(self.base_model)
        self.storage.save()

        # Create a new FileStorage instance to simulate reloading
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the BaseModel instance was reloaded
        reloaded_objects = new_storage.all()
        self.assertTrue(len(reloaded_objects) > 0)
        self.assertIn(self.base_model.__class__.__name__, reloaded_objects)
        self.assertIn(self.base_model.id, reloaded_objects[self.base_model.__class__.__name__])

    def test_save_empty_file(self):
        """Test saving to an empty JSON file."""
        # Create an empty JSON file
        with open(self.storage._FileStorage__file_path, "w") as f:
            f.write("")

        # Save the test BaseModel instance to the empty file
        self.storage.new(self.base_model)
        self.storage.save()

        # Check if the BaseModel instance was saved
        with open(self.storage._FileStorage__file_path, "r") as f:
            data = f.read()
            self.assertNotEqual(data, "")
            self.assertIn(self.base_model.__class__.__name__, data)

    def test_save_invalid_json(self):
        """Test saving when JSON data is corrupted."""
        # Create an invalid JSON file
        with open(self.storage._FileStorage__file_path, "w") as f:
            f.write("invalid_json_data")

        # Attempt to save the test BaseModel instance
        self.storage.new(self.base_model)
        self.storage.save()

        # Check if the BaseModel instance was not saved due to invalid JSON
        with open(self.storage._FileStorage__file_path, "r") as f:
            data = f.read()
            self.assertEqual(data, "invalid_json_data")


if __name__ == "__main__":
    unittest.main()
