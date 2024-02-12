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
        # Create a dictionary of object IDs to their serialized (dictionary) form.
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        # Open the target file in write mode and serialize obj_dict to it.
        with open(self.__file_path, 'w') as filename:
            json.dump(obj_dict, filename) # Write the JSON serialization to the file.

    def reload(self):
        """
        Deserializes and loads objects from the JSON file, if it exists.
        """
        try:
            # Open the JSON file in read mode.
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f) # Load and deserialize the JSON data into a dictionary.
                # Iterate through the items in the deserialized data.
                for key, value in data.items():
                    # Dynamically create an instance of the class specified in the data,
                    # passing the attributes as keyword arguments.
                    object = eval(value['__class__'])(**value)
                    # Store the newly created object in the __objects dictionary.
                    self.__objects[key] = object
        except FileNotFoundError:
            # If the JSON file does not exist, do nothing.
            pass
