#!/usr/bin/python3
"""Module to hold an amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class to define an amenity

    Attributes:
        name (str): The name of the amenity.

    Inherits from:
        BaseModel: The base class for all models in the application.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity instance

        Note:
            Calls the constructor of the parent class (BaseModel).
            Gets id(uuid), created_at, and updated_at from parent
        """
        super().__init__(*args, **kwargs)
