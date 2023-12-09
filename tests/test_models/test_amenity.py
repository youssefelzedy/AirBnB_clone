#!/usr/bin/python3
"""Test Amenity"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class Testamenity(unittest.TestCase):
    """
    unittests for Amenity class
    """

    def test_class(self):
        """
        Tests if the class is named correctly.
        """
        amenityy = Amenity()
        self.assertEqual(amenityy.__class__.__name__, "Amenity")

    def test_class2(self):
        """
        Tests if class inherits from BaseModel.
        """
        amenityy = Amenity()
        self.assertTrue(issubclass(amenityy.__class__, BaseModel))


if __name__ == '__main__':
    unittest.main()
