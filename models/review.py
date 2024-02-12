#!/usr/bin/python3
"""Module to hold a review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class to define a review

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who created the review.
        text (str): The text content of the review.

    Inherits from:
        BaseModel: The base class for all models in the application.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Review instance

        Note:
            Calls the constructor of the parent class (BaseModel).
            Gets id(uuid), created_at, and updated_at from parent
        """
        super().__init__(*args, **kwargs)
