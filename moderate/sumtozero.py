#!/usr/bin/python

import sys
import itertools

for line in open (sys.argv[1],'r'):
    l = map(int,line.rstrip().split(','))
    count = 0
    for i in itertools.combinations(l,4):
        if sum(i) == 0:
            count += 1
    print count
