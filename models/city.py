#!/usr/bin/python3#!/usr/bin/python3
"""Write all those classes that inherit from BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""
