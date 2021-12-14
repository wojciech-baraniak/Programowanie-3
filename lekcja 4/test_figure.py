import unittest
from figure import Triangle
from math import sqrt

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.t = Triangle(3,4,5)
        self.t1 = Triangle(6, 6, 6)

    def test_length(self):
        self.assertEqual(self.t.length, 12)
        self.assertEqual(self.t1.length, 18)

    def test_area(self):
        self.assertEqual(self.t.area, 6)
        self.assertAlmostEqual(self.t1.area, 36/4*sqrt(3))

    def test_assert_0(self):
        self.assertRaises(ValueError, Triangle, 0, 3, 3)

    def test_assert_side(self):
        self.assertRaises(ValueError, Triangle, 1, 2, 3)

if __name__ == "__main__":
    unittest.main()
