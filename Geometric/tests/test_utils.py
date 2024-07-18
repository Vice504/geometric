import unittest
from geometry.shapes import Circle, Triangle
from geometry.utils import get_area, is_right_triangle


class TestUtils(unittest.TestCase):

    def test_get_area_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(get_area(circle), 78.53981633974483)

    def test_get_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(get_area(triangle), 6.0)

    def test_is_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(is_right_triangle(triangle))

        triangle = Triangle(3, 3, 3)
        self.assertFalse(is_right_triangle(triangle))


if __name__ == '__main__':
    unittest.main()
