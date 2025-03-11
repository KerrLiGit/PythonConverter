import unittest
from prac3.converters.Weight import Weight


class TestWeight(unittest.TestCase):
    def test_ton_to_english_ton(self):
        self.assertEqual(41/1.016, Weight.ton_to_english_ton(self, 41))

    def test_ton_to_american_ton(self):
        self.assertEqual(47*1.102, Weight.ton_to_american_ton(self, 47))

    def test_kilogram_to_lb(self):
        self.assertEqual(4.05*2.205, Weight.kilogram_to_lb(self, 4.05))

    def test_kilogram_to_ounce(self):
        self.assertEqual(23*35.274, Weight.kilogram_to_ounce(self, 23))


if __name__ == '__main__':
    unittest.main()
