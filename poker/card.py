
class CardColor:

    def __init__(self, color):
        self.parse(color)

    def parse(self, color):
        allowed_colors = ['S', 'D', 'H', 'C']
        if color not in allowed_colors:
            raise ValueError('Unknown color')
        self._color = color

    def __str__(self):
        colors_map = {
            'S' : 'Spades', 
            'D' : 'Diamonds',
            'H' : 'Hearts',
            'C' : 'Clubs'
        }
        return colors_map[self._color]     


class CardValue:

    _values_score_map = {
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'T' : 10,
        'J' : 12,
        'Q' : 13,
        'K' : 14,
        'A' : 15
    }

    value = property(lambda self: self._value, lambda self,v:self.parse(v))
    score = property(lambda self: self._score)

    def __init__(self, value):
        self.parse(value)

    def parse(self, value):
        if value not in CardValue._values_score_map.keys():
            raise ValueError('Unknown card value')
        self._value = value
        self._score = self._values_score_map[value] 

    def __str__(self):
        if self._value in [str(x) for x in range(2,10)]:
            return self._value
        else:
            _str_map = {'T':'Ten', 'J':'Jack', 'Q':'Queen', 'K':'King', 'A':'Ace'}
            return _str_map[self._value]

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
        pass

    def __str__(self):
        return self._card

