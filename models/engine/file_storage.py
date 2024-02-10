#!/usr/bin/python3
"""initialize the FileStorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new.dump(new_dict, f)
            dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_load = json.load(f)
                for val in obj_load.values():
                    self.new(eval(val["__class__"])(**val))
        except FileNotFoundError:
            pass
