# https://github.com/cvkells07/lab_10_CK_AW.git
# Partner 1: Claire Kelleter
# Partner 2: Avery Walh

from calculator import *
import unittest

def test_multiply(self):
    self.assertEqual(mul(3,0), 0)
    self.assertEqual(mul(3,1), 3)
    self.assertEqual(mul(3,-1), -3)
    self.assertEqual(mul(30,3), 90)

def test_divide(self):
    self.assertEqual(div(3,0), "division by zero")
    self.assertEqual(div(3,1), 3)
    self.assertEqual(div(0, 3), 0)
    self.assertEqual(div(6,-3), -2)
    self.assertEqual(div(-6,3), -2)
    self.assertAlmostEqual(div(1,3), 1/3)

def test_log_invalid_argument(self):
    self.assertEqual(log(-2, 2), "logarithm undefined for non-positive a")

def test_hypotenuse(self):
    self.assertEqual(hypotenuse(3, 4), 5)
    self.assertEqual(hypotenuse(6, 8), 10)

def test_sqrt(self):
    self.assertEqual(square_root(-3), "square root cannont be for a num less than zero")
    self.assertEqual(square_root(3), 9)
    self.assertAlmostEqual(square_root(1/2), 1/4)