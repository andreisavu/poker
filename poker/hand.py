
from card import *

class Hand:
    """
    A full poker hand

    It cotains 5 cards. The order is not important.
    """
    
    MAX_SIZE = 5

    def __init__(self, cards):
        if len(cards) != Hand.MAX_SIZE:
            raise ValueError("A hand should contain %d cards" % Hand.MAX_SIZE)

        self.cards = []
        for card in cards:
            c = Card(card)
            if c in self.cards:
                raise ValueError('Duplicate card in one hand')
            self.cards.append(c)

    def get_card(self, n):
        return self.cards[n-1]

