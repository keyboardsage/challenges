#!/usr/bin/python

import sys
from collections import Counter

for line in open (str(sys.argv[1]), "r"):
    temp = line.strip().split(',')
    theCount = Counter(temp).most_common(2)
    

    if theCount[0][1] == theCount[1][1] or (len(temp) / 2) > theCount[0][1]:
        print "None"
    else:
        print theCount[0][0]
