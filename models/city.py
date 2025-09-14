#!/usr/bin/python3
"""Thids module creates a User class"""

from models.base_model import BaseModel

class City(BaseModel):
    """Class for managing city objects"""
    
    state_id = ""
    name = ""