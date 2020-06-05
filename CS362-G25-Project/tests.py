import unittest
import random

from datetime import datetime
from tasks import my_datetime, conv_num, conv_endian


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertTrue(True)

    '''
        Unit tests for function 2 - my_datetime(num_sec)
    '''

    # test 0 - epoch start
    def test_zero(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    # edge cases - first/last second of day
    def test_last_second_epoch_day(self):
        self.assertEqual(my_datetime(86399), "01-01-1970")

    def test_first_second_new_day(self):
        self.assertEqual(my_datetime(86400), "01-02-1970")

    def test_first_second_first_leap_day_after_epoch(self):
        self.assertEqual(my_datetime(68169600), "02-29-1972")

    def test_last_second_first_leap_day_after_epoch(self):
        self.assertEqual(my_datetime(68255999), "02-29-1972")

    def test_leap_day_first_second(self):
        self.assertEqual(my_datetime(1456704000), "02-29-2016")

    def test_leap_day_last_second(self):
        self.assertEqual(my_datetime(1456790399), "02-29-2016")

    def test_november_nonleap(self):
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    def test_december_nonleap(self):
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

    def test_far_in_future_first_second_of_day(self):
        self.assertEqual(my_datetime(25337577600), "12-01-2772")

    # examples from assignment
    def test_asgmt_example_1(self):
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    def test_asgmt_example_2(self):
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

    # failed during original testing - confirm now working
    # edge case first of month
    def test_first_of_month(self):
        self.assertEqual(my_datetime(23146902924), "07-01-2703")

    # edge case end of month
    def test_end_of_month(self):
        self.assertEqual(my_datetime(5856362124), "07-31-2155")

    # edge case first of year
    def test_first_of_year(self):
        self.assertEqual(my_datetime(15620858124), "01-01-2465")

    # edge case end of year
    def test_last_of_year(self):
        self.assertEqual(my_datetime(9688029324), "12-31-2276")

    # first of year after year that should have been leap but not
    def test_special_non_leap_year(self):
        self.assertEqual(my_datetime(7289738124), "01-01-2201")

    # randomly generate seconds
    def test_random(self):
        for i in range(0, 1000):
            num_secs = random.randint(0, 253402300799)
            self.assertEqual(my_datetime(num_secs),
                             datetime.utcfromtimestamp(num_secs).
                             strftime('%m-%d-%Y'))

    '''
        Unit tests for conv_num function
    '''

    # Happy path tests (AKA, all valid input verified)
    def test_valid_hex(self):
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test_valid_hex_upper_X(self):
        self.assertEqual(conv_num('0XAD4'), 2772)

    def test_valid_hex_lower_letter(self):
        self.assertEqual(conv_num('0xaD4'), 2772)

    def test_valid_hex_negative(self):
        self.assertEqual(conv_num('-0xFF'), -255)

    def test_valid_float(self):
        self.assertEqual(conv_num('.45'), 0.45)

    def test_valid_float_zeros_outfront(self):
        self.assertEqual(conv_num('000.45'), 0.45)

    def test_valid_float_zeros_outfront_more(self):
        self.assertEqual(conv_num('000.450000'), 0.45)

    def test_valid_float_just_decimal(self):
        self.assertEqual(conv_num('12.'), 12.0)

    def test_valid_float_negative(self):
        self.assertEqual(conv_num('-12.'), -12.0)

    def test_valid_integer(self):
        self.assertEqual(conv_num('12345'), 12345)

    def test_valid_integer_negative(self):
        self.assertEqual(conv_num('-1234'), -1234)

    # Failure modes
    def test_big_invalid_hex(self):
        self.assertEqual(conv_num('00x75BCD15'), None)

    def test_too_many_x_zero(self):
        self.assertEqual(conv_num('-0x0x75BCD15'), None)

    def test_too_many_x_zero_2(self):
        self.assertEqual(conv_num('-0x-0x75BCD15'), None)

    def test_invalid_hex_letter(self):
        self.assertEqual(conv_num('0xAh4'), None)

    def test_invalid_hex_two_oh_x(self):
        self.assertEqual(conv_num('0x0x4'), None)

    def test_invalid_integer_with_letter(self):
        self.assertEqual(conv_num('1234a'), None)

    def test_invalid_float_too_many_periods(self):
        self.assertEqual(conv_num('123.34.1'), None)

    def test_empty_string(self):
        self.assertEqual(conv_num(""), None)

    def test_big_empty_string(self):
        self.assertEqual(conv_num("  123"), None)

    def test_integer_input(self):
        self.assertEqual(conv_num(123), None)

    def test_func_3_positive_big(self):
        self.assertEqual(conv_endian(954786, 'big'), "0E 91 A2")

    def test_func_3_positive_none(self):
        self.assertEqual(conv_endian(954786), "0E 91 A2")

    def test_func_3_positive_little(self):
        self.assertEqual(conv_endian(954786, 'little'), "A2 91 0E")

    def test_func_3_negative_little(self):
        self.assertEqual(conv_endian(-954786, 'little'), "-A2 91 0E")

    def test_func_3_positive_junk(self):
        self.assertEqual(conv_endian(954786, 'foobar'), None)

    def test_func_3_negative_junk(self):
        self.assertEqual(conv_endian(-954786, 'foobar'), None)

    def test_func_3_zero_junk(self):
        self.assertEqual(conv_endian(0, 'big'), "00")

    def test_func_3_empty_junk(self):
        self.assertEqual(conv_endian("", 'foobar'), None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
