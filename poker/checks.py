
from cardvalue import CardValue
from cardcolor import CardColor
from hand import Hand

class _HandChecker(object):
    pass

class RoyalFlushChecker(_HandChecker):

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

class StraightFlushChecker(_HandChecker):
    
    def __init__(self):
        self._offset = 0

    def match(self, hand):
        if not hand.all_same_color():
            return False
        c = hand.get_smallest_card()
        for x in range(1, Hand.MAX_SIZE):
            c = c.next_by_value()
            if c not in hand.cards:
                return False
        self._offset = hand.get_highest_card().value.score
        return True
     
    def offset(self):
        return self._offset

class FourOfAKindChecker(_HandChecker):
    
    def match(self, hand):
        return False

    def offset(self):
        return 0

def match(hand):
    checks = [
        RoyalFlushChecker(),
        StraightFlushChecker(),
        FourOfAKindChecker()
    ]
    count = 0
    for check in checks:
        if check.match(hand):
            return check, len(checks)-count
        count += 1
    return None, None

