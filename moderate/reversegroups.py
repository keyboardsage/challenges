#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    fileList = (line.strip().split(';')[0]).split(',')
    k = int(line.strip().split(';')[1])
    subLists = [fileList[i:i + k] for i in range(0, len(fileList), k)]
    tempList = []
    for subList in subLists:
        tempList += (reversed(subList) if len(subList) == k else subList)
    print ','.join(tempList)
