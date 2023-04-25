def decimal_to_binary(num):
    binary = ""
    while num != 1:
        binary = str(num % 2) + binary[:]
        num = int(num / 2)
    binary = "1" + binary
    return int(binary)


def binary_to_decimal(num):
    return int(num, 2)


def decimal_to_octal(num):
    return oct(num)[2:]


def octal_to_decimal(num):
    return int(num, 8)


def decimal_to_hex(num):
    return hex(num)[2:]


def hex_to_decimal(num):
    return int(num, 16)


def octal_to_hexa(num):
    decimal = octal_to_decimal(num)
    return decimal_to_hex(decimal)


def octal_to_binary(num):
    decimal = octal_to_decimal(num)
    return decimal_to_binary(decimal)


def hex_to_octal(num):
    decimal = hex_to_decimal(num)
    return decimal_to_octal(decimal)


def hex_to_binary(num):
    decimal = hex_to_decimal(num)
    return decimal_to_binary(decimal)


def binary_to_octal(num):
    decimal = binary_to_decimal(num)
    return decimal_to_octal(decimal)


def binary_to_hex(num):
    decimal = binary_to_decimal(num)
    return decimal_to_hex(decimal)
