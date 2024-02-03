#!/usr/bin/python3
"""Module to hold a place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class to define a place
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
