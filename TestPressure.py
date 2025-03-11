"""Файл класса TestPressure."""


import unittest
from prac3.converters.Pressure import Pressure


class TestPressure(unittest.TestCase):
    """Класс тестирования, содержащий методы тестирования класса Pressure."""

    def test_bar_to_atmosphere(self):
        """Метод тестирует работу метода bar_to_atmosphere класса Pressure.

        :return: результат тестирования.
        """
        self.assertEqual(4.2/1.013, Pressure.bar_to_atmosphere(self, 4.2))

    def test_bar_to_pascal(self):
        """Метод тестирует работу метода bar_to_pascal класса Pressure.

        :return: результат тестирования.
        """
        self.assertEqual(2.14*100000, Pressure.bar_to_pascal(self, 2.14))

    def test_atmosphere_to_torr(self):
        """Метод тестирует работу метода atmosphere_to_torr класса Pressure.

        :return: результат тестирования.
        """
        self.assertEqual(51*760, Pressure.atmosphere_to_torr(self, 51))


if __name__ == '__main__':
    unittest.main()
