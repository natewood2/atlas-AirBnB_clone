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
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
