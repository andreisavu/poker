
class StraightFlushChecker():
    
    def __init__(self):
        self._max_card = None

    def match(self, hand):
        if not hand.all_same_color():
            return False
        if not hand.in_sequence():
            return False
        self._max_card = hand.get_highest_card()
        return True

    def explain(self):
        return "Straight Flush. Max card: %s" % str(self._max_card)
     
    def offset(self):
        return self._max_card.value.score

