
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

    value = property(lambda self: self._value)
    score = property(lambda self: self._score)

    def __init__(self, value):
        self.parse(value)

    def parse(self, value):
        if value not in CardValue._values_score_map.keys():
            raise ValueError('Unknown card value')
        self._value = value
        self._score = self._values_score_map[value]
        
    def next(self):
        new_score = (self._score + 1) % 16
        if new_score < 2: new_score += 2
        keys = [k for k,v in self._values_score_map.items() if v == new_score]
        return CardValue(keys[0])

    def __eq__(self, card):
        if not isinstance(card, CardValue):
            raise ValueError('Trying to compare incompatible types')
        return self._score == card.score

    def __ne__(self, card):
        return not (self == card)

    def __lt__(self, card):
        if not isinstance(card, CardValue):
            raise ValueError('Trying to compare incompatible types')
        return self._score < card._score

    def __le__(self, card):
        return (self < card) or (self == card)

    def __gt__(self, card):
        return not (self <= card)

    def __ge__(self, card):
        return not (self < card)

    def __str__(self):
        if self._value in [str(x) for x in range(2,10)]:
            return self._value
        else:
            _str_map = {'T':'Ten', 'J':'Jack', 'Q':'Queen', 'K':'King', 'A':'Ace'}
            return _str_map[self._value]

