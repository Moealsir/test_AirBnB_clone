#!/usr/bin/python3
"""Module containing the BaseModule class."""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModule class."""

    def __init__(self, *args, **kwargs):
        """
        initialize BaseModel instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """print string

        Returns:
            format: class_name, id, dict
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        """Save current object to database."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """>>

        Return a dictionary representation of an object.

        Returns:
            A dictionary with all attributes and their values.
        """
        the_dict = self.__dict__.copy()
        the_dict["__class__"] = self.__class__.__name__
        the_dict["updated_at"] = self.updated_at.isoformat()
        the_dict["created_at"] = self.created_at.isoformat()
        return the_dict


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)