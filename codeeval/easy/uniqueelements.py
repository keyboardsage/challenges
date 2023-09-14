#!/usr/bin/env python

import sys
from sets import Set

for line in open(str(sys.argv[1]), "r"):
    theSetSortedAsList = map(str,sorted(list(Set(map(int,line.strip().split(','))))))
    print str(",").join(theSetSortedAsList)
