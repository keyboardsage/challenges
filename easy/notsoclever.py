#!/usr/bin/python

import sys
import re

for line in open(sys.argv[1], "r"):
    l, n = line.rstrip().split("|")
    l = map(int, l.rstrip().split()) # list of numbers
    n = int(n.lstrip()) # times to do algorithm
    
    for i in range(n): # for each iteration...
        for j in range(0, len(l)): # do algorithm...
            temp = l[j:j+2] # two at a time...
            if len(temp) != 2:
                break

            if l[j] > l[j+1]:
                l[j+1], l[j] = temp
                break
    
    print " ".join(map(str, l))
