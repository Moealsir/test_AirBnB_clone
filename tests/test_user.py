#!/usr/bin/python3
import unittest
import sys
from models.user import User
sys.path.append('../')


class TestUser(unittest.TestCase):

    def test_user_instantiation(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes_default_empty(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_email_assignment(self):
        user = User()
        email = "test@example.com"
        user.email = email
        self.assertEqual(user.email, email)

    def test_user_password_assignment(self):
        user = User()
        password = "super_secure_password"
        user.password = password
        self.assertEqual(user.password, password)

    def test_user_first_name_assignment(self):
        user = User()
        first_name = "John"
        user.first_name = first_name
        self.assertEqual(user.first_name, first_name)

    def test_user_last_name_assignment(self):
        user = User()
        last_name = "Doe"
        user.last_name = last_name
        self.assertEqual(user.last_name, last_name)

    def test_user_id_uniqueness(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_user_updated_at_creation(self):
        user = User()
        self.assertIsNotNone(user.updated_at)

    def test_user_updated_at_save(self):
        user = User()
        first_update_time = user.updated_at
        user.save()
        second_update_time = user.updated_at
        self.assertNotEqual(first_update_time, second_update_time)

    def test_user_to_dict_contains_correct_keys(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)

    def test_user_to_dict_values(self):
        user = User()
        user.email = "test@example.com"
        user.password = "super_secure_password"
        user.first_name = "John"
        user.last_name = "Doe"
        user_dict = user.to_dict()
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "super_secure_password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")

    def test_user_str_representation(self):
        user = User()
        user_str = user.__str__()
        expected_substrings = ["[User] ({})".format(user.id),
                               "email", "password", "first_name", "last_name"]


if __name__ == '__main__':
    unittest.main()
