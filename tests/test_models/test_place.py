#!/usr/bin/python3
"""Test place"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class Testplace(unittest.TestCase):
    """
    unittests for Place class
    """

    def test_class(self):
        """
        Tests if the class is named correctly.
        """
        placee = Place()
        self.assertEqual(placee.__class__.__name__, "Place")

    def test_class2(self):
        """
        Tests if class inherits from BaseModel.
        """
        placee = Place()
        self.assertTrue(issubclass(placee.__class__, BaseModel))


if __name__ == '__main__':
    unittest.main()
