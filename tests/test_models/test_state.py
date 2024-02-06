#!/usr/bin/python3
""" Tests for the State Class. """
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """ Testing the State Class. """
    def test_state_init(self):
        """ Testing State. """
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_state_attributes(self):
        """ Testing the states attributes. """
        state = State()
        state.name = "Washington"

        self.assertEqual(state.name, "Washington")

    def test_fake_state(self):
        state = State()
        state.name = "FakeState"

        self.assertNotEqual(state.name, "Fakestate")
