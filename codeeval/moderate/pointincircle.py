#!/usr/bin/env python

import sys
import math

for line in open(sys.argv[1], "r"):
    dataLine = tuple(line.strip().translate(None, "(,);").split(' '))
    centerX = float(dataLine[1])
    centerY = float(dataLine[2])
    radius = float(dataLine[4])
    pointX = float(dataLine[6])
    pointY = float(dataLine[7])
    if math.sqrt((pointY - centerY)**2 + (pointX - centerX)**2) <= radius:
        print "true"
    else:
        print "false"
