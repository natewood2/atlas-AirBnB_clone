#!/usr/bin/python3
"""Module to hold a user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class to define a user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
