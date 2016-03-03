#!/usr/bin/python

import sys

for line in open (sys.argv[1],'r'):
    w = list(line.rstrip())
    for l in w:
        if w.count(l) == 1:
            print l
            break
