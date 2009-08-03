
from cardvalue import *
from cardcolor import *

class Card:
   
    value = property(lambda self: self._value)
    color = property(lambda self: self._color)

    def __init__(self, card=None):
        self._card = card
        if card:
            self.parse(card)
        else:
            self._value = self._color = None

    def parse(self, card):
        """
        Parse a card configuration

        If the parsing fails the function will raise ValueError
        """
        if len(card) != 2:
            raise ValueError('Unknown card format')
        self._value = CardValue(card[0])
        self._color = CardColor(card[1])

    def __eq__(self, card):
        return self.color == card.color and self.value == card.value
    
    def __ne__(self,card):
        return not (self == card)

    def __lt__(self, card):
        if not isinstance(card, Card):
            raise ValueError('Trying to compare incompatible types')
        return self._value < card.value

    def __le__(self, card):
        return (self < card) or (self == card)

    def __gt__(self, card):
        return not (self <= card)

    def __ge__(self, card):
        return not (self < card)

    def __str__(self):
        return self._card

