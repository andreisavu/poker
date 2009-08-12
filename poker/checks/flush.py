
class FlushChecker(object):
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

