#!/usr/bin/python3
"""Module to hold a place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class to define a place

    Attributes:
        city_id (str): The ID of the city associated with the place.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate
        price_by_night (int): The price per night for staying at the place.
        latitude (float): The latitude coordinates of the place.
        longitude (float): The longitude coordinates of the place.
        amenity_ids (list): List of amenity IDs associated with the place.

    Inherits from:
        BaseModel: The base class for all models in the application.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize a new Place instance

        Note:
            Calls the constructor of the parent class (BaseModel).
            Gets id(uuid), created_at, and updated_at from parent
        """
        super().__init__(*args, **kwargs)
