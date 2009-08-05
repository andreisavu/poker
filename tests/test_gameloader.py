
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