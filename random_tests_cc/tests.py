from unittest import TestCase
import unittest
import random
from credit_card_validator import credit_card_validator


class TestCredCardNumber(TestCase):
    def test_totally_random_l1_l16(self):
        for x in range(0, 1000):

            random_val = random.randint(1, 9999999999999999)

            random_num_to_list = [int(d) for d in str(random_val)]

            cc_str_list = [str(i) for i in random_num_to_list]

            cc = int("".join(cc_str_list))

            credit_card_validator(str(cc))

    def test_totally_random_l16(self):

        for x in range(0, 100):

            random_val = random.randint(1000000000000000, 9999999999999999)

            rest_of_card = [int(d) for d in str(random_val)]

            cc_list = rest_of_card

            cc_str_list = [str(i) for i in cc_list]

            cc = int("".join(cc_str_list))

            credit_card_validator(str(cc))

    def test_totally_random_l15(self):

        for x in range(0, 1000):

            random_val = random.randint(4052000000000000, 4052999999999999)

            rest_of_card = [int(d) for d in str(random_val)]

            cc_list = rest_of_card

            cc_str_list = [str(i) for i in cc_list]

            cc = int("".join(cc_str_list))

            credit_card_validator(str(cc))

    def test_prefix_range_mastercard(self):
        for x in range(0, 1000):
            for i in range(2221, 2721):
                cc_prefix = [int(d) for d in str(i)]

                random_val = random.randint(100000000000, 999999999999)

                rest_of_card = [int(d) for d in str(random_val)]

                cc_list = cc_prefix + rest_of_card

                cc_str_list = [str(i) for i in cc_list]

                cc = int("".join(cc_str_list))

                credit_card_validator(str(cc))

    def test_prefix_range_am_exp_1(self):
        for x in range(0, 100):

            random_val = random.randint(340000000000000, 349999999999999)

            rest_of_card = [int(d) for d in str(random_val)]

            cc_str_list = [str(i) for i in rest_of_card]

            cc = int("".join(cc_str_list))

            credit_card_validator(str(cc))

    def test_prefix_range_am_exp_2(self):
        for x in range(0, 100):

            random_val = random.randint(370000000000000, 379999999999999)

            rest_of_card = [int(d) for d in str(random_val)]

            cc_str_list = [str(i) for i in rest_of_card]

            cc = int("".join(cc_str_list))

            credit_card_validator(str(cc))


if __name__ == '__main__':
    unittest.main(verbosity=2)
