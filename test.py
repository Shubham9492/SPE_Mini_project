#!/usr/bin/python3
import unittest
from cal import square_root, factorial, natural_logarithm, power_function

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertAlmostEqual(square_root(169), 13)
        self.assertAlmostEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(625), 25)

    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(5), 120)

    def test_natural_logarithm(self):
        self.assertAlmostEqual(natural_logarithm(1), 0)
        self.assertAlmostEqual(natural_logarithm(2.718281828459045), 1)  # ln(e) = 1

    def test_power_function(self):
        self.assertAlmostEqual(power_function(3, 3), 27)
        self.assertAlmostEqual(power_function(3, 0), 1)
        self.assertAlmostEqual(power_function(10, -2), 0.01)

if __name__ == '__main__':
    unittest.main()
