#!/usr/bin/python3
''' BaseModel Class '''

import uuid
from datetime import datetime
import models
import cmd

timedate = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel(cmd.Cmd):
    ''' BaseModel Class'''
    def __init__(self, *args, **kwargs):
        '''public instance Constructor '''
        for key, val in kwargs.items():
            if key == "created_at" or key == "updated_at":
                self.__dict__[key] = datetime.strptime(val, timedate)
            else:
                self.__dict__[key] = val
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        ''' __str_method '''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        ''' save method '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' return a dictionary with created_at and updated_at '''
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
