import json
import locale
import os
from models.engine import customserializer
"""
FileStorage: a class FileStorage that serializes instances to,
 a JSON file and deserializes JSON file to instances

 Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by,
    <class name>.id (ex: to store a BaseModel object with id=12121212,
    the key will be BaseModel.12121212)
    __list_objects : objects list

 Public instance methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects ,
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file does not exist, no exception should be raised)
"""


class FileStorage:
    """ Implementation of the FileStorage Class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        ''' create empty dictionary'''
        objects_to_dict = {}
        for key, value in self.__objects.items():
            my_dict = self.__objects[key].__dict__
            objects_to_dict[key] = my_dict
        list_object_to_dict = list(objects_to_dict.values())
        with open(self.__file_path, mode="w+", encoding=locale.getpreferredencoding()) as file:
            for value_object_to_dict in list_object_to_dict:
                json.dump(value_object_to_dict, file, default=customserializer.to_json)
                file.write("\n")
            file.close()
        print(list_object_to_dict)

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists """
        final_list_reload_object = []
        final_list = []
        class_t = list(self.__objects.values())
        try:
            classes_t = class_t[0].__class__
        except IndexError:
            print(f"ERROR : Object list is Empety")
            return
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r+", encoding=locale.getpreferredencoding()) as file:
                list_objects_to_json = file.readlines()
                for item in list_objects_to_json:
                    container = json.loads(item)
                    final_list.append(container)
                file.close()
            for my_dict in final_list:
                my_instance = classes_t(my_dict)
                final_list_reload_object.append(my_instance)
            return final_list_reload_object
        else:
            print(f"The file {self.__file_path} does not exist. Attention!")
