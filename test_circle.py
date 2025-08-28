import unittest
import math
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_set_radius_return(self):
        c = Circle(8)
        self.assertEqual(c.setRadius(7), True)

    def test_set_radius_positive(self):
        c = Circle(8)
        c.setRadius(16)
        self.assertEqual(c.getRadius(), 16)

    def test_set_radius_negative(self):
        c = Circle(8)
        self.assertEqual(c.setRadius(-7), False)

    def test_set_radius_zero(self):
        c = Circle(8)
        self.assertEqual(c.setRadius(0), True)

    def test_get_area_positive(self):
        c = Circle(8)
        self.assertEqual(c.getArea(), math.pi * 8 * 8)

    def test_get_area_two(self):
        c = Circle(2)
        self.assertEqual(c.getArea(), 0)

    def test_get_circumference(self):
        c = Circle(7)
        self.assertEqual(c.getCircumference(), 2 * math.pi * 7)


if __name__ == "__main__":
    unittest.main()
