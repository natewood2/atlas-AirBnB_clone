#!/usr/bin/python3
"""Module to hold a city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class to define a city

    Attributes:
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.

    Inherits from:
        BaseModel: The base class for all models in the application.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new City instance

        Note:
            Calls the constructor of the parent class (BaseModel).
            Gets id(uuid), created_at, and updated_at from parent
        """
        super().__init__(*args, **kwargs)
