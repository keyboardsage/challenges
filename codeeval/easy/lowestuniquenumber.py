#!/usr/bin/env python

import sys

def pruneDups(originalList):
    dupList = [x for x in originalList if originalList.count(x) > 1]
    uniqList = [i for i in originalList if i not in dupList]
    lowestNumber = sorted(uniqList, key = int)[0] if len(uniqList) > 0 else 0
    return (originalList.index(lowestNumber) + 1) if lowestNumber != 0 else 0

for line in open(str(sys.argv[1]), "r"):
    print pruneDups(map(int, line.strip().split(' ')))
