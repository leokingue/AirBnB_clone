#!/usr/bin/python3
""" testing State """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ check State """

    def setUp(self):
        """Initialize the data"""
        self.state1 = State()

    def test_if_StateIsSubClassBaseModel(self):
        """Check if State is a Subclass of BaseModel"""
        self.assertIsInstance(self.state1, BaseModel)
