
import unittest
import os

from poker import *

class TestGameLoader(unittest.TestCase):
    
    def setUp(self):
        self.fixtures = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures/')
        self.input = os.path.join(self.fixtures, 'input.txt')
        self.output = os.path.join(self.fixtures, 'output.txt')
        
    def testGameLoaderFromFile(self):
        games = GameLoader.from_file(self.input, ['White', 'Black'])
        for g in games:
            self.assertEquals(len(g.hands), 2)
            
    def testFullCycle(self):
        games = GameLoader.from_file(self.input, ['White', 'Black'])
        output = map(lambda s:s.strip("\n"), open(self.output).readlines())
        line = 0
        for g in games:
            h = g.get_winner()
            if h:
                self.assertEquals(output[line], "%s wins." % h.name)
            else:
                self.assertEquals(output[line], 'Tie.')
            line += 1