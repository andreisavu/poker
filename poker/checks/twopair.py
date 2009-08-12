
class TwoPairChecker(object):

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

