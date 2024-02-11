#!/usr/bin/python3
import unittest
import sys
from unittest.mock import patch
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
sys.path.append('../')


class TestBaseModel(unittest.TestCase):
    def test_base_model_instance(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)


class TestCityModel(unittest.TestCase):

    def test_city_inheritance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attribute_types(self):
        city = City()
        self.assertIs(type(city.name), str)
        self.assertIs(type(city.state_id), str)

    def test_city_kwargs(self):
        city = City(name="San Francisco", state_id="CA")
        self.assertEqual(city.name, "San Francisco")
        self.assertEqual(city.state_id, "CA")

    def test_city_save(self):
        city = City()
        first_updated_at = city.updated_at
        city.save()
        second_updated_at = city.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)
        self.assertTrue(second_updated_at > first_updated_at)

    def test_city_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIs(type(city_dict), dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)
        self.assertEqual(city_dict["__class__"], "City")

    def test_city_serialization_format(self):
        city = City()
        city_dict = city.to_dict()
        created_at = city_dict["created_at"]
        updated_at = city_dict["updated_at"]
        self.assertIs(type(created_at), str)
        self.assertIs(type(updated_at), str)

    def test_city_datetime_format(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsNotNone(datetime.strptime(
            city_dict["created_at"], '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertIsNotNone(datetime.strptime(
            city_dict["updated_at"], '%Y-%m-%dT%H:%M:%S.%f'))

    def test_city_custom_attributes(self):
        city = City()
        city.custom_attr = "custom_val"
        city.save()
        city_dict = city.to_dict()
        self.assertIn("custom_attr", city_dict)
        self.assertEqual(city_dict["custom_attr"], "custom_val")


if __name__ == '__main__':
    unittest.main()
