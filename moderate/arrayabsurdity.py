#!/usr/bin/python

import sys
import itertools

for line in open (sys.argv[1], "r"):
    l = (line.strip().split(';')[1]).split(',')
    for i in itertools.combinations(l,2):
        if i[0] == i[1]:
            print i[0]
            break
