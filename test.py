
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

    def testEqual(self):
        c1 = CardColor('S')
        c2 = CardColor('S')
        self.assertEquals(c1, c2)

    def testNotEqual(self):
        c1 = CardColor('S')
        c2 = CardColor('D')
        self.assertNotEquals(c1,c2)

    def testOrderingFail(self):
        c1 = CardColor('S')
        c2 = CardColor('D')
        thrown = False
        try:
            b = c1 < c2
        except Exception, e:
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

    def testEquals(self):
        c1 = CardValue('A')
        c2 = CardValue('A')
        self.assertEquals(c1,c2)

    def testNotEqual(self):
        c1 = CardValue('3')
        c2 = CardValue('4')
        self.assertNotEquals(c1,c2)

    def testGreater(self):
        c1 = CardValue('A')
        c2 = CardValue('K')
        self.assertTrue(c1 > c2)
    
    def testSmaller(self):
        c1 = CardValue('2')
        c2 = CardValue('J')
        self.assertTrue( c1 < c2)

if __name__ == '__main__':
    unittest.main()

