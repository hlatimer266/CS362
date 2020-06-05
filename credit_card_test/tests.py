from unittest import TestCase
import unittest
from credit_card_validator import credit_card_validator

'''
    credit_card_validtor module unit tests :
    All tests were generated via manual testing by
    implementing either the boundary conditions (L = 16
    for card with max length 15 should return false , etc..)
    or common error checks i.e. valid inputs should
    return true and invalid inputs should return false.

    Developer - Harrison Latimer
    Class - CS 362 (Spring 2020)
'''


class TestCredCardNumber(TestCase):

    # Bug 3 - Valid card number (Visa) but an integer : Found via manual test
    # using common error check - valid input but improper input format (not a
    # string value)
    def test_valid_card_int(self):
        ccn = 4113601974804222
        self.assertFalse(credit_card_validator(ccn), msg=f"{ccn} is invalid")

    # Bug 4 - invalid check sum with valid prefix (American Express) :
    # Found via manual test using common error condition methodology -
    # All invalid check sums should return false (domain constraint)
    def test_valid_prefix_bad_checksum(self):
        ccn = "349840222276842"
        self.assertFalse(credit_card_validator(ccn), msg=f"{ccn} is invalid")

    # Bug 1 - empty string input : Found via manual test by implementing
    # common error check - valid input and boundary condition : size = 0
    def test_empty_card(self):
        ccn = ""
        self.assertFalse(credit_card_validator(ccn), msg=f"{ccn} is invalid")

    # Bug 2 - valid prefix (Visa) and checksum but size is 15 not 16
    # : Found via manual test using boundary condition methodology.
    # Upper limit for visa cards is L = 16 but function L could be
    # 15. Validate boundary holds.
    def test_valid_check_too_short(self):
        ccn = "400000000000006"
        self.assertFalse(credit_card_validator(ccn), msg=f"{ccn} is invalid")

    # Bug 5 - valid prefix (American Express) and checksum but
    # size is 16 rather then 15 : Found via manual test using
    # boundary condition methodology (see bug 2 for explanation)
    def test_amExp_card_too_long(self):
        ccn = "3400000000000000"
        self.assertFalse(credit_card_validator(ccn), msg=f"{ccn} is invalid")

    # Bug 6 - valid prefix and check sum should be true but instead is false
    # : Found via manual test (and a crap ton of help from Eric Ianni and
    #   Wendy Roberts :) by implementing common error methodology -
    # verify true values are true (common error check)
    def test_master_card_prefix_boundary(self):
        ccn = "2720000000000005"
        self.assertTrue(credit_card_validator(ccn), msg=f"{ccn} is invalid")

    # Check 51-55 prefix range with valid check sum : Manual test which
    # implements common error check (valid input should be true)
    def test_master_card_prefix_fiveOne(self):
        ccn = "5214933908062378"
        self.assertTrue(credit_card_validator(ccn), msg=f"{ccn} is invalid")

    # Check 37 prefix with valid check sum : Manual test which implements
    # common error check (valid input should return true)
    def test_amExpr_card_prefix_threeSeven(self):
        ccn = "371309110920366"
        self.assertTrue(credit_card_validator(ccn), msg=f"{ccn} is invalid")


if __name__ == '__main__':
    unittest.main(verbosity=2)
