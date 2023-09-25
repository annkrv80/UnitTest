import unittest
from numberInInterval import numberInInterval


class TestNumberInInterval(unittest.TestCase):
    def test_lowerLimitInterval(self):
        self.assertEqual(numberInInterval(24), False)
        self.assertEqual(numberInInterval(25), True)

    def test_numberInsideInterval(self):
        self.assertEqual(numberInInterval(55), True)

    def test_upperLimitInterval(self):
        self.assertEqual(numberInInterval(100), True)
        self.assertEqual(numberInInterval(101), False)
