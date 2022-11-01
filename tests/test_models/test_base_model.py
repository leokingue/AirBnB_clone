#!/usr/bin/python3
import unittest
import models
from models.base_model import BaseModel
"""
 Create BaseModel from dictionary
 Update models/base_model.py:
 test_base_model.py
"""


class TestBaseModel(unittest.TestCase):
    """ Test for class BaseModel"""

    def setUp(self):
        """Initialize the data """
        self.p1 = BaseModel()
        self.p2 = BaseModel()

    def test_init_BaseModel(self):
        """test if an object is an type BaseModel"""
        self.assertIsInstance(self.p, BaseModel)

    def test_id(self):
        """ test that id is unique """
        self.assertNotEqual(self.p1.id, self.p2.id)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        _dict = self.p1.__dict__
        string1 = "[BaseModel] ({}) {}".format(self.p1.id, _dict)
        string2 = str(self.p1)
        self.assertEqual(string1, string2)

    def test_save(self):
        """ check if date update when save """
        first_updated = self.p1.updated_at
        self.p1.save()
        second_updated = self.p1.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        '''check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.'''
        my_model3 = BaseModel()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
