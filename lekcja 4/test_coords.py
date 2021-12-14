import unittest
from coords import count_distance
from math import sqrt

class TestCoords(unittest.TestCase):
    def test_count_distance(self):
        self.assertEqual(count_distance(((1, 5), (5, 2))), 5)
        self.assertEqual(count_distance(((1, 6), (5, 2))), sqrt(32))
        self.assertEqual(count_distance(((0, 0), (1, 1))), sqrt(2))
        self.assertEqual(count_distance(((sqrt(2), -sqrt(2)), (0, 0))), 2)
        self.assertEqual(count_distance(((-1, 5), (5, 2))), sqrt(45))
        self.assertEqual(count_distance(((-2, -3), (2, 2))), sqrt(41))
        self.assertEqual(count_distance(((2, -5), (1, 1))), sqrt(37))

if __name__ == "__main__":
    unittest.main()
