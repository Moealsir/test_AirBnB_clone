#!/usr/bin/python3
"""Module containing the BaseModule class."""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModule class."""

    def __init__(self):
        """
        initialize BaseModel instance.
        """
        self.my_number = ''
        self.name = ''
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        
        
        

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                  self.id,
                                self.__dict__
                                ))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        the_dict = self.__dict__.copy()
        the_dict["__class__"] = self.__class__.__name__
        the_dict["updated_at"] = self.updated_at.isoformat()
        the_dict["created_at"] = self.created_at.isoformat()
        return the_dict


if  __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))