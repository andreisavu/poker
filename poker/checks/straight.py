
from poker.cardvalue import CardValue

class StraightChecker(object):
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

    def explain(self):
        return "Straight"
 
    def offset(self):
        return self._offset

