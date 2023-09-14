#!/usr/bin/python

import sys

for line in open (str(sys.argv[1]), "r"):
    binaryNumber = bin(int(line.rstrip()))[2:]
    print list(binaryNumber).count('1')
