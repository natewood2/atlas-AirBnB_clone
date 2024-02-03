#!/usr/bin/python3
"""Module to hold a state class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class to define a state
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
