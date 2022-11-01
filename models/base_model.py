#!/usr/bin/python
"""
The BaseModel class is a parent class for future objects in our AirBnB
It will have the following attributes:
    id: string - assign with an uuid when an instance is created
    created_at: datetime - assign with the current datetime when an instance
    updated_at: datetime - assign with the current datetime when an instance

Public instance methods:
save(self): updates the public instance attribute updated_at with the curr
to_dict(self): returns a dictionary containing all keys/values of __dict__

A method inherited from the redefined Object super class:
self.__str__: should print: [<class name>] (<self.id>) <self.__dict__>

"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Implementation of the BaseModel class """
    def __init__(self, *args, **kwargs):
        """ The constructor of the BaseModel class """
        if kwarg:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Show current object information """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute updated_at with the curren"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = datetime.isoformat(self.created_at)
        new_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return new_dict
