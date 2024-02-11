"""whew"""
import unittest
import sys
from unittest.mock import patch
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
sys.path.append('../')


class TestPlace(unittest.TestCase):
    """whew"""

    def setUp(self):
        """Set up test variables"""
        self.place = Place()

    def test_initialization(self):
        """Test initialization of place instance"""
        self.assertIsInstance(self.place, Place)
        self.assertIs(self.place.city_id, "")
        self.assertIs(self.place.user_id, "")
        self.assertIs(self.place.name, "")
        self.assertIs(self.place.description, "")
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertEqual(self.place.number_rooms, 0)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertEqual(self.place.max_guest, 0)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_types(self):
        """Test attribute types"""
        self.place.city_id = "12345"
        self.place.user_id = "abcde"
        self.place.name = "Test Place"
        self.place.description = "Test description"
        self.place.number_rooms = 1
        self.place.number_bathrooms = 2
        self.place.max_guest = 3
        self.place.price_by_night = 100
        self.place.latitude = 12.34
        self.place.longitude = -56.78
        self.place.amenity_ids = ["pool", "wifi"]

        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_modify_attributes(self):
        """Test modification of attributes"""
        self.place.city_id = "12345"
        self.place.user_id = "abcde"
        self.place.name = "Test Place"
        self.place.description = "Some new description"
        self.place.number_rooms = 5
        self.place.number_bathrooms = 3
        self.place.max_guest = 7
        self.place.price_by_night = 300
        self.place.latitude = 33.33
        self.place.longitude = -44.44
        self.place.amenity_ids = ["sauna"]

        self.assertEqual(self.place.city_id, "12345")
        self.assertEqual(self.place.user_id, "abcde")
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.description, "Some new description")
        self.assertEqual(self.place.number_rooms, 5)
        self.assertEqual(self.place.number_bathrooms, 3)
        self.assertEqual(self.place.max_guest, 7)
        self.assertEqual(self.place.price_by_night, 300)
        self.assertEqual(self.place.latitude, 33.33)
        self.assertEqual(self.place.longitude, -44.44)
        self.assertEqual(self.place.amenity_ids, ["sauna"])


if __name__ == '__main__':
    unittest.main()
