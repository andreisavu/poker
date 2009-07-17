
import unittest
from poker import *

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

