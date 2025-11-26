import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    """Набор unit-тестов для функций квадрата из модуля square.py."""

    # -------- Тесты для area(a) --------

    def test_area_positive_int(self):
        """Площадь квадрата с положительной целой стороной."""
        self.assertEqual(area(4), 16)

    def test_area_one_side(self):
        """Площадь квадрата со стороной 1."""
        self.assertEqual(area(1), 1)

    def test_area_zero_side(self):
        """Площадь квадрата с нулевой стороной должна быть 0."""
        self.assertEqual(area(0), 0)

    def test_area_float_side(self):
        """Площадь квадрата с дробной стороной."""
        self.assertAlmostEqual(area(2.5), 6.25, places=7)


    # -------- Тесты для perimeter(a) --------

    def test_perimeter_positive_int(self):
        """Периметр квадрата с положительной стороной."""
        self.assertEqual(perimeter(4), 16)

    def test_perimeter_one_side(self):
        """Периметр квадрата со стороной 1."""
        self.assertEqual(perimeter(1), 4)

    def test_perimeter_zero_side(self):
        """Периметр квадрата с нулевой стороной должен быть 0."""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_float_side(self):
        """Периметр квадрата с дробной стороной."""
        self.assertAlmostEqual(perimeter(2.5), 10.0, places=7)



if __name__ == "__main__":
    unittest.main()