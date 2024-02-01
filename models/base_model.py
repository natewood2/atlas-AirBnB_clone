#!/usr/bin/python3
import uuid
import datetime
"""
Base Model Class for AirBnB: The Console
"""


class BaseModel:
    """ Base Class for The Console. """
    def __init__(self, id=0):
        """ Init for the BaseModel Class. """
        self.id = uuid.uuid4() if id is None else id
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Returns a string representation of the instance. """
        return f"[self.__class__.__name__] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates
        the updated_at attribute with the current
        datetime whenever an object's state changes.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Converts the instance into a dictionary for serialization. """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__

        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['created_at'] = self.created_at.isoformat()
