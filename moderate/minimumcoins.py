#!/usr/bin/python

import sys

for line in open(str(sys.argv[1]), "r"):
    target = int(line.rstrip())
    coinCount = 0
    for value in [5,3,1]:
        coinCount += target / value
        target = target % value
        if target == 0:
            break
    print coinCount
