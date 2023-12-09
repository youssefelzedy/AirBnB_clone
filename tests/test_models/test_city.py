#!/usr/bin/python3
"""Test city"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class Testcity(unittest.TestCase):
    """
    unittests for city class
    """

    def test_class(self):
        """
        Tests if the class is named correctly.
        """
        cityy = City()
        self.assertEqual(cityy.__class__.__name__, "City")

    def test_class2(self):
        """
        Tests if class inherits from BaseModel.
        """
        cityy = City()
        self.assertTrue(issubclass(cityy.__class__, BaseModel))
