#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing the BaseModel class """

    def setUp(self):
        """ Data initialization """
        self.data1 = BaseModel()
        self.data2 = BaseModel()

    def test_init_BaseModel(self):
        """Test if the instance is indeed a base model object """
        self.assertIsInstance(self.data1, BaseModel)

    def test_id_is_compliant(self):
        """Check if id is compliant"""
        self.assertIsInstance(self.data1.id, str)
        self.assertEqual(len(self.data1.id), 36)
        self.assertNotEqual(self.data1.id, self.data2.id)

    def test_save_method(self):
        """Test if save method works"""
        first_updated = self.data1.updated_at
        second_updated = self.data1.save()
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict_method(self):
        """Test if to_dict method works"""
        new_dict = self.data1.to_dict()
        self.assertIsInstance(new_dict, dict)
        for key, value in new_dict.items():
            flag = 0
            if new_dict["__class__"] == "BaseModel":
                flag += 1
            self.assertTrue(flag == 1)
        for key1, value1 in new_dict.items():
            if key1 == 'created_at':
                self.assertIsInstance(value1, str)
            if key1 == 'updated_at':
                self.assertIsInstance(value1, str)


if __name__ == "__main__":
    unittest.main()
