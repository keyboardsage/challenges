#!/usr/bin/env python

import sys

for line in open(str(sys.argv[1]), "r"):
    temp = line.rstrip().split(',')
    theLine = temp[0]
    theChars = list(temp[1].strip())
    for character in theLine:
        if character not in theChars: sys.stdout.write(character)
    print
