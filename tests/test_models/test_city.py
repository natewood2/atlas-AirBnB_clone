#!/usr/bin/python3
""" Tests for the City Class. """
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """ Testing the City Class. """
    def test_city_init(self):
        """ Testing City. """
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

    def test_city_attributes(self):
        """ Testing the cities attributes. """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
