#!/usr/bin/python

import sys
import re

for line in open(sys.argv[1], "r"):
    temp = line.rstrip()
    accum = 0
    for i in range(0, len(temp)):
        temp2 = temp[i:i+5]
        if len(temp2) != 5:
            continue
        accum += len(re.findall(r">>-->", temp2)) + len(re.findall(r"<--<<", temp2))
    print accum
