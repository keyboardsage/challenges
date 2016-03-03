#!/usr/bin/python

import sys
import re

for line in open(sys.argv[1], "r"):
    zeroCount, n = map(int, line.rstrip().split(' '))
    accum = 0
    for i in range(1, n+1):
        if len(re.findall(r"0", bin(i)[2:])) == zeroCount:
            accum += 1
    print accum
