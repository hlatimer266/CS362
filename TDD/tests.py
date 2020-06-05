from unittest import TestCase
import unittest
from check_pwd import check_pwd


class TestCheckPwd(TestCase):
    def test_empty_string(self):
        empty_string = ""
        self.assertFalse(check_pwd(empty_string), msg="input not emtpy")

    def test_nonempty_string(self):
        not_empty = "Meow123!"
        self.assertTrue(check_pwd(not_empty), msg='input empty')

    def test_has_lower_case(self):
        upper_case_string = "MEOW123!"
        self.assertFalse(check_pwd(upper_case_string), msg='should be no upper case in input')

    def test_has_upper_case(self):
        lower_case_string = "meow123!"
        self.assertFalse(check_pwd(lower_case_string), msg='upper case letter in input')

    def test_lower_and_upper(self):
        upper_lower_string = "Meow123!"
        self.assertTrue(check_pwd(upper_lower_string), msg='should have upper and lower case')

    def test_no_digit(self):
        string_no_digits = "Meowmeow!"
        self.assertFalse(check_pwd(string_no_digits), msg="shouldn't have any digits")

    def test_has_digit(self):
        string_one_digit = "Meowmeow1!"
        self.assertTrue(check_pwd(string_one_digit), msg='has no digit')

    def test_has_no_special_char(self):
        no_special_chars = "Meowmeow1"
        self.assertFalse(check_pwd(no_special_chars), msg='has special char')

    def test_has_special_char(self):
        special_char = "Meow123-"
        self.assertTrue(check_pwd(special_char), msg="doesn't have a special char")

    def test_length_too_small(self):
        too_small_ps = "Meow1&"
        self.assertFalse(check_pwd(too_small_ps), msg='password meets min req')

    def test_min_length(self):
        min_length_pwd = "Meow123@"
        self.assertTrue(check_pwd(min_length_pwd), msg="password doesn't meet min length")

    def test_length_too_long(self):
        too_large_ps = "Meow1234567910123456&"
        self.assertFalse(check_pwd(too_large_ps), msg="password meets max length reqs")

    def test_max_length(self):
        max_length_ps = "Meow123456791012345&"
        self.assertTrue(check_pwd(max_length_ps), msg='password exceeds max length')

    def test_special_and_digit(self):
        special_and_digit = "-~`!@#$%^&*()_+=1"
        self.assertFalse(check_pwd(special_and_digit), msg='char added to password')

    def test_just_digits(self):
        just_digits = "12345678"
        self.assertFalse(check_pwd(just_digits), msg='assertion failed')

    def test_just_chars(self):
        just_chars = "Meowmeow"
        self.assertFalse(check_pwd(just_chars), msg='assertion failed')

    def test_char_and_special(self):
        char_and_spec = "Meow-~`!@#"
        self.assertFalse(check_pwd(char_and_spec), msg='assertion failed')

    def test_special_not_allowed(self):
        spec_not_allowed = "Meow123{"
        self.assertFalse(check_pwd(spec_not_allowed), msg='assertion failed')


if __name__ == '__main__':
    unittest.main(verbosity=2)
