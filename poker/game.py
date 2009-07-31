
class Game:
    
    def __init__(self):
        self.hands = []
        
    def add_hand(self, hand):
        for h in self.hands:
            if h.contains_any(hand):
                raise ValueError('Duplicate card not allowed')
        self.hands.append(hand)
    
