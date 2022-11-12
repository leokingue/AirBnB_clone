#!/usr/bin/python3
""" testing Review """
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ check Review """

    def setUp(self):
        """Initialize the data"""
        self.review = Review()

    def test_if_ReviewIsSubclassBaseModel(self):
        """Check if Review is a Subclass of BaseModel"""
        self.assertIsInstance(self.review, BaseModel)
