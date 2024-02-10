#!/usr/bin/python3
"""Write all those classes that inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    def to_dict(self):
        """return a dictionary representation of the object"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict