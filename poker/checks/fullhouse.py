
class FullHouseChecker(object):

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

    def explain(self):
        return "Full house"

    def offset(self):
        return self._offset

