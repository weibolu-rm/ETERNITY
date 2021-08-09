from django.test import TestCase
from calculator.models import *

# ARCCOS(X)
# testing against numpy
class TestArccos(TestCase):

    # absolute error range <= 6.753e-5
    def test_arccos(self):
        self.assertTrue(arccos(1 == 0))
        self.assertTrue(abs(arccos(-1) - pi) <= 0.00006753)
        self.assertTrue(abs(arccos(0) - pi/2) <= 0.00006753)


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
        self.assertTrue(mean_absolute_deviation([1,2,3,4]) == 1)

    def test_mad_of_negative_integers(self):
        self.assertTrue(mean_absolute_deviation([-1,-2,-3,-4]) == 1)

    def test_mad_of_mixed_integers(self):
        self.assertTrue(abs(mean_absolute_deviation([-2,-1,0,1,2]) - 1.2) < 0.0000001)

    def text_mad_of_floats(self):
        self.assertTrue(abs(mean_absolute_deviation([0.5,0.75,1.2,3.8]) - 1.11875) < 0.0000001)

