import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from src.tools import OrderPrice

class Test_OrderPrice(unittest.TestCase):
    def test_success(self):
        orderList=["Back to the Future 1","Back to the Future 2","Back to the Future 3","La chèvre"]
        actual = OrderPrice(orderList=orderList)
        expected = 56
        self.assertEqual(actual, expected)
