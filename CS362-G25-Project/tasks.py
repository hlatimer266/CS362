from math import floor

import num_conv_helper
import conv_endian_helper
from my_datetime_helper import is_leap_year, extra_days, \
    leap_years, reg_years, adjust_for_overflow_days


def conv_num(num_str):
    """
    Takes string and converts to base
    10 number. Accepts integer, float
    or hexidecimal numbers

    :param num_str: string of valid
    integer, float or hexidecimal number
    :return: integer or float

    """
    if type(num_str) is not str:
        return None

    if num_str == "":
        return None
    elif "0x" in num_str[:2] or "0X" in num_str[:2] \
            or "-0X" in num_str[:3] or "-0x" in num_str[:3]:
        return num_conv_helper.conv_hex_to_dec(num_str)
    elif "." in num_str and num_str.count(".") == 1:
        return num_conv_helper.conv_string_to_float(num_str)
    else:
        return num_conv_helper.conv_string_to_integer(num_str)


def my_datetime(num_sec):
    """
    Takes in an integer value that represents the number
    of seconds since the epoch, converts it to a date
    and returns it as a string with the format: MM-DD-YYYY.

    :param num_sec: int representing seconds since epoch
    :return: date as string in format MM-DD-YYYY
    """

    day_seconds = 86400
    total_days = floor(num_sec / day_seconds)
    four_year_days = 1461
    one_year_inc = 0

    # 1970 is not a leap year, first leap year is 1972
    # a 4-year period starting 01-01-1970 would be R R L R
    # where R = regular year and L = leap year
    days_in_years = [365, 365, 366, 365]

    # initialize epoch date values
    epoch_month = 1
    epoch_day = 1
    epoch_year = 1970

    # divide total days by increments of 4 years (3 regular, 1 leap)
    four_year_inc = floor(total_days / four_year_days)
    days_remaining = total_days % four_year_days

    # from remainder...decrement days by R, L, R days in year until
    for d in days_in_years:
        if days_remaining > 365:
            days_remaining -= d
            one_year_inc += 1

    year = epoch_year + (four_year_inc * 4) + one_year_inc

    days_remaining += extra_days(year)

    # special case for years that should have been leap
    special = 0
    if year % 4 == 0 and (year % 100 == 0 and year % 400 != 0):
        special = 1

    days_remaining, year = adjust_for_overflow_days(days_remaining, year)

    # if leap year
    if is_leap_year(year):
        days_remaining, months = leap_years(days_remaining)
    # if regular year
    else:
        if one_year_inc == 2 and (special == 1 or days_remaining > 59):
            days_remaining -= 1
        days_remaining, months = reg_years(days_remaining)

    month = epoch_month + months
    day = epoch_day + days_remaining

    return str(month).zfill(2) + '-' + str(day).zfill(2) + '-' + str(year)


def conv_endian(num, endian='big'):
    """
     Takes in an integer value as num and
     converts it to a hexadecimal number.
     The endian type is determined by the
     flag endian.

    :param num: int to be converted to hex (can be negative)
    :param endian: 'big' will return big endian formatted hex,
    'little' will return little endian, nothing is big endian
    by default and anything else will return None
    :return: The returned hex string will have each byte separated
    by a space and each byte must be two characters in length
    """
    if num == 0:
        return "00"
    elif num == "":
        return None
    # store boolean value & flip sign appropriately
    is_negative = num < 0
    if is_negative:
        num *= -1

    # convert decimal value to hexadecimal notation
    hex_val = conv_endian_helper.convert_dec_to_hex(num)

    # return formatted hex based on desired endian notation
    formatted_hex = conv_endian_helper.format_hex(hex_val, is_negative)
    if endian == 'big':
        return formatted_hex
    elif endian == 'little':
        return conv_endian_helper.switch_endian(formatted_hex, is_negative)
    else:
        return None
