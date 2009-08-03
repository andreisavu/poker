
from card import *

class Hand:
    """
    A full poker hand

    It contains 5 cards. The order is not important.
    """
    
    MAX_SIZE = 5
    
    name = property(lambda self:self._name)
    cards = property(lambda self:self._cards[:])

    def __init__(self, cards, name=''):
        if len(cards) != Hand.MAX_SIZE:
            raise ValueError("A hand should contain %d cards" % Hand.MAX_SIZE)

        self._cards = []
        for card in cards:
            c = Card(card)
            if c in self._cards:
                raise ValueError('Duplicate card in one hand')
            self._cards.append(c)
        self._name = name

    def contains_any(self, hand):
        for card in hand.cards:
            if card in self.cards:
                return True
        return False

    def get_highest_card(self):
        return sorted(self.cards)[-1]

    

