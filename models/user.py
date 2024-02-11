#!/usr/bin/python3
"""Class User for handling user data."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class represents a user in the system"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
