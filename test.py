
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

    def testParseFail_InvalidCard(self):
        thrown = False
        cards = ['2H', '3D', '5S', '9S', 'KX']
        try:
            h = Hand(cards)
        except ValueError, e:
            thrown = True
        self.assertTrue(thrown)

class TestCardColor(unittest.TestCase):

    def testParse(self):
        data = {
            'S' : 'Spades',
            'D' : 'Diamonds',
            'H' : 'Hearts',
            'C' : 'Clubs'
        }
        for k in data.keys(): 
            c = CardColor(k)
            self.assertEquals(str(c), data[k])

    def testParseFail(self):
        thrown = False
        try:
            c = CardColor('A')
        except ValueError:
            thrown = True
        self.assertTrue(thrown)
        
class TestCardValue(unittest.TestCase):

    def testParse(self):
        for x in range(2,10):
            c = CardValue(str(x))
            self.assertEquals(c.value, str(c)) 
        data = {
            'T' : 'Ten',
            'J' : 'Jack',
            'Q' : 'Queen',
            'K' : 'King',
            'A' : 'Ace'}
        for k in data.keys():
            c = CardValue(str(k))
            self.assertEquals(str(c), str(c))

    def testParseFail(self):
        thrown = False
        try:
            c = CardValue('X')
        except ValueError:
            thrown = True
        self.assertTrue(thrown)

if __name__ == '__main__':
    unittest.main()

