import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from src.tools import SliceBaseTitle

class Test_SliceBaseTitle(unittest.TestCase):
    def test_success_without_mode(self):
        actual = SliceBaseTitle(title= "Star wars 2")
        expected = ("Star wars",None)
        self.assertEqual(actual, expected)

    def test_success_with_mode(self):
        actual = SliceBaseTitle(title= "Star wars 2",mode=True)
        expected = ("Star wars","2")
        self.assertEqual(actual, expected)

    def test_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            SliceBaseTitle(title= 5)
        self.assertEqual(str(exception_context.exception),"object cannot be slice")
