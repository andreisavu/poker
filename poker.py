
class Card:
    """
    Card handling class

    Parse and compare poker cards

    Usage:

    Create a card:
        >>> c = Card('2D')

    Display string representation
        >>> c
        '2D'
    """
   
    value = property(lambda self: self._value)
    color = property(lambda self: self._color)

    def __init__(self, card=None):
        self.card = card
        if card:
            self.parse(card)
        else:
            self._value = 0
            self._color = ''

    def parse(self, card):
        """
        Parse a card configuration

        If the parsing fails the function will raise ValueError
        """
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

