#!/usr/bin/python

import sys

def higherNumberArray(a, b):
    return [(b[i] if b[i] > a[i] else a[i]) for i in range(len(a))]

for line in open (sys.argv[1], "r"):
    temp = []
    for row in line.strip().split('|'):
        if not temp:
            temp = map(int, row.strip().split(' '))
        else:
            temp = higherNumberArray(temp, map(int, row.strip().split(' ')))
    print ' '.join(map(str,temp))
    
