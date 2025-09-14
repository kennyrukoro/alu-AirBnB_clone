#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
import os
import datetime

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {} #this will store all the objects by <class.name>.id
    
    
    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id) # creates a key for the object in the format ClassName.id
        FileStorage.__object[key] = obj # adds the object to the __objects dictionary with the created key
        
    def save(self):
        """Seraializes __objects to the JSON file (path: __file_path)"""
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k,v in FileStorage.__objects.items()} # creates a dictionary of the objects in __objects with their to_dict() representation
            json.dumps(d,f)
            
    def classes(self):
        """Return a dictionary of vslid classes and their references"""
        from models.base_models import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        
        classes = {
            "BaseModel": BaseModel,
            "State": State,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            
        }
        
        return classes
    
    def reload(self):
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)}
            # TODO: should this iverwrite or insert?
            FileStorage.__objects = obj_dict
    
    def attributes(self):
        """Returns the valid attribuites and their types for classname"""
        attributes = {
            "BaseModel":
                {
                    "id":str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime
                },
            "User":
                {
                    "emial": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str
                },
            "State":
                {
                    "name": str
                },
            "City":
                {
                    "state_id": str
                },
            "Amenity":
                {
                    "name": str
                },
            "place":
                {
                    "city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "place_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list
                
                },
            "Reviews":
                {
                    "place_id": str,
                    "user_id": str,
                    "text": str
                }
        } 
        return attributes