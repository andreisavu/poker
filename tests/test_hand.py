
import unittest
from poker import *

class TestHand(unittest.TestCase):

    def testParse(self):
        h = Hand(['2H', '3D', '5S', '9C', 'KD'])

        self.assertEquals(str(h.get_card(3).value), '5')
        self.assertEquals(str(h.get_card(3).color), 'Spades')
        self.assertEquals(str(h.get_card(5).value), 'King')

    def testParseFail_NotEnoughCards(self):
        thrown = False
        cards = ['2H', '3D', '5S']
        try:
            h = Hand(cards)
        except ValueError, e:
            thrown = True
        self.assertTrue(thrown)

    def testParseFail_DuplicateCard(self):
        cards = ['2H', '3D', '5S', '2S', '2H']
        try:
            h = Hand(cards)
            self.assertTrue(False)
        except ValueError:
            pass

    def testParseFail_InvalidCard(self):
        thrown = False
        cards = ['2H', '3D', '5S', '9S', 'KX']
        try:
            h = Hand(cards)
        except ValueError, e:
            thrown = True
        self.assertTrue(thrown)