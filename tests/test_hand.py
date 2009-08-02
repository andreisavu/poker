
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

    def testContainsAny(self):
        h1 = Hand(['2H', '3D', '5S', '9C', 'KD'])
        h2 = Hand(['2D', '5D', '9C', 'AC', 'KS'])
        self.assertTrue(h1.contains_any(h2))

    def testDoesNotContainAny(self):
        h1 = Hand(['2H', '3D', '5S', '9C', 'KD'])
        h2 = Hand(['2D', '5D', '6C', 'AC', 'KS'])
        self.assertFalse(h1.contains_any(h2))

    def testCreateWithName(self):
        h1 = Hand(['2H', '3D', '5S', '9C', 'KD'], 'White')
        self.assertEquals(h1.name, 'White')
        
    def testGetHighestCard(self):
        c = Card('KD')
        h = Hand(['2H', '3D', '5S', '9C', str(c)])
        self.assertEquals(c, h.get_highest_card())
