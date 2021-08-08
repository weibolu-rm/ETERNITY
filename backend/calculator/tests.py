from django.test import TestCase
# should be from models, but idk how to register the functions
from models import *
import numpy as np
import unittest

# ARCCOS(X)
# testing against numpy
def test_arccos(x):
    print(arccos(x))
    print(np.arccos(x))

def test_arccos_in_range(x):
    if arccos(x) is None:
        print(f"ASSERT ERROR: arccos(x) in expected range returned None with value {x}.")
        return 1
    return 0


def test_arccos_out_of_range(x):
    if arccos(x) is not None:
        print(f"ASSERT ERROR: arccos(x) out of range exception not handled with value {x}.")
        return 1
    return 0


def unit_test_arccos_range():
    i = -3
    while i < 3:
        # Not in the expected [-1, 1] range
        if i < -1 or i > 1:
            if test_arccos_out_of_range(i) == 1:
                return 1

        # In the expected [-1, 1] range
        if i >= -1 and i <= 1:
            if test_arccos_in_range(i) == 1:
                return 1

        i = i + 0.1
    print("Arccos(x): All range tests passed.")

def unit_test_arccos_np():
    print("Testing for accuracy against numpy:\n")
    # testing accuracy vs. numpy
    i = -1
    while i < 1:
        # for larger steps
        if i > 1:
            break

        print(arccos(i))
        print(np.arccos(i))
        i += 0.3

print("Testing Arccos(x)...")
unit_test_arccos_range()
unit_test_arccos_np()
print("Done.\n")

# Mean Absolute Deviation (MAD) Unit Test
class TestMeanAbsoluteDeviation(unittest.TestCase):

	def test_mad_of_positive_integers(self):
		self.assertTrue(mean_absolute_deviation([1,2,3,4]) == 1)

	def test_mad_of_negative_integers(self):
		self.assertTrue(mean_absolute_deviation([-1,-2,-3,-4]) == 1)
	
	def test_mad_of_mixed_integers(self):
		self.assertTrue(abs(mean_absolute_deviation([-2,-1,0,1,2]) - 1.2) < 0.0000001)
	
	def text_mad_of_floats(self):
		self.assertTrue(abs(mean_absolute_deviation([0.5,0.75,1.2,3.8]) - 1.11875) < 0.0000001)

if __name__ == '__main__':
    unittest.main()