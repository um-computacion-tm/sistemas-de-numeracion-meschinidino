import unittest

from sistemas_num import *


class MyTest(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(0), 0)
        self.assertEqual(decimal_to_binary(1), 1)
        self.assertEqual(decimal_to_binary(2), 10)
        self.assertEqual(decimal_to_binary(9), 1001)
        self.assertEqual(decimal_to_binary(15), 1111)
        self.assertEqual(decimal_to_binary(255), 11111111)
        self.assertEqual(decimal_to_binary(512), 1000000000)
        self.assertEqual(decimal_to_binary(1023), 1111111111)
        self.assertEqual(decimal_to_binary(65535), 1111111111111111)
        self.assertEqual(decimal_to_binary(1048575), 11111111111111111111)

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal('0'), 0)
        self.assertEqual(binary_to_decimal('1'), 1)
        self.assertEqual(binary_to_decimal('10'), 2)
        self.assertEqual(binary_to_decimal('1001'), 9)
        self.assertEqual(binary_to_decimal('1111'), 15)
        self.assertEqual(binary_to_decimal('11111111'), 255)
        self.assertEqual(binary_to_decimal('1000000000'), 512)
        self.assertEqual(binary_to_decimal('1111111111'), 1023)
        self.assertEqual(binary_to_decimal('1111111111111111'), 65535)
        self.assertEqual(binary_to_decimal('11111111111111111111'), 1048575)

    def test_decimal_to_octal(self):
        self.assertEqual(decimal_to_octal(0), '0')
        self.assertEqual(decimal_to_octal(1), '1')
        self.assertEqual(decimal_to_octal(8), '10')
        self.assertEqual(decimal_to_octal(63), '77')
        self.assertEqual(decimal_to_octal(512), '1000')
        self.assertEqual(decimal_to_octal(1023), '1777')
        self.assertEqual(decimal_to_octal(4095), '7777')
        self.assertEqual(decimal_to_octal(65535), '177777')
        self.assertEqual(decimal_to_octal(262143), '777777')
        self.assertEqual(decimal_to_octal(1048575), '3777777')

    def test_octal_to_decimal(self):
        self.assertEqual(octal_to_decimal('0'), 0)
        self.assertEqual(octal_to_decimal('1'), 1)
        self.assertEqual(octal_to_decimal('10'), 8)
        self.assertEqual(octal_to_decimal('77'), 63)
        self.assertEqual(octal_to_decimal('1000'), 512)
        self.assertEqual(octal_to_decimal('1777'), 1023)
        self.assertEqual(octal_to_decimal('7777'), 4095)
        self.assertEqual(octal_to_decimal('177777'), 65535)
        self.assertEqual(octal_to_decimal('777777'), 262143)
        self.assertEqual(octal_to_decimal('3777777'), 1048575)

    def test_decimal_to_hex(self):
        self.assertEqual(decimal_to_hex(255), "ff")
        self.assertEqual(decimal_to_hex(4096), "1000")
        self.assertEqual(decimal_to_hex(65535), "ffff")

    def test_hex_to_decimal(self):
        self.assertEqual(hex_to_decimal("ff"), 255)
        self.assertEqual(hex_to_decimal("1000"), 4096)
        self.assertEqual(hex_to_decimal("ffff"), 65535)

    def test_octal_to_hexa(self):
        self.assertEqual(octal_to_hexa("10"), "8")
        self.assertEqual(octal_to_hexa("100"), "40")
        self.assertEqual(octal_to_hexa("377"), "ff")

    def test_octal_to_binary(self):
        self.assertEqual(octal_to_binary("10"), 1000)
        self.assertEqual(octal_to_binary("100"), 1000000)
        self.assertEqual(octal_to_binary("377"), 11111111)

    def test_hex_to_octal(self):
        self.assertEqual(hex_to_octal("8"), "10")
        self.assertEqual(hex_to_octal("40"), "100")
        self.assertEqual(hex_to_octal("ff"), "377")

    def test_hex_to_binary(self):
        self.assertEqual(hex_to_binary("8"), 1000)
        self.assertEqual(hex_to_binary("40"), 1000000)
        self.assertEqual(hex_to_binary("ff"), 11111111)

    def test_binary_to_octal(self):
        self.assertEqual(binary_to_octal("1000"), "10")
        self.assertEqual(binary_to_octal("1000000"), "100")
        self.assertEqual(binary_to_octal("11111111"), "377")

    def test_binary_to_hex(self):
        self.assertEqual(binary_to_hex("1000"), "8")
        self.assertEqual(binary_to_hex("1000000"), "40")
        self.assertEqual(binary_to_hex("11111111"), "ff")

    if __name__ == '__main__':
        unittest.main()
