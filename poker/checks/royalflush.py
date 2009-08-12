
from poker.cardvalue import CardValue

class RoyalFlushChecker(object):

    def match(self, hand):
        if not hand.get_highest_card().value == CardValue('A'):
            return False
        if not hand.get_smallest_card().value == CardValue('T'):
            return False
        if not hand.all_same_color():
            return False
        return True

    def offset(self):
        return 0

