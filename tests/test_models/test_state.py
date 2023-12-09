#!/usr/bin/python3
"""Test state"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class Teststate(unittest.TestCase):
    """
    unittests for state class
    """

    def test_class(self):
        """
        Tests if the class is named correctly.
        """
        statee = State()
        self.assertEqual(statee.__class__.__name__, "State")

    def test_class2(self):
        """
        Tests if class inherits from BaseModel.
        """
        statee = State()
        self.assertTrue(issubclass(statee.__class__, BaseModel))
