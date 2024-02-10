#!/usr/bin/python3

import unittest
import sys
sys.path.append('../')
from unittest.mock import patch
import unittest
from models.base_model  import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    
    def test_amenity_init(self):
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))
        self.assertEqual(amenity.name, "")
    
    def test_amenity_attributes(self):
        am = Amenity()
        self.assertTrue(hasattr(am, 'name'))
        self.assertIsInstance(am.name, str)
        
    def test_amenity_save(self):
        am = Amenity()
        updated_at = am.updated_at
        am.save()
        self.assertNotEqual(am.updated_at, updated_at)
    
    def test_amenity_to_dict(self):
        am = Amenity()
        am.name = "Wi-Fi"
        am_dict = am.to_dict()
        self.assertEqual(am_dict['__class__'], 'Amenity')
        self.assertEqual(am_dict['name'], 'Wi-Fi')
        
        # Ensure that 'created_at' and 'updated_at' are strings in ISO format
        self.assertIsInstance(am_dict['created_at'], str)
        self.assertIsInstance(am_dict['updated_at'], str)
        
        # Confirm that time strings are in ISO format
        self.assertEqual(datetime.fromisoformat(am_dict['created_at']).replace(tzinfo=None), am.created_at)
        self.assertEqual(datetime.fromisoformat(am_dict['updated_at']).replace(tzinfo=None), am.updated_at)
        
        # Ensure it contains the key 'id' 
        self.assertIn('id', am_dict)
        self.assertEqual(am.id, am_dict['id'])
        
    def test_amenity_str(self):
        am = Amenity()
        expected_str_format = f"[Amenity] ({am.id}) {am.__dict__}"
        self.assertEqual(str(am), expected_str_format)

    @patch('models.storage')
    def test_save_method_calls_storage_save(self, mock_storage):
        am = Amenity()
        am.save()
        mock_storage.save.assert_called_once()

if __name__ == '__main__':
    unittest.main()
