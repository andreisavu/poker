
import unittest
from poker import *
from poker.checks import *

class TestCheckers(unittest.TestCase):

    def setUp(self):
        self.royal_flush = Hand(['TS', 'JS', 'QS', 'KS', 'AS'])
        self.straight_flush = Hand(['7D', '8D', '9D', 'TD', 'JD'])
        self.four_of_a_kind = Hand(['6H', 'JS', 'JD', 'JH', 'JC'])
        self.full_house = Hand(['QH', 'QS', 'KD', 'KC', 'KH'])
        self.flush = Hand(['AC', '5C', '7C', '9C', 'JC'])
        self.straight = Hand(['8H', '9C', 'TC', 'JD', 'QS'])
        self.three_of_a_kind = Hand(['7H', 'TC', 'KH', 'KD', 'KS'])
        self.two_pair = Hand(['4H', 'JS', 'JH', 'QC', 'QD'])
        self.pair = Hand(['2D', '6H', '7D', 'TS', 'TC'])
        self.nothing = Hand(['4H', '6S', '8C', 'TD', 'QH']) 
     
    def testRoyalFlushMatch(self):
        check = RoyalFlushChecker()
        self.assertTrue(check.match(self.royal_flush))
        self.assertFalse(check.match(self.straight_flush))

    def testStraightFlushMatch(self):
        check = StraightFlushChecker()
        self.assertTrue(check.match(self.royal_flush))
        self.assertTrue(check.match(self.straight_flush))
        self.assertFalse(check.match(self.four_of_a_kind))

    def testFourOfAKind(self):
        check = FourOfAKindChecker()
        self.assertTrue(check.match(self.four_of_a_kind))
        self.assertFalse(check.match(self.straight_flush))

