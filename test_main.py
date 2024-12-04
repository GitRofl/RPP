import unittest
from main import calculate


class TestCalculate(unittest.TestCase):

    
    def test_positive_discriminant(self):
        self.assertEqual(calculate(1, 5, 6), 1)

    
    def test_zero_discriminant(self):
        self.assertEqual(calculate(1, 2, 1), 0)

    
    def test_negative_discriminant(self):
        self.assertEqual(calculate(1, 2, 3), -8)


if __name__ == '__main__':
    unittest.main()
