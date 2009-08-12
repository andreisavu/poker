
class FourOfAKindChecker(object):
    
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

