from unittest import TestCase
from Obliczenia_35 import Obliczenia

class TestObliczenia(TestCase):
    def testSilnia(self):
        obiekt = Obliczenia()
        self.assertEquals(obiekt.silnia(5), 120)
        self.assertEquals(obiekt.silnia(7), 5040)

    def test_silnia(self):
        self.fail()
