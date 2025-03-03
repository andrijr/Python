from unittest import TestCase
from Main import Obliczenia

class TestObliczenia(TestCase):
    def testSilnia(self):
        obiekt = Obliczenia()
        self.assertEqual(obiekt.silnia(5),120)
        self.assertEqual(obiekt.silnia(7),5040)

    def testSilnia2(self):
        obiekt = Obliczenia()
        self.greater = self.assertGreater(obiekt.silnia(100), 100000000)
