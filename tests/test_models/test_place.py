#!/usr/bin/python3
""" Tests for the User Class. """
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Testing for Place. """
    def test_place_init(self):
        """ Testing Init. """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))

    def test_variable_attributes(self):
        """ Testing values and equals. """
        place = Place()
        place.city_id = "Tulsa"
        place.user_id = "atlasStudent"
        place.name = "Nathan"
        place.description = "Awesome City"
        place.number_rooms = "3"
        place.number_bathrooms = "45"
        place.max_guest = "3"
        place.price_by_night = "$235"
        place.latitude = "37.7749"
        place.longitude = "-122.4194"

        self.assertEqual(place.city_id, "Tulsa")
        self.assertEqual(place.user_id, "atlasStudent")
        self.assertEqual(place.name, "Nathan")
        self.assertEqual(place.description, "Awesome City")
        self.assertEqual(place.number_rooms, "3")
        self.assertEqual(place.number_bathrooms, "45")
        self.assertEqual(place.max_guest, "3")
        self.assertEqual(place.price_by_night, "$235")
        self.assertEqual(place.latitude, "37.7749")
        self.assertEqual(place.longitude, "-122.4194")