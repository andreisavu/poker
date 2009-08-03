
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
        
    def testNextByValue(self):
        self.assertEquals(Card('2S').next_by_value(), Card('3S'))
        self.assertEquals(Card('AS').next_by_value(), Card('2S'))
        
    def testNextByColor(self):
        self.assertEquals(Card('2S').next_by_color(), Card('2D'))
        
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
        

