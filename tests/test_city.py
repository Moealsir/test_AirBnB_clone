"""whew"""
import unittest
import sys
from unittest.mock import patch
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
sys.path.append('../')


class TestCity(unittest.TestCase):
    """whew"""

    def test_attributes(self):
        """Test if City instance has the expected attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_attribute_types(self):
        """Test if attribute types are correct"""
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_attribute_defaults(self):
        """Test if attribute defaults are correct"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_assignment(self):
        """Test if attributes can be assigned properly"""
        city = City()
        city.state_id = "123"
        city.name = "Test City"
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "Test City")


if __name__ == '__main__':
    unittest.main()
