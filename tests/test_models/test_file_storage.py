#!/usr/bin/python3
import unittest
import sys
sys.path.append("../../models/engine")
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import locale

class TestFileStorage(unittest.TestCase):
    """ Test class for the FileStorage class"""
    def setUp(self):
        """Initialize the data for testing"""
        self.storage_data = FileStorage()
        self.bd1 = BaseModel()
        self.bd2 = BaseModel()
        self.bd3 = BaseModel()

    def test_checkMethod_all(self):
        """Check if the all method works"""
        my_dict = self.storage_data.all()
        self.assertIsInstance(my_dict, dict)

    def test_checkMethod_new(self):
        """Check if the new method works"""
        self.storage_data.new(self.bd1)
        my_dict = self.storage_data.all()
        my_list = list(my_dict.values())
        self.assertIsInstance(my_list[0], BaseModel)

    def test_checkMethod_save(self):
        """Check if the save method works"""
        self.storage_data.new(self.bd1)
        self.storage_data.new(self.bd2)
        self.storage_data.new(self.bd3)
        self.storage_data.save()
        numbers_of_lines = 0
        with open("../../models/engine/file.json", mode="r+", encoding=locale.getpreferredencoding()) as file:
            list_content = file.readlines()
            numbers_of_lines = len(list_content)
        self.assertEqual(numbers_of_lines, 3)

    def test_checkMethod_reload(self):
        """Check if the reload method works"""
        self.storage_data.new(self.bd1)
        self.storage_data.new(self.bd2)
        self.storage_data.new(self.bd3)
        self.storage_data.save()
        new_list_objects = self.storage_data.reload()
        self.assertIsInstance(new_list_objects[0], BaseModel)


if __name__ == "__main__":
    unittest.main()