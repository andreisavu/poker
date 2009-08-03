
from card import *

class Hand:
    """
    A full poker hand

    It contains 5 cards. The order is not important.
    """
    
    MAX_SIZE = 5
    
    name = property(lambda self:self._name)
    cards = property(lambda self:self._cards[:])
    score = property(lambda self:self.get_score())

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
            if card in self.cards:
                return True
        return False

    def get_highest_card(self):
        return sorted(self.cards)[-1]

    def get_score(self):
        if self._score is None:
            self._score = self._compute_score()
        return self._score

    def _compute_score(self):
        return 0

