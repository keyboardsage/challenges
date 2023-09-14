#!/usr/bin/python

import sys

for line in open(sys.argv[1], "r"):
    d = map(int, line.rstrip().replace(',','').split(' ')[1::2])
    print ((d[0]*3 + d[1]*4 + d[2]*5) * d[3]) / sum(d[0:3])
