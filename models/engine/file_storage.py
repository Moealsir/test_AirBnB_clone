#!/usr/bin/python3
# description of code
"""FileStorage class to store content"""
import json


class FileStorage:
    """
    Class for serializing instances to a JSON file
    and deserializingJSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return  a dictionary of objects in memory"""
        return self.__objects

    def new(self, obj):
        """Add a new object instance to the dictionary __objects."""
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialize __objects to the JSON file"""
        with open(self.__file_path, "w") as fp:
            json.dump(self.__objects, fp, default=str)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.load(json_file)
        except Exception:
            pass


if __name__ == "__main__":
    from models import storage
    from models.base_model import BaseModel

    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
