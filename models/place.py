#!/usr/bin/python3
"""This modul is for creating place classs"""
from models.base_models import BaseModel

class Place(BaseModel):
    """This class manages Place objects"""
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtude = 0.0
    amenity_ids = []