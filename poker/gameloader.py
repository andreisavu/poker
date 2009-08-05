
from hand import Hand
from game import Game

class GameLoader:
    """ 
    Load game configurations from file
    """
    
    @staticmethod
    def from_file(file, names):
        """ Create a new loader from a file """
        f = open(file)
        data = []
        for l in f.xreadlines():
            parts = filter(None, l.strip("\n").upper().split(' '))
            data.append(parts)
        return GameLoader(data, names)
        
    def __init__(self, data, names):
        self.data = data
        self.current = 0
        self.names = names
        
    def has_games(self):
        return self.current < len(self.data)
        
    def next(self):
        if not self.has_games():
            raise StopIteration('No more games available')
        current = self.data[self.current]
        self.current += 1
        
        if len(current) != len(self.names) * 5:
            raise ValueError('Invalid game configuration')
        g = Game()
        offset = 0
        for name in self.names:
            h = Hand(current[offset:offset+5], name)
            g.add_hand(h)
            offset += 5
        return g
    
    def __iter__(self):
        return self
    