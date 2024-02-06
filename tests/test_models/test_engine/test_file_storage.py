#!/usr/bin/python3
import json
import os
import unittest
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """ Testing File storage. """

    def test_save(self):
        """ Testing save. """
        instance = FileStorage()
        obj = BaseModel()
        path = "file.json"
        with open(path, 'r') as f:
            before_save_content = json.load(f)

        instance.all()["New"] = obj
        instance.save()

        with open(path, 'r') as f:
            after_save_content = json.load(f)

        self.assertNotEqual(before_save_content, after_save_content)


    def test_new_and_all(self):
        """ Test that new objects are correctly added to storage. """
        new_object = BaseModel()
        tmp = FileStorage()
        tmp.new(new_object)
        all_objects = storage.all()
        object_key = f"{new_object.__class__.__name__}.{new_object.id}"
        self.assertIn(object_key, all_objects)
        self.assertEqual(all_objects[object_key], new_object)
