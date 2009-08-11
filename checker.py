#! /usr/bin/env python

import sys
from poker import *

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print 'Reading from file %s ...' % sys.argv[1]
        input = open(sys.argv[1])
    else:
        print 'Reading from stdin ...'
        input = sys.stdin

    games = GameLoader.from_handle(input, ['White', 'Black'])
    for g in games:
        h = g.get_winner()
        if h:
            print "%s wins." % h.name
        else:
            print 'Tie.'
 
