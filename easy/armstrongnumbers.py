#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    n = line.strip()
    e = len(n)
    c = 0
    for i in map(int,list(n)):
        c += i**e
    print "True" if c == int(n) else "False"
