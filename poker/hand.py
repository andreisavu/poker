
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
            self.cards.append(Card(card))

    def get_card(self, n):
        return self.cards[n-1]

