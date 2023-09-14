#!/usr/bin/python

import sys

for line in open (sys.argv[1], "r"):
    # ignore empty lines
    t = line.rstrip()
    if t == "":
        continue

    # rightmost character
    l, c = t.split(',')
    print l.rfind(c)
