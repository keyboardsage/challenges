#!/usr/bin/python

import sys

fo = open (sys.argv[1], "r")

for line in fo:
    nmList = map(int,line.strip().split(','))
    timesDivisible = nmList[0]/nmList[1]
    print nmList[0] - (nmList[1] * timesDivisible)
