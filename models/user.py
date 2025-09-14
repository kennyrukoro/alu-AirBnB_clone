#1/usr/bin/python3
"""Module to create user class"""

from models.base_model import BaseModel

class User(BaseModel):
    """Class for managing User objects"""
    
    email = ""
    password = ""
    firt_name = ""
    last_name = ""