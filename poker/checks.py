
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
        if not hand.in_sequence():
            return False
        self._offset = hand.get_highest_card().value.score
        return True
     
    def offset(self):
        return self._offset

class FourOfAKindChecker(_HandChecker):
    
    def __init__(self):
        self._offset = 0

    def match(self, hand):
        counts = hand.counts_by_value()
        if len(counts) != 2:
            return False
        for k,v in counts.items():
            if v == 4:
                self._offset = k
                return True
        return False

    def offset(self):
        return self._offset

class FullHouseChecker(_HandChecker):

    def __init__(self):
        self._offset = 0

    def match(self, hand):
        counts = hand.counts_by_value()
        if len(counts) != 2:
            return False
        d = counts.items()
        if d[0][1] != 2 and d[0][1] != 3:
            return False

        if d[0][1] == 2:
            self._offset = d[0][0]
        else:
            self._offset = d[1][0]
        return True

    def offset(self):
        return self._offset

class FlushChecker(_HandChecker):
    def __init__(self):
        self._offset = 0

    def match(self, hand):
        if not hand.all_same_color():
            return False
        if hand.in_sequence():
            return False
        self._offset = hand.get_highest_card().value.score
        return True 

    def offset(self):
        return self._offset

class StraightChecker(_HandChecker):
    def __init__(self):
        self._offset = 0

    def match(self, hand):
        if hand.all_same_color():
            return False
        if not hand.in_sequence():
            return False 
        for value in ['2', '3', 'Q', 'K', 'A']:
            if hand.contains_value(CardValue(value)):
                return False
        self._offset = hand.get_highest_card().value.score
        return True
 
    def offset(self):
        return self._offset

class ThreeOfAKindChecker(_HandChecker):

    def __init__(self):
        self._offset = 0

    def match(self, hand): 
        counts = hand.counts_by_value()
        for k, v in counts.items():
            if v ==  3:
                self._offset = k
                return True
        return False

    def offset(self): 
        return self._offset

class TwoPairChecker(_HandChecker):

    def __init__(self):
        self._offset = 0

    def match(self, hand):
        counts = hand.counts_by_value()
        count, max = 0, 0
        for k, v in counts.items():
            if v == 2:
                count += 1
                if max < k:
                    max = k
        if count == 2:
            self._offset = max
            return True
        return False

    def offset(self):
        return self._offset

class PairChecker(_HandChecker):
    def match(self, hand): return False
    def offset(self): return 0

class DefaultChecker(_HandChecker):

    def __init__(self):
        self._offset = 0

    def match(self, hand):
        cards = sorted(hand.cards, reverse=True)
        self._offset = cards[0].value.score * 10
        self._offset += cards[1].value.score
        return True

    def offset(self):
        return self._offset

def match(hand):
    checks = [
        RoyalFlushChecker(),
        StraightFlushChecker(),
        FourOfAKindChecker(),
        FullHouseChecker(),
        FlushChecker(),
        StraightFlushChecker(),
        ThreeOfAKindChecker(),
        TwoPairChecker(),
        PairChecker(),
        DefaultChecker()
    ]
    count = 0
    for check in checks:
        if check.match(hand):
            return check, len(checks)-count
        count += 1
    
    return None, None

