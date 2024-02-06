#!/usr/bin/python3
"""Module to hold a state class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class to define a state

    Attributes:
        name (str): The name of the state.

    Inherits from:
        BaseModel: The base class for all models in the application.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Review instance

        Note:
            Calls the constructor of the parent class (BaseModel).
            Gets id(uuid), created_at, and updated_at from parent
        """
        super().__init__(*args, **kwargs)
