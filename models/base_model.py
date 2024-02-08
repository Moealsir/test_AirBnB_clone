#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    
    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        Update the updated_at attribute and save the instance to the file storage.
        """
        self.updated_at = datetime.now()

        models.storage.save()

    def to_dict(self):
        the_dict = self.__dict__.copy()
        the_dict["__class__"] = self.__class__.__name__
        the_dict["updated_at"] = self.updated_at.isoformat()
        the_dict["created_at"] = self.created_at.isoformat()
        return the_dict
    
