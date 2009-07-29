
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

    def testEqual(self):
        c1 = CardColor('S')
        c2 = CardColor('S')
        self.assertEquals(c1, c2)

    def testEqualFail_NotSameClass(self):
        c1 = CardColor('S')
        try:
            self.assertEquals(c1, 'S')
            self.assertTrue(False)
        except ValueError:
            pass

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
        