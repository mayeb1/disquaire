import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from src.tools import Text_to_List

class Test_Text_to_List(unittest.TestCase):
    def test_success(self):
        actual = Text_to_List(path='./unit_test/test.txt')
        expected = ["Back to the Future 1","Back to the Future 2","Back to the Future 3","La chèvre"]
        self.assertEqual(actual, expected)

    def test_exception(self):
        with self.assertRaises(FileNotFoundError) as exception_context:
            Text_to_List(path='./tes.txt')
        self.assertEqual(str(exception_context.exception),"The file isn't in the path or cannot be read")
