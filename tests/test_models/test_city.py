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
        city.name = "Seattle"
        city.state_id = "101010"

        self.assertEqual(city.name, "Seattle")
        self.assertEqual(city.state_id, "101010")