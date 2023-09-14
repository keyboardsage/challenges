#!/usr/bin/env python

import sys
import math

for line in open(str(sys.argv[1]), "r"):
    theCoordinates = map(int, line.strip().translate(None, "(,)").split(' '))
    print int(math.sqrt((theCoordinates[2] - theCoordinates[0])**2 + (theCoordinates[3] - theCoordinates[1])**2))
