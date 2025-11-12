# https://github.com/cvkells07/lab_10_CK_AW.git
# Partner 1: Claire Kelleter
# Partner 2: Avery Walh

from calculator import *
import unittest


class TestCalculator(unittest.TestCase):
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
        self.assertEqual(logarithm(-2, 2), "logarithm undefined for non-positive a")

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self):
        self.assertEqual(square_root(-3), "square root cannont be for a num less than zero")
        self.assertEqual(square_root(3), 9)
        self.assertAlmostEqual(square_root(1/2), 1/4)
    
    def test_add(self):
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(0,3), 3)
        self.assertEqual(add(4,0), 4)
        self.assertEqual(add(5,1), 6)
        self.assertEqual(add(-1,3), 2)
        self.assertEqual(add(5,-2), 3)
        self.assertEqual(add(-4,-8), -12)
        self.assertEqual(add(-3,0), -3)

    def test_subtract(self):
        self.assertEqual(subtract(0,0), 0)
        self.assertEqual(subtract(5,0), 5)
        self.assertEqual(subtract(0,5), -5)
        self.assertEqual(subtract(3,2), 1)
        self.assertEqual(subtract(2,3), -1)
        self.assertEqual(subtract(3,-1), 4)
        self.assertEqual(subtract(-2,4), -6)
        self.assertEqual(subtract(-3,-3), 0)

    def test_divide_by_zero(self):
        self.assertEqual(div(0,0), "division by zero")

    def test_logarithm(self):
        self.assertEqual(round(logarithm(10, 10), 5), 1.0)
        self.assertEqual(round(logarithm(100, 10), 5), 2.0)
        self.assertEqual(round(logarithm(1, 10), 5), 0.0)
        self.assertEqual(round(logarithm(8, 2), 5), 3.0)
        self.assertEqual(round(logarithm(16, 2), 5), 4.0)
        self.assertEqual(round(logarithm(1, 2), 5), 0.0)
        self.assertEqual(round(logarithm(math.e, math.e), 5), 1.0)
        self.assertEqual(round(logarithm(math.e**3, math.e), 5), 3.0)
        self.assertEqual(round(logarithm(1, math.e), 5), 0.0)
        self.assertEqual(round(logarithm(27, 3), 5), 3.0)
        self.assertEqual(round(logarithm(81, 9), 5), 2.0)
        self.assertEqual(round(logarithm(32, 2), 5), 5.0)

    def test_log_invalid_base(self):
        self.assertEqual(logarithm(2, 1), "base must be positive and not equal to 1")
        self.assertEqual(logarithm(2, -1), "base must be positive and not equal to 1")

if __name__ == '__main__':
    unittest.main()