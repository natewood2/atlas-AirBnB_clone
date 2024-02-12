#!/usr/bin/python3
""" Tests for the Review Class. """
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """ Testing the Review Class. """
    def test_Review_init(self):
        """ Testing Review. """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_Review_attributes(self):
        """ Testing the reviews attributes. """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
