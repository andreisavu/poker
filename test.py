
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
        
        

if __name__ == '__main__':
    unittest.main()

