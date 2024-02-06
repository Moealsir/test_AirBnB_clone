import unittest
import os
import sys
sys.path.append('../')
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_initialization(self):
        self.assertTrue(isinstance(self.storage, FileStorage))

    def test_all_method(self):
        # Test if all() method returns a dictionary
        all_objs = self.storage.all()
        self.assertTrue(isinstance(all_objs, dict))

    def test_new_method(self):
        # Test if new() method adds an object to the __objects dictionary
        model = BaseModel()
        self.storage.new(model)
        self.assertIn("BaseModel {}".format(model.id), self.storage.all())

    def test_save_method(self):
        # Test if save() method creates a file
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method(self):
        # Test if reload() method loads objects from a file
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn("BaseModel {}".format(model.id), new_storage.all())

    def test_reload_empty_file(self):
        # Test if reload() method handles an empty JSON file
        open("file.json", "w").close()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_corrupted_file(self):
        # Test if reload() method handles a corrupted JSON file
        with open("file.json", "w") as json_file:
            json_file.write("Corrupted JSON")
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

if __name__ == '__main__':
    unittest.main()
