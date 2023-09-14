#!/usr/bin/env python

import sys

fo = open(str(sys.argv[1]), "r")
numberLinesWanted = int(fo.readline().rstrip())
gradualIncrease = map(str.strip, sorted(fo.readlines(), key = len))
count = 0
for line in reversed(gradualIncrease):
    if count < numberLinesWanted:
        count += 1
        print line
