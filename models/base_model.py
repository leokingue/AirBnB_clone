#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"""
The BaseModel class is a parent class for future objects in our AirBnB web project.
 It will have the following attributes:

        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime when an instance is created
        updated_at: datetime - assign with the current datetime when an instance is created,
        and it will be updated every
         time you change your object

 A method inherited from the redefined Object super class:

        self.__str__: should print: [<class name>] (<self.id>) <self.__dict__>

 Public instance methods:
        save(self): updates the public instance attribute updated_at with the current datetime
        to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance

"""
'''
IMPORTANT:To reload an object use the storage instance on the reload method
            storage.reload()
            <storage> is an instance of FileStorage
            Respect The rules !
'''


class BaseModel:
    """ Implementation of the BaseModel class """
    def __init__(self, *args, **kwargs):
        """ The constructor of the BaseModel class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = str(datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                if key == "updated_at":
                    self.updated_at = str(datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))

    def __str__(self):
        """ Show current object information """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = str(datetime.fromisoformat(str(self.created_at)))
        new_dict['updated_at'] = str(datetime.fromisoformat(str(self.updated_at)))
        return new_dict


if __name__ == "__main__":
    b1 = BaseModel()
    b1.save()
