#!/usr/bin/python3
""" testing city """
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ check City """

    def setUp(self):
        """Initialize the data"""
        self.City_1 = City()

    def test_isSubclass_city(self):
        """Check City is subclass of BaseModel"""
        self.assertIsInstance(self.City_1, BaseModel)



