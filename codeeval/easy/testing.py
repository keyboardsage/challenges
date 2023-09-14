#!/usr/bin/python

import sys
import re

for line in open(sys.argv[1], "r"):
    dev, des = line.rstrip().split("|")
    dev = dev.rstrip()
    des = des.lstrip()
    accum = 0
    for compare in zip(dev,des):
        if compare[0] != compare[1]:
            accum += 1

    output = ""
    if accum == 0:
        output = "Done"
    elif accum < 3:
        output = "Low"
    elif accum < 5:
        output = "Medium"
    elif accum < 7:
        output = "High"
    elif accum > 6:
        output = "Critical"

    print output
