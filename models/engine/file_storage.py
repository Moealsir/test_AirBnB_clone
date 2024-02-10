#!/usr/bin/python3

"""The FileStorage class"""

import os
import json
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
import datetime as time

class FileStorage:
    """
    FileStorage class that serializes instances to a JSON file and deserializes
    JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """a function that return the dictionary object"""

        return FileStorage.__objects

    def new(self, obj):
        """a function that add elements in the dictionary.
        Args:
            obj: The object to set with key <obj class name>.id
        """
        if obj:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """function to serializes __objects to JSON file (path: __file_path)
        """
        new_dictionary = {}
        for keys, values in FileStorage.__objects.items():
            new_dictionary[keys] = values.to_dict()

        with open(FileStorage.__file_path, 'w') as obj:
            json.dump(new_dictionary, obj)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as file:
                new_object_dict = json.load(file)
            for keys, val in new_object_dict.items():
                FileStorage.__objects[keys] = eval(val['__class__'])(**val)

    def delete(self, obj):
        """Deletes obj from __objects
        """
        try:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            del self.__objects[key]
            return True
        except Exception:
            return False

    def calss_dict(self)
        """to cottectly deserializes the JSON file  """

        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        return class_dict
