#!/usr/bin/python

import sys

for line in open (sys.argv[1],'r'):
    (numbers, pattern) = line.rstrip().split(' ')
    isMinus = False if pattern.find('-') == -1 else True
    if not isMinus:
        left = numbers[0:pattern.find('+')]
        right = numbers[len(left):]
        print int(left) + int(right)
    elif isMinus:
        left = numbers[0:pattern.find('-')]
        right = numbers[len(left):]
        print int(left) - int(right)
