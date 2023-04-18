def decimal_to_binary(num):
    binary = ""
    while num != 1:
        binary = str(num % 2) + binary[:]
        num = int(num/2)
    binary = "1" + binary
    return int(binary)
def binary_to_decimal(num):
    return decimal
def decimal_to_octal(num):
    return octal
def octal_to_decimal(num):
    return decimal
def decimal_to_hex(num):
    return hex
def hex_to_decimal(num):
    return decimal