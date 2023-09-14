#!/usr/bin/python

import sys

for line in open (sys.argv[1], "r"):
    timeArrSorted = sorted(line.strip().split(' '), reverse=True)
    print ' '.join(map(str, timeArrSorted))
