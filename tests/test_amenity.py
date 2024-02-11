import unittest
import sys
from unittest.mock import patch
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
sys.path.append('../')


class TestAmenity(unittest.TestCase):

    def test_attributes(self):
        """Test if Amenity instance has the expected attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_attribute_types(self):
        """Test if attribute types are correct"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.name, str)

    def test_attribute_defaults(self):
        """Test if attribute defaults are correct"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attribute_assignment(self):
        """Test if attributes can be assigned properly"""
        amenity = Amenity()
        amenity.name = "Test Amenity"
        self.assertEqual(amenity.name, "Test Amenity")


if __name__ == '__main__':
    unittest.main()
