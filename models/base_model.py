#!/usr/bin/python3
"""
Base Model Class for AirBnB: The Console
"""
import uuid
import datetime


class BaseModel:
    """ Base Class for The Console. """
    def __init__(self):
        """ Init for the BaseModel Class. """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Returns a string representation of the instance. """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates
        the updated_at attribute with the current
        datetime whenever an object's state changes.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Converts the instance into a dictionary for serialization. """
        attr_order = [
            'my_number',
            'name',
            '__class__',
            'updated_at',
            'id',
            'created_at',
        ]

        dict_copy = {key: getattr(self, key) for key in attr_order}
        dict_copy['__class__'] = self.__class__.__name__

        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['created_at'] = self.created_at.isoformat()

        return dict_copy
