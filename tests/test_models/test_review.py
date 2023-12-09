#!/usr/bin/python3
"""Test review"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class Testreview(unittest.TestCase):
    """
    unittests for Review class
    """

    def test_class(self):
        """
        Tests if the class is named correctly.
        """
        revieww = Review()
        self.assertEqual(revieww.__class__.__name__, "Review")

    def test_class2(self):
        """
        Tests if class inherits from BaseModel.
        """
        revieww = Review()
        self.assertTrue(issubclass(revieww.__class__, BaseModel))

if __name__ == '__main__':
    unittest.main()
