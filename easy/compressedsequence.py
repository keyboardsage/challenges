#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    theList = line.strip().split(' ')
    lastKnown = ""
    count = 0
    output = []
    for e in theList:
        if e != lastKnown:
            if count != 0:
                output.append(str(count) + ' ' + lastKnown)
            
            lastKnown = e
            count = 1
        else:
            count += 1
    output.append(str(count) + ' ' + lastKnown) 
    print ' '.join(output)
