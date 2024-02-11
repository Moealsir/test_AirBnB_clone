#!/usr/bin/python3
import unittest
import sys
from models.user import User
from models.base_model import  BaseModel
sys.path.append('../')


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user1 = User()
        self.user2 = User()

    def test_user_instance(self):
        self.assertTrue(isinstance(self.user1, User))

    def test_user_has_attributes(self):
        self.assertTrue(hasattr(self.user1, "email"))
        self.assertTrue(hasattr(self.user1, "password"))
        self.assertTrue(hasattr(self.user1, "first_name"))
        self.assertTrue(hasattr(self.user1, "last_name"))

    def test_user_attributes_empty_initially(self):
        self.assertEqual(self.user1.email, "")
        self.assertEqual(self.user1.password, "")
        self.assertEqual(self.user1.first_name, "")
        self.assertEqual(self.user1.last_name, "")

    def test_setting_user_attributes(self):
        self.user1.email = "user1@example.com"
        self.user1.password = "user1password"
        self.user1.first_name = "User"
        self.user1.last_name = "One"
        self.assertEqual(self.user1.email, "user1@example.com")
        self.assertEqual(self.user1.password, "user1password")
        self.assertEqual(self.user1.first_name, "User")
        self.assertEqual(self.user1.last_name, "One")

    def test_different_users_have_different_attributes(self):
        self.user1.email = "user1@example.com"
        self.user2.email = "user2@example.com"
        self.assertNotEqual(self.user1.email, self.user2.email)

    def test_users_have_unique_ids(self):
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_user_inheritance_from_BaseModel(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_update_user_attributes(self):
        self.user1.email = "user1@example.com"
        self.user1.password = "newpassword123"
        self.user1.first_name = "John"
        self.user1.last_name = "Doe"
        
        self.user1.save()
        
        self.assertEqual(self.user1.email, "user1@example.com")
        self.assertEqual(self.user1.password, "newpassword123")
        self.assertEqual(self.user1.first_name, "John")
        self.assertEqual(self.user1.last_name, "Doe")
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_save_updates_updated_at(self):
        old_updated_at = self.user1.updated_at
        self.user1.save()
        self.assertNotEqual(old_updated_at, self.user1.updated_at)


if __name__ == '__main__':
    unittest.main()
