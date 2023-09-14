#!/usr/bin/python

import sys
import itertools

def allSubsequences(theList, theX):
    return zip(*[theList[i:] for i in range(theX)])

for line in open (sys.argv[1], "r"):
    (l, s) = tuple(line.strip().split(';'))
    s = int(s)
    l = map(int, l.split(','))
    output = []
    for i in itertools.combinations(l,2):
        if sum(i) == s:
            output.append(str(i[0]) + ',' + str(i[1]))
    if len(output) > 0:
        print ';'.join(output)
    else:
        print"NULL"
