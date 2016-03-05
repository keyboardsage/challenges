#!/usr/bin/env python

import sys
import math
import itertools

for line in open(sys.argv[1], "r"):
    # prepare the list of coordinates
    l = line.translate(None, "()").rstrip().split(', ')
    l = [tuple(map(int, elem.split(','))) for elem in l]

    # find all combinations of coordinates
    c = list(itertools.combinations(l, 2))

    # get distances between coordinates by using the distance formula on all coordinate pairs
    d = [math.sqrt((twoPoints[1][1] - twoPoints[0][1])**2 + (twoPoints[1][0] - twoPoints[0][0])**2) for twoPoints in c]
    
    # check
    if len(set(d)) in [1, 2]:
    # 1) there should be only two unique values for distances (hypotenuse and legs)
    # 4 because of the legs, 2 because of the hypotenuse
    # 2) although sometimes they may all be the same number
        print "true"
    else:
        print "false"
