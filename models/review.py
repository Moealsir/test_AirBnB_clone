#!/usr/bin/python3
"""Write all those classes that inherit from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""
