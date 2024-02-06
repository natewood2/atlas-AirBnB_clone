#!/usr/bin/python3
""" Test file for BaseModel.py. """
import unittest
import tests
from models.base_model import BaseModel
from unittest.mock import patch
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """ Defines test cases for the BaseModel class. """
    def test_instance_type(self):
        """Test if the created instance is an object of BaseModel."""
        instance = BaseModel()
        self.assertTrue(isinstance(instance, BaseModel))

    def test_id_type(self):
        """ Testing type of id. """
        newId = BaseModel()
        self.assertTrue(isinstance(newId.id, str))

    def test_save_method_updates_updated_at(self):
        """Test that the save method updates updated_at."""
        instance = BaseModel()
        original_updated_at = instance.updated_at

        instance.save()
        self.assertNotEqual(instance.updated_at, original_updated_at, "updated_at was not updated.")

    def test_to_dict_method(self):
        """Test conversion of instance to dictionary."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
