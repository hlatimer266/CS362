"""
Helper functions for function 3 of assignment, conv_endian(num, endian='big')
"""


def convert_dec_to_hex(dec_val):
    """
    converts decimal parameter into
    hexadecimal notation number

    :param dec_val: val to convert to hex
    :return: string representing converted hex value
    """
    # list of hex values corresponding to element indexes
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7',
                  '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    reversed_hex = ""  # value is reversed post-conversion
    while dec_val > 0:
        last_digit = dec_val % 16
        reversed_hex += hex_digits[last_digit]
        dec_val -= last_digit  # store hex digit, then subtract dec value
        dec_val //= 16  # shift magnitude of num down by one in hex

    # reverse the string
    return reversed_hex[::-1]


def add_prefix(hex_val, is_negative):
    """
    Returns a formatted prefix
    as a string for a hexadecimal number

    :param is_negative: if true, add a '-'
    to returned prefix
    :param hex_val: if odd number of digits,
    add a '0' to returned prefix
    :return: string prefix for hex number
    """
    prefix = ""
    if is_negative:
        prefix += "-"
    if len(hex_val) % 2 != 0:
        prefix += "0"
    return prefix


def switch_endian(hex_val, is_negative):
    """
    Returns a hexadecimal number
    with a flipped endian format
    (ie, big -> little OR little -> big)

    :param is_negative: if true, handle '-' appropriately
    :param hex_val: hex value to toggle endian of and return
    :return: string hex number with switched endian
    """
    if is_negative:
        temp_byte_1 = hex_val[1:-6]
        temp_byte_2 = hex_val[4:-3]
        temp_byte_3 = hex_val[7:]
        hex_val = "-" + temp_byte_3 + " " + temp_byte_2 + " " + temp_byte_1
        return hex_val
    else:
        temp_byte_1 = hex_val[:-6]
        temp_byte_2 = hex_val[3:-3]
        temp_byte_3 = hex_val[6:]
        hex_val = temp_byte_3 + " " + temp_byte_2 + " " + temp_byte_1
        return hex_val


def format_hex(hex_val, is_negative):
    """
    Returns a big endian notation hex with
    string with spaces in between bytes

    :param hex_val: string value to format
    :param is_negative: used to determine prefix
    :return: big endian string w/ space-separated-bytes
    """
    formatted_hex = add_prefix(hex_val, is_negative)
    for hex_digit in range(0, len(hex_val)):
        formatted_hex += hex_val[hex_digit]
        if hex_digit % 2 == 0 and hex_digit != len(hex_val) - 1:
            formatted_hex += " "  # print a space if even
    return formatted_hex
