
import unittest
from poker import *

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

    def testEqualFail_NotSameClass(self):
        c1 = CardValue('A')
        try:
            self.assertEquals(c1 == 'A')
            self.assertTrue(False)
        except ValueError:
            pass

    def testNotEqual(self):
        c1 = CardValue('3')
        c2 = CardValue('4')
        self.assertNotEquals(c1,c2)
        
    def testNotEqualFail_NotSameClass(self):
        c1 = CardValue('A')
        try:
            self.assertTrue(c1 != 'A')
            self.assertTrue(False)
        except ValueError:
            pass

    def testGreater(self):
        c1 = CardValue('A')
        c2 = CardValue('K')
        self.assertTrue(c1 > c2)
    
    def testSmaller(self):
        c1 = CardValue('2')
        c2 = CardValue('J')
        self.assertTrue( c1 < c2)