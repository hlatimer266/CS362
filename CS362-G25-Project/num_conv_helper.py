def conv_hex_to_dec(num_str):
    """
    Helper function to convert
    valid hex string to integer

    :param num_str: string
    :return: integer
    """
    conversion_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                      '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'a': 10,
                      'B': 11, 'b': 11, 'c': 12, 'C': 12, 'd': 13, 'D': 13,
                      'e': 14, 'E': 14, 'f': 15, 'F': 15}

    is_negative = False

    # Check if 0x or 0X occur more then once
    if num_str.count("0x") > 1 or num_str.count("0X") > 1:
        return None

    # Check if number is negative
    if "-" in num_str:
        num_str = num_str.replace("-", "")
        is_negative = True

    if "0x" in num_str:
        stripped_input = num_str.replace("0x", "")
    elif "0X" in num_str:
        stripped_input = num_str.replace("0X", "")

    curr_exp = len(stripped_input) - 1
    base_ten_conv = 0

    for c in stripped_input:
        try:
            converted = conversion_map[c]
        except KeyError:
            return None

        base_ten_conv += converted*(16**curr_exp)
        curr_exp -= 1

    if is_negative:
        return base_ten_conv * -1

    return base_ten_conv


def base_ten_conversion(num_str, dec_flag):
    """
    Helper function to return string
    converted to base ten integer or
    floating point number

    :param num_str: string
    :param dec_flag: boolean
    :return: integer or float
    """
    conversion_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                      '6': 6, '7': 7, '8': 8, '9': 9}

    base_ten_conv = 0.0

    if dec_flag:
        size_exp = 1
    else:
        size_exp = len(num_str) - 1

    for c in num_str:
        try:
            converted = conversion_map[c]
        except KeyError:
            return None

        if dec_flag:
            base_ten_conv += converted * (10 ** -size_exp)
            size_exp += 1
        else:
            base_ten_conv += converted * (10 ** size_exp)
            size_exp -= 1

    return base_ten_conv


def conv_string_to_float(num_str):
    """
    Takes valid decimal input as
    string, splits string into
    number before and after decimal
    before converting to base 10
    numbers. Results are added
    together and then returned

    :param num_str: string
    :return: floating point
    """
    is_negative = False

    if "-" in num_str:
        num_str = num_str.replace('-', "")
        is_negative = True

    # Split string on decimal point
    split_input = num_str.split('.')

    before_dec = split_input[0]

    after_dec = split_input[1]

    # Get base 10 conversion of string
    base_ten_conv = base_ten_conversion(before_dec, False)
    base_ten_conv_dec = base_ten_conversion(after_dec, True)

    if is_negative:
        return (base_ten_conv + base_ten_conv_dec) * -1

    return base_ten_conv + base_ten_conv_dec


def conv_string_to_integer(num_str):
    """
    Takes valid integer string
    and returns integer

    :param num_str: string
    :return: integer
    """
    is_negative = False

    if "-" in num_str:
        num_str = num_str.replace("-", "")
        is_negative = True

    base_ten_conv = base_ten_conversion(num_str, False)

    if is_negative:
        return base_ten_conv * -1

    return base_ten_conv
