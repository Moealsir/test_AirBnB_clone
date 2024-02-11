import sys
import unittest
from models.engine.file_storage import FileStorage
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os
from io import StringIO
sys.path.append('../../')


class TestFileStorage(unittest.TestCase):


    @patch("builtins.open", new_callable=mock_open, read_data='{"BaseModel.1234": {"__class__": "BaseModel", "id": "1234", "created_at": "2021-11-02T14:15:22", "updated_at": "2021-11-02T14:15:22"}}')
    def test_reload_with_data(self, mock_open):
        self.storage.reload()
        self.assertTrue(self.storage._FileStorage__objects)
        key = "BaseModel.1234"
        self.assertIn(key, self.storage._FileStorage__objects)
        obj = self.storage._FileStorage__objects[key]
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.id, "1234")


if __name__ == '__main__':
    unittest.main()