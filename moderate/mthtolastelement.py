#!/usr/bin/env python

import sys

for line in open(str(sys.argv[1]), "r"):
    temp = line.strip().split(' ')
    mth = int(temp[-1])
    listLength = len(temp) - 1
    if mth > listLength:
        continue
    else:
        print temp[len(temp)-mth-1]
