#!/usr/bin/python3
"""Module to hold an amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class to define an amenity
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
