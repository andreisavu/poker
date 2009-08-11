
from card import *

class Hand(object):
    """
    A full poker hand

    It contains 5 cards. The order is not important.
    """
    
    MAX_SIZE = 5
    
    name = property(lambda self:self._name)
    cards = property(lambda self:self._cards[:])

    @staticmethod
    def from_string(str, name=''):
        """ Create a hand instance by parsing a string with card definitions """
        cards = filter(None, str.upper().split(' '))
        return Hand(cards, name)

    def __init__(self, cards, name=''):
        if len(cards) != Hand.MAX_SIZE:
            raise ValueError("A hand should contain %d cards" % Hand.MAX_SIZE)

        self._cards = []
        self._score = None
        self._name = name

        for card in cards:
            c = Card(card)
            if c in self._cards:
                raise ValueError('Duplicate card in one hand')
            self._cards.append(c)


    def contains_any(self, hand):
        for card in hand.cards:
            if card in self._cards:
                return True
        return False

    def get_highest_card(self):
        return sorted(self.cards)[-1]

    def get_smallest_card(self):
        return sorted(self.cards)[0]

    def get_score(self):
        if self._score is None:
            self._score = self._compute_score()
        return self._score

    def _compute_score(self):
        import checks
        check, level = checks.match(self)
        if check is None:
            return 0
        return 1000 * level + check.offset()

    def all_same_color(self):
        first = self.cards[0]
        for c in self.cards:
            if not first.color == c.color:
                return False
        return True

    def counts_by_value(self):
        counts = {}
        for card in self._cards:
            score = card.value.score
            if score in counts:
                counts[score] += 1
            else:
                counts[score] = 1
        return counts


    def __eq__(self, hand):
        if not isinstance(hand, Hand):
            raise ValueError('Trying to compare incompatible types')
        return self.get_score() == hand.get_score()

    def __ne__(self, hand):
        return not (self == hand)
    
    def __lt__(self, hand):
        if not isinstance(hand, Hand):
            raise ValueError('Truing to compare incompatible types')
        return self.get_score() < hand.get_score()
    
    def __le__(self, card):
        return (self < card) or (self == card)

    def __gt__(self, card):
        return not (self <= card)

    def __ge__(self, card):
        return not (self < card)

