#!/usr/bin/python3
""" testing Place """
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ check Place """

    def setUp(self):
        """Initialize the data"""
        self.place = Place()

    def test_if_PlaceIsInstanceBasemodel(self):
        """Check if Place is a subclass of BaseModel """
        self.assertIsInstance(self.place, BaseModel)

