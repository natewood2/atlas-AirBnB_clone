#!/usr/bin/python3
""" File Storage using JSON. """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """
    Handles the storage of objects in a file.

    Attributes:
        __objects (dict): Cache of objects by <classname>.<id>.
        __file_path (str): Path to the JSON file used for storage.
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """
        Retrieves all stored objects.

        Returns:
            dict: A copy of the objects cache.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Parameters:
            obj: The object to be stored.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes and saves objects to the JSON file.
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as filename:
            json.dump(obj_dict, filename)

    def reload(self):
        """
        Deserializes and loads objects from the JSON file, if it exists.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    object = eval(value['__class__'])(**value)
                    self.__objects[key] = object
        except FileNotFoundError:
            pass
