
class DefaultChecker(object):

    def __init__(self):
        self._offset = 0
        self._max_card = 0

    def match(self, hand):
        cards = sorted(hand.cards, reverse=True)
        self._max_card = cards[0]
        self._offset = cards[0].value.score * 20
        self._offset += cards[1].value.score
        return True

    def explain(self):
        return "Empty hand. Max card: %s" % str(self._max_card)

    def offset(self):
        return self._offset

