#!/usr/bin/python3
""" testing Amenity """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ check Amenity """

    def setUp(self):
        """ Initialize the Data"""
        self.Am = Amenity()

    def test_if_AmenityIsSubClass(self):
        """ Check if Amenity is a Subclass of BaseModel"""
        self.assertIsInstance(self.Am, BaseModel)
