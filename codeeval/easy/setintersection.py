#!/usr/bin/env python

import sys
from sets import Set

for line in open(sys.argv[1], "r"):
    theSetsAsLists = line.rstrip().split(';')
    setA = Set(theSetsAsLists[0].split(','))
    setB = Set(theSetsAsLists[1].split(','))
    setA &= setB
    print ",".join(sorted(list(setA)))
