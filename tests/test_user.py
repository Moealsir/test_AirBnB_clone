#!/usr/bin/python3
import unittest
import sys
import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
sys.path.append('../')


class TestUserModel(unittest.TestCase):

    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_inheritance(self):
        user = User()
        self.assertTrue(issubclass(user.__class__, BaseModel))

    def test_attributes_existence(self):
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_attributes_type(self):
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_empty_string_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_assigning_values(self):
        user = User()
        user.email = "test@example.com"
        user.password = "pass123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "pass123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_time_attributes(self):
        user = User()
        current_time = datetime.now()

        self.assertLessEqual(user.created_at, current_time)

        self.assertLessEqual(user.updated_at, current_time)

    def test_id_unique(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_str_representation(self):
        user = User()
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(user.__str__(), expected_str)

    def test_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)

    def test_to_dict_values(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict["id"], user.id)
        self.assertEqual(user_dict["__class__"], "User")

    def test_save_method(self):
        user = User()
        updated_at_before = user.updated_at
        user.save()
        updated_at_after = user.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)


if __name__ == '__main__':
    unittest.main()
