#!/usr/bin/env python

import sys
import math

for line in open(sys.argv[1],'r'):
    houses = sorted(map(int, line.strip().split(' '))[1:])
    l = houses[0]
    h = houses[len(houses)-1] + 1
    #tally = {}
    tally = sys.maxint

    for i in range(l,h):
        temp = sum([abs(i-x) for x in houses])
        if temp < tally:
            tally = temp
    print tally
