#!/usr/bin/python3
"""Module to hold a city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class to define a city
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
