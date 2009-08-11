
class Game(object):
    
    def __init__(self):
        self.hands = []
        
    def add_hand(self, hand):
        for h in self.hands:
            if h.contains_any(hand):
                raise ValueError('Duplicate card not allowed')
        self.hands.append(hand)
    
    def get_winner(self):
        """ Find the winning hand. Return None if the game is tie. """
        if len(self.hands) == 0:
            raise Exception('This game has no players')
        if len(self.hands) == 1:
            return self.hands[0]
        
        self.hands.sort(reverse=True)
        if self.hands[0] == self.hands[1]:
            return None
        return self.hands[0]
        
