#!/usr/bin/python3
""" Tests for the Amenity Class. """
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestState(unittest.TestCase):
    """ Testing the Amenity Class. """
    def test_amenity_init(self):
        """ Testing Amenity. """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_amenity_attributes(self):
        """ Testing the amenity attributes. """
        amenity = Amenity()
        amenity.name = "Wifi"

        self.assertEqual(amenity.name, "Wifi")
