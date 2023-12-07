#!/usr/bin/python3
''' BaseModel Class '''

import uuid
from datetime import datetime
import json
import models
import cmd

timedate = '%Y-%m-%dT%H:%M:%S.%f'

class BaseModel(cmd.Cmd):
    ''' BaseModel Class'''
    def __init__(self, *args, **kwargs):
        '''public instance Constructor '''
        if kwargs:
            self.__dict__ = kwargs
            if 'created_at' in kwargs:
                value = datetime.strptime(kwargs.get("created_at"), timedate)
            if 'updated_at' in kwargs:
                value = datetime.strptime(kwargs.get("updated_at"), timedate)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    
    def __str__(self):
        ''' __str_method '''
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                self.id, self.__dict__)

    def save(self):
        ''' save method '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' return a dictionary with created_at and updated_at '''
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        for key, value in my_dict.items():
            if isinstance(value, datetime):
                my_dict[key] = value.strftime(timedate)
        return my_dict
