#!/usr/bin/python

import sys

for line in open (sys.argv[1], "r"):
    (a, b) = (line.strip().split(','))
    print 1 if a[-len(b):] == b else 0
