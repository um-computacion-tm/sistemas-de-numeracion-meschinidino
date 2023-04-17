import unittest

from sistemas_num import *

class MyTest(unittest.TestCase):
    def test_uno(self):
        self.assertEqual(decimal_to_binary(5), 101)