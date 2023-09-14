#!/usr/bin/python

import sys

for line in open(sys.argv[1], "r"):
    d = map(int, list(line.rstrip().replace(' ', '')))[::2]
    nd = map(int, list(line.rstrip().replace(' ', '')))[1::2]
    print "Real" if sum([2*i for i in d] + nd) % 10.0 == 0 else "Fake"
