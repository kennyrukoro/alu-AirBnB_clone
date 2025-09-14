#!/usr/bin/python3
"""This module creates a Review class"""

from models.base_models import BaseModel

class Review(BaseModel):
    """Class for managing review objrcts"""
    place_id =""
    user_id = ""
    text = ""