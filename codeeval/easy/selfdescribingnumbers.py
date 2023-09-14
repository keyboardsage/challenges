#!/usr/bin/python

import sys

fo = open (sys.argv[1], "r")

for line in fo:
    startingCounts = map(int,list(line.strip()))
    endingCounts = []
    for digitType in range(10): # for each digit type...
        endingCounts.append(sum([1 for x in startingCounts if x == digitType])) # count times it shows up in number
    # if my count matches your count it is self-describing
    print (1 if (startingCounts+[0]*(len(endingCounts)-len(startingCounts)) == endingCounts) else 0)
