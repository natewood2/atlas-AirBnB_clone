#!/usr/bin/python3
""" File Storage using JSON. """
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ Document. """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """All."""
        return FileStorage.__objects

    def new(self, obj):
        """OBJ"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Save to file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as filename:
            json.dump(obj_dict, filename)

    def reload(self):
        """Reloads"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    object = eval(value['__class__'])(**value)
                    self.__objects[key] = object
        except FileNotFoundError:
            pass
