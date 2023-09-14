#!/usr/bin/env python

import sys

for line in open(str(sys.argv[1]), "r"):
    for x in sorted(map(float, line.strip().split(' '))):
        print "%.3f" % x,
    print
