#!/usr/bin/python3
""" testing User """
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ check User """

    def setUp(self):
        """Initialize the date"""
        self.user1 = User()

    def test_if_UserIsSubclassBaseModel(self):
        """Check if User is a Subclass of BaseModel"""
        self.assertIsInstance(self.user1, BaseModel)
        