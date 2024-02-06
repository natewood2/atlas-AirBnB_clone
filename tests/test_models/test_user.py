#!/usr/bin/python3
""" Tests for the User Class. """
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test suite for the User class."""
    def test_user_init(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_set_values(self):
        """ Testing if the values equal to what they are set too. """
        user = User()
        user.email = "thisisaemail@yahoo.com"
        user.password = "thecakeisalie"
        user.first_name = "Lamar"
        user.last_name = "Jackson"

        self.assertEqual(user.email, "thisisaemail@yahoo.com")
        self.assertEqual(user.password, "thecakeisalie")
        self.assertEqual(user.first_name, "Lamar")
        self.assertEqual(user.last_name, "Jackson")

if __name__ == '__main__':
    unittest.main()
