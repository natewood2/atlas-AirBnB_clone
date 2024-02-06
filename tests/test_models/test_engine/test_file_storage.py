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
        self.test_instance = BaseModel()
        self.test_instance.save()
        self.saving_test = FileStorage()
        storage.reload()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save(self):
        """ Testing save. """
        all_objects = storage.all()
        object_key = f"{self.test_instance.__class__.__name__}.{self.test_instance.id}"
        self.assertIn(object_key, all_objects)
        self.assertTrue(hasattr(self.test_instance, 'save'))
        tmp = self.test_instance.updated_at.microsecond
        self.test_instance.save()
        self.assertNotEqual(tmp,
                            self.test_instance.updated_at.microsecond)


    def test_new_and_all(self):
        """ Test that new objects are correctly added to storage. """
        new_object = BaseModel()
        self.saving_test.new(new_object)
        all_objects = self.saving_test.all()
        object_key = f"{new_object.__class__.__name__}.{new_object.id}"
        self.assertIn(object_key, all_objects)
        self.assertEqual(all_objects[object_key], new_object)
