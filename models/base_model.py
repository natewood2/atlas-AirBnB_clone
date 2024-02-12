#!/usr/bin/python3
"""
Base Model Class for AirBnB: The Console
"""
import uuid
import datetime
import models


class BaseModel:
    """ Base Class for The Console.

    Attributes:
        id (str): A unique identifier for each instance.
        created_at (datetime): The date/time when the instance was created.
        updated_at (datetime): The date/time when the instance was last updated
    """
    def __init__(self, *args, **kwargs):
        """ Init for the BaseModel Class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            If kwargs is provided, it initializes the instance using the
            provided values.
            Otherwise, it generates a new id and sets created_at and
            updated_at to the current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                # Loop through keyword arguments if provided.
                if key == '__class__':
                    continue # Skip special '__class__' key.
                elif key in ['created_at', 'updated_at']:
                    # Convert string to datetime for 'created_at' and 'updated_at'.
                    value = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                # Dynamically set attributes based on kwargs.
                setattr(self, key, value)
        else:
            # Assign a unique ID if no kwargs.
            self.id = str(uuid.uuid4())
            # Set current time as created_at
            self.created_at = datetime.datetime.now()
            # Set current time as updated_at.
            self.updated_at = datetime.datetime.now()
        # Add the instance to the storage mechanism.
        models.storage.new(self)

    def __str__(self):
        """ Overwrites the default str.

        Returns:
            str: A formatted representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates the updated_at attribute with the current
        datetime whenever an object's state changes.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Converts the instance into a dictionary for serialization.

        Returns:
            dict: A dictionary representation of the instance.
        """
        dict_copy = {}
        # Iterates over the instance's attributes.
        for a in vars(self):
            # Adds each attribute to the dictionary using update method.
            dict_copy.update({a: getattr(self, a)})
        # Adds a '__class__' key with the name of the class as its value.
        dict_copy['__class__'] = self.__class__.__name__
        # Converts 'updated_at' datetime to ISO format string.
        dict_copy['updated_at'] = self.updated_at.isoformat()
        # Converts 'create_at' datetime to ISO format string.
        dict_copy['created_at'] = self.created_at.isoformat()

        return dict_copy
