#!/usr/bin/python3
"""initialize the model"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

classes_dict = {
            'BaseModel': BaseModel,
        }

storage = FileStorage()
storage.reload()