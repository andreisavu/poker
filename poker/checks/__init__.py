
import sys
import os

_base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.append(_base)

from royalflush import *
from straightflush import *
from fourofakind import *
from fullhouse import *
from flush import *
from straight import *
from threeofakind import *
from twopair import *
from pair import *
from default import *

def match(hand):
    checks = [
        RoyalFlushChecker(),
        StraightFlushChecker(),
        FourOfAKindChecker(),
        FullHouseChecker(),
        FlushChecker(),
        StraightFlushChecker(),
        ThreeOfAKindChecker(),
        TwoPairChecker(),
        PairChecker(),
        DefaultChecker()
    ]
    count = 0
    for check in checks:
        if check.match(hand):
            return check, len(checks)-count
        count += 1
    
    return None, None

