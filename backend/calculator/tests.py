from django.test import TestCase
# should be from models, but idk how to register the functions
from calculator.views import *
import numpy as np

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
