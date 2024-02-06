#!/usr/bin/python3
import json
import os
import unittest
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """ Testing File storage. """
    def setUp(self):
        """ Setting up. """
        self.test_save = BaseModel()
        self.saving_test = FileStorage()

    def test_save(self):
        """ Testing save. """
        self.test_save.save()
        storage.reload()
        all_objects = storage.all()
        object_key = f"{self.test_save.__class__.__name__}.{self.test_save.id}"
        self.assertIn(object_key, all_objects)
        self.assertTrue(hasattr(self.test_save, 'save'))
        self.assertNotEqual(self.test_save.created_at, self.test_save.updated_at)

    def test_new_and_all(self):
        """ Test that new objects are correctly added to storage. """
        new_object = BaseModel()
        self.saving_test.new(new_object)
        all_objects = self.saving_test.all()
        object_key = f"{new_object.__class__.__name__}.{new_object.id}"
        self.assertIn(object_key, all_objects)
        self.assertEqual(all_objects[object_key], new_object)
        