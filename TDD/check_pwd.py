import re


def char_check(pwd):
    regex = re.compile('[-~`!@#$%^&*()_+=]')
    found_lower = False
    found_upper = False
    found_digit = False
    found_special_char = False

    for c in pwd:
        if c.islower():
            found_lower = True
        elif c.isupper():
            found_upper = True
        elif c.isdigit():
            found_digit = True
        elif regex.search(c):
            found_special_char = True

    return found_lower and found_upper and found_digit and found_special_char


def check_pwd(input):
    if len(input) < 8 or len(input) > 20:
        return False
    return char_check(input)
