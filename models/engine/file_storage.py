#!/usr/bin/python3
"""Class for a generic list of objects. """
import json
import os
import datetime as time
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    Class for serializing instances to a JSON file
    and deserializingJSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Adds an object to the storage."""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def all(self):
        """return  all objects"""
        return self.__objects

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path).
        """
        values = {}
        for key, value in self.__objects.items():

            values[key] = value.to_dict()
        with open(self.__file_path, "w", encoding=("utf-8")) as f:
            json.dump(values, f, indent=2)

    def reload(self):
        """
        Load data from the JSON file into __objects.
        If the file does not exist, create it with default data.
        """
        try:
            with open(self.__file_path, "r+", encoding="utf-8") as f:
                if os.stat(self.__file_path).st_size == 0:
                    return
                f.seek(0)
                data = json.load(f)
                for key, value in data.items():
                    self.__objects[key] = eval(value["__class__"])(**value)

        except FileNotFoundError:
            pass

    def class_dict(self):
        """
        to correctly serialize and deserialize instances of the new classes
        """
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        return class_dict

    def attribe(self):
        """Returns the valid attributes and their types for classname"""
        attribe = {
            "BaseModel": {
                "id": str,
                "created_at": time.datetime,
                "updated_at": time.datetime,
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str,
            },
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list,
            },
            "Review": {"place_id": str, "user_id": str, "text": str},
        }
        return attribe
