#!usr/bin/python3
"""this is the base model and  will contain public attributes and methods"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    
    """Class frmo whci all the classes will inherit"""
    
    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        args: 
        *args: list of arguments # Name["frank", "john", "doe"]
        ** kwargs: dictionary of key/values arguments # {"name": "frank", "age": 23}
        """
        
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT %H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "({}) ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)
    
    
    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict["created_at"].isoformat()
        my_dict['updated_at'] = my_dict["updated_at"].isoformat()
        return my_dict