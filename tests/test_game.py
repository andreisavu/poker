
import unittest
from poker import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.white_wins = [
            (['TS', 'JS', 'QS', 'KS', 'AS'], 'White'),
            (['7D', '8D', '9D', 'TD', 'JD'], 'Black')
        ]
        self.tie = [
            (['3D', '4H', '5D', 'TS', 'TC'], 'White'),
            (['2D', '6H', '7D', 'TD', 'TH'], 'Black')
        ]

    def createGame(self, cfg):
        g = Game()
        for hand, name in cfg:
            g.add_hand(Hand(hand,name))
        return g

    def getWinner(self, cfg):
        g = self.createGame(cfg)
        return g.get_winner()

    def testGetWinner(self):
        h = self.getWinner(self.white_wins)
        self.assertEquals(h.name, 'White')
        
    def testGetWinner_Tie(self):
        h = self.getWinner(self.tie)
        self.assertEquals(h, None)

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
        
    
 
