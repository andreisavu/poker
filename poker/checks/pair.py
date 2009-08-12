
class PairChecker(object):

    def __init__(self):
        self._offset = 0

    def match(self, hand): 
        counts = hand.counts_by_value()
        for k, v in counts.items():
            if v == 2:
                self._offset = k
                return True
        return False

    def explain(self):
        return "Pair"

    def offset(self):
        return self._offset


