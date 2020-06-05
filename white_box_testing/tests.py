from unittest import TestCase
import unittest
from contrived_func import contrived_func


class TestBranchAndConditions(TestCase):
    def test_conditions_1(self):
        self.assertFalse(contrived_func(6), msg=f"assert failed")

    def test_conditions_2(self):
        self.assertTrue(contrived_func(101), msg=f"assert failed")

    def test_conditions_3(self):
        self.assertFalse(contrived_func(151), msg=f"assert failed")

    def test_conditions_4(self):
        self.assertTrue(contrived_func(10), msg=f"assert failed")

    def test_conditions_5(self):
        self.assertTrue(contrived_func(100), msg=f"assert failed")

    def test_conditions_6(self):
        self.assertTrue(contrived_func(60), msg=f"assert failed")

    def test_conditions_7(self):
        self.assertFalse(contrived_func(51), msg=f"assert failed")


if __name__ == '__main__':
    unittest.main(verbosity=2)
