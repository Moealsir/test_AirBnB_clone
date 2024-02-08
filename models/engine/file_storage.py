#!/usr/bin/python3
import json
from pathlib import Path
from ..base_model import BaseModel

class FileStorage:
    """
    Class for serializing instances to a JSON file
    and deserializingJSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}
    
    def new(self, obj):
        """ """
        self.__objects[obj.__class__.__name__ +'.' + obj.id] = obj
        
        
    def all(self):

        return self.__objects
    
    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path).
        """
        values = {}
        for key, value in self.__objects.items():
            values[key] = value.to_dict()
        json.dump(values, open(self.__file_path, 'w', encoding=('utf-8')), indent=2)
    
    def reload(self):
        try:
            with  open(self.__file_path, 'r+', encoding=('utf-8')) as f:
                f.seek(0)
                data = json.load(f)
                for  key, value in data.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
            
        except Exception:
            pass
        