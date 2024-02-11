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


    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_save(self, mock_json_dump, mock_open):
        self.storage.new(self.base_model)
        self.storage.save()
        mock_open.assert_called_once_with(FileStorage._FileStorage__file_path, "w", encoding="utf-8")
        mock_json_dump.assert_called_once()

    @patch("os.stat")
    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_reload_empty(self, mock_open, mock_stat):
        mock_stat.return_value.st_size = 0
        self.storage.reload()
        self.assertFalse(self.storage._FileStorage__objects)

    @patch("builtins.open", new_callable=mock_open, read_data='{"BaseModel.1234": {"__class__": "BaseModel", "id": "1234", "created_at": "2021-11-02T14:15:22", "updated_at": "2021-11-02T14:15:22"}}')
    def test_reload_with_data(self, mock_open):
        self.storage.reload()
        self.assertTrue(self.storage._FileStorage__objects)
        key = "BaseModel.1234"
        self.assertIn(key, self.storage._FileStorage__objects)
        obj = self.storage._FileStorage__objects[key]
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.id, "1234")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_reload_not_found(self, mock_open):
        self.storage.reload()
        mock_open.assert_called_once_with(FileStorage._FileStorage__file_path, "r+", encoding="utf-8")
        self.assertFalse(self.storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()