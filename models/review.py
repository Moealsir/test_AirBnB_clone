#!/usr/bin/python3
"""Write all those classes that inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    def __init__(self, *args, **kwargs):
        """initialize attributes"""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get("place_id", "")
        self.user_id = kwargs.get("user_id", "")
        self.text = kwargs.get("user_id", "")
