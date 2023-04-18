import unittest

from sistemas_num import *


class MyTest(unittest.TestCase):
    def test_uno(self):
        self.assertEqual(decimal_to_binary(5), 101)

    def test_dos(self):
        self.assertEqual(decimal_to_binary(8), 1000)

    def test_tres(self):
        self.assertEqual(decimal_to_binary(16), 10000)

    def test_cuatro(self):
        self.assertEqual(binary_to_decimal(101), 5)

    def test_cinco(self):
        self.assertEqual(binary_to_decimal(1000), 8)

    def test_seis(self):
        self.assertEqual(binary_to_decimal(10000), 16)

if __name__ == "__main__":
    unittest.main()
