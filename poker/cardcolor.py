
class CardColor:

    color = property(lambda self:self._color)

    def __init__(self, color):
        self.parse(color)

    def parse(self, color):
        allowed_colors = ['S', 'D', 'H', 'C']
        if color not in allowed_colors:
            raise ValueError("Unknown color: %s" % color)
        self._color = color

    def next(self):
        seq = ['S', 'D', 'H', 'C', 'S']
        for i in range(0, len(seq)):
            if seq[i] == self._color:
                break
        return CardColor(seq[i+1])

    def __eq__(self, card):
        if not isinstance(card,CardColor):
            raise ValueError('Trying to compare incompatible types')
        return self._color == card.color

    def __ne__(self, card):
        return not (self == card)

    def __lt__(self, card):
        raise Exception('Operator not applicable')

    def __le__(self, card):
        return (self < card) or (self == card)

    def __gt__(self, card):
        return not (self <= card)

    def __ge__(self, card):
        return not (self < card)

    def __str__(self):
        colors_map = {
            'S' : 'Spades', 
            'D' : 'Diamonds',
            'H' : 'Hearts',
            'C' : 'Clubs'
        }
        return colors_map[self._color]     



