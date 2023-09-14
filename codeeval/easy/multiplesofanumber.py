#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    # prepare variables
    x, n = tuple(map(int, line.rstrip().split(',')))
    t = 0
    
    # find multiples and stop when multiple is higher than x
    for i in range(1, 1000):
        t = n * i
        if t >= x:
            break

    # print the finding
    print t
