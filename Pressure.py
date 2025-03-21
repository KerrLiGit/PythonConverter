"""Файл класса Pressure."""


class Pressure:
    """Класс, содержащий методы - конверторы величин (давления)."""

    def bar_to_atmosphere(self, a):
        """Метод конвертирует значение в барах в значения в атмосферах.

        :param a: значение в барах.
        :type a: float
        :return: значение в атмосферах.
        """
        return a / 1.013

    def bar_to_pascal(self, a):
        """Метод конвертирует значение в барах в значения в паскалях.

        :param a: значение в барах.
        :type a: float
        :return: значение в паскалях.
        """
        return a * 100000

    def atmosphere_to_torr(self, a):
        """Метод конвертирует значение в атмосферах в значения в торрах.

        :param a: значение в атмосферах.
        :type a: float
        :return: значение в торрах.
        """
        return a * 760
