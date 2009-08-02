
import unittest
from poker import *

class TestCard(unittest.TestCase):
    
    def testParse(self):
        c = Card('2D')
        self.assertEquals(str(c.value), '2')
        self.assertEquals(str(c.color), 'Diamonds')
        
    def testParseFail(self):
        thrown = False
        try:
            c = Card('2X')
        except ValueError, e:
            thrown = True
        self.assertTrue(thrown)
        
    def testEqual(self):
        c1 = Card('2D')
        c2 = Card('2D')
        self.assertTrue(c1 == c2)
        
    def testNotEqual(self):
        c1 = Card('2D')
        c2 = Card('3D')
        self.assertFalse(c1 == c2)
        
    def testGreater(self):
        c1 = Card('AD')
        c2 = Card('2S')
        self.assertTrue(c1 > c2)
        
    def testSmaller(self):
        c1 = Card('2D')
        c2 = Card('AD')
        self.assertTrue(c1 < c2)
        
    def testSameSuite(self):
        c1 = Card('2D')
        c2 = Card('AD')
        self.assertTrue(c1.same_suite(c2))
        self.assertFalse(c1.same_suite(Card('AS')))
    
    def testSameValue(self):
        c = Card('2D')
        self.assertTrue(c.same_value(Card('2S')))
        self.assertFalse(c.same_value(Card('3D')))

