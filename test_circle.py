import unittest
import math

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    """Набор unit-тестов для функций расчёта круга из модуля circle.py."""

    # -------- Тесты для area(r) --------

    def test_area_positive_int(self):
        """Площадь круга с положительным целым радиусом."""
        r = 5
        expected = math.pi * r * r
        self.assertAlmostEqual(area(r), expected, places=7)

    def test_area_zero_radius(self):
        """Площадь круга с нулевым радиусом должна быть равна 0."""
        self.assertEqual(area(0), 0.0)

    def test_area_float_radius(self):
        """Площадь круга с дробным радиусом."""
        r = 2.5
        expected = math.pi * r * r
        self.assertAlmostEqual(area(r), expected, places=7)

    def test_area_negative_radius_raises(self):
        """При отрицательном радиусе должна выбрасываться ошибка ValueError."""
        with self.assertRaises(ValueError):
            area(-1)

    # -------- Тесты для perimeter(r) --------

    def test_perimeter_positive_int(self):
        """Периметр круга (длина окружности) с положительным радиусом."""
        r = 10
        expected = 2 * math.pi * r
        self.assertAlmostEqual(perimeter(r), expected, places=7)

    def test_perimeter_zero_radius(self):
        """Периметр окружности с нулевым радиусом равен 0."""
        self.assertEqual(perimeter(0), 0.0)

    def test_perimeter_large_radius(self):
        """Периметр для очень большого радиуса (проверка работы с большими числами)."""
        r = 1_000_000
        expected = 2 * math.pi * r
        self.assertAlmostEqual(perimeter(r), expected, places=7)

    def test_perimeter_negative_radius_raises(self):
        """При отрицательном радиусе должна выбрасываться ошибка ValueError."""
        with self.assertRaises(ValueError):
            perimeter(-3)


if __name__ == "__main__":
    unittest.main()