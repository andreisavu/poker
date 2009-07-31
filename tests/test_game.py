
import unittest
from poker import *

class TestGame(unittest.TestCase):

    def testAddHand(self):
        valid_hands = [
            ['2H', '3D', '5S', '9C', 'KD'], 
            ['2D', '5D', '7C', 'AC', 'KS'] 
        ]
        
        g = Game()
        for hand_data in valid_hands:
            g.add_hand(Hand(hand_data))

    def testAddHandFail_DuplicateCard(self):
        valid_hands = [
            ['2H', '3D', '5S', '9C', 'KD'], 
            ['2D', '5D', '9C', 'AC', 'KS'] 
        ]

        g = Game()
        try:
            for hand_data in valid_hands:
                g.add_hand(Hand(hand_data))           
            self.assertTrue(False)
        except ValueError:
            pass

        
 
