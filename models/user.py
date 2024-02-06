#!/usr/bin/python3
"""Module defining the User class.

This module contains the User class, which represents a user entity in the system.
A User has attributes such as email, password, first name, and last name.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class to define a User

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user's account.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Inherits from:
        BaseModel: The base class for all models in the application.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance

        Note:
            Calls the constructor of the parent class (BaseModel).
            Gets id(uuid), created_at, and updated_at from parent
        """
        super().__init__(*args, **kwargs)
