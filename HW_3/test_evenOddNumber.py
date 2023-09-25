import unittest
from evenOddNumber import evenOddNumber


class TestEvenOddNumber(unittest.TestCase):
    def test_evenNumber(self):
        self.assertEqual(evenOddNumber(4), True)

    def test_oddNumber(self):
        self.assertEqual(evenOddNumber(3), False)

    def test_zero(self):
        self.assertEqual(evenOddNumber(0), True)

    def test_negativeNumber(self):
        self.assertEqual(evenOddNumber(-1), False)
        self.assertEqual(evenOddNumber(-4), True)
