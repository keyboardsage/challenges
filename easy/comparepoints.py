#!/usr/bin/python

import sys

for line in open (sys.argv[1], "r"):
    (x1, y1, x2, y2) = tuple(map(int,line.strip().split(' ')))
    if x1 == x2 and y1 == y2:
        print "here"
    else:
        eastWest = ''
        northSouth = ''
        if x1 != x2:
            eastWest = 'W' if x1 > x2 else 'E'
        
        if y1 != y2:
            northSouth = 'S' if y1 > y2 else 'N'
        
        print northSouth + eastWest
