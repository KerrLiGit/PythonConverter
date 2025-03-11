import unittest
from prac3.converters.Length import Length


class TestLength(unittest.TestCase):
    def test_meters_to_inch(self):
        self.assertEqual(1.4*39.37, Length.meters_to_inch(self, 1.4))

    def test_kilometers_to_mile(self):
        self.assertEqual(3/1.609, Length.kilometers_to_mile(self, 3))

    def test_meters_to_yard(self):
        self.assertEqual(7*1.094, Length.meters_to_yard(self, 7))

    def test_meters_to_foots(self):
        self.assertEqual(5*3.281, Length.meters_to_foots(self, 5))

    def test_kilometers_to_sea_mile(self):
        self.assertEqual(45/1.852, Length.kilometers_to_sea_mile(self, 45))


if __name__ == '__main__':
    unittest.main()
