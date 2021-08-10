from django.test import TestCase
from calculator.models import *


# ARCCOS(X)
class TestArccos(TestCase):

    # absolute error range <= 6.753e-5
    def test_arccos(self):
        self.assertTrue(arccos(1) == 0)
        self.assertTrue(abs(arccos(-1) - pi) <= 0.00006753)
        self.assertTrue(abs(arccos(0) - pi / 2) <= 0.00006753)

    # [-1, 1]
    def test_arccos_range(self):
        self.assertEqual(arccos(1.000001), None)
        self.assertEqual(arccos(-1.000001), None)
        self.assertEqual(arccos(3), None)
        self.assertEqual(arccos(-3), None)
        self.assertEqual(arccos(300), None)
        self.assertEqual(arccos(-300), None)

        self.assertNotEqual(arccos(0.5), None)
        self.assertNotEqual(arccos(-0.5), None)
        self.assertNotEqual(arccos(0.3), None)
        self.assertNotEqual(arccos(-0.3), None)
        self.assertNotEqual(arccos(1), None)
        self.assertNotEqual(arccos(-1), None)


# Mean Absolute Deviation (MAD) Unit Test
class TestMeanAbsoluteDeviation(TestCase):

    def test_mad_of_positive_integers(self):
        self.assertTrue(mean_absolute_deviation([1, 2, 3, 4]) == 1)

    def test_mad_of_negative_integers(self):
        self.assertTrue(mean_absolute_deviation([-1, -2, -3, -4]) == 1)

    def test_mad_of_mixed_integers(self):
        self.assertTrue(abs(mean_absolute_deviation([-2, -1, 0, 1, 2]) - 1.2) < 0.0000001)

    def test_mad_of_floats(self):
        self.assertTrue(abs(mean_absolute_deviation([0.5, 0.75, 1.2, 3.8]) - 1.11875) < 0.0000001)


# Log Unit Test
class TestLog(TestCase):
    def test_log(self):
        self.assertTrue(round(log(0.1), 8) == -1)
        self.assertTrue(round(log(1), 8) == 0)
        self.assertTrue(round(log(10), 8) == 1)
        self.assertTrue(round(log(100), 8) == 2)
        self.assertTrue(round(log(1000), 8) == 3)
        self.assertTrue(round(log(10000), 8) == 4)

        self.assertTrue(round(ln(3), 8) == 1.09861229)
        self.assertEqual(log(0), None)
        self.assertEqual(log(-1), None)


# ab^x Unit Test
class TestExponential(TestCase):
    def testOne(self):
        self.assertTrue(exponential(1, 100) == 1)

    def testOneE(self):
        self.assertTrue(exponential(100, 1) == 100)

    def testPositive(self):
        self.assertTrue(exponential(2, 4) == 16)

    def testNegative(self):
        self.assertTrue(exponential(-2, 4) == 16)

    def testNegative2(self):
        self.assertTrue(exponential(-2, 3) == -8)


# Sinh Unit Test
class TestSinh(TestCase):
    def test_sinh(self):
        # test sinh(x) at a = 0
        self.assertTrue(sinh(0) == 0)
        # test if sinh(-x) == -sinh(x)
        self.assertTrue(sinh(-10) == -1 * sinh(10))
        # test precision of sinh(x) to 8 decimal places and test if fractional arguments work
        self.assertTrue(round(sinh(0.1), 8) == 0.10016675)
        # test to 4 decimal places
        self.assertTrue(round(sinh(1), 4) == 1.1752)


# Standard deviation (SD) Unit Test
class TestStandardDeviation(TestCase):

    def test_sd_of_positive_integers(self):
        self.assertTrue((standard_deviation(10, 12, 23, 23, 16, 23, 21, 16) - 4.898979485566356) < 0.0000001)

    def test_sd_of_negative_integers(self):
        self.assertTrue((standard_deviation(-10, -12, -23, -16, -21) - 5.003998401278722) < 0.0000001)

    def test_sd_of_mixed_integers(self):
        self.assertTrue((standard_deviation(10, -12, 23, -23, 16, 23, -21, -16) - 18.65475810617763) < 0.0000001)

    def test_sd_of_floats(self):
        self.assertTrue((standard_deviation(1.0, 1.2, 1.6, 3.2, 2.4) - 0.8158431221748451) < 0.0000001)
