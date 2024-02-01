#!/usr/bin/python3
""" File Storage using JSON. """
import json
import os


class FileStorage:
    """ Document. """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All."""
        return FileStorage.__objects

    def new(self, obj):
        """OBJ"""
        FileStorage.__objects.update({f"{obj.__class__.__name__}.{obj.id}" : obj})

    def save(self):
        """Save to file"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as filename:
            json.dump(obj_dict, filename)

    def reload(self):
        """Reloads"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as filename:
                data = json.load(filename):
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                obj_instance = eval(class_name).from_dict(value)
                FileStorage.__objects[key] = obj_instance
        