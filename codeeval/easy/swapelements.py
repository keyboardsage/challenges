#!/usr/bin/python

import sys

fo = open (str(sys.argv[1]), "r")

for line in fo:
    tempList = line.strip().split(':')
    theList = map(int, tempList[0].rstrip(' ').split(' '))
    swapLists = [x.strip(' ') for x in tempList[1].split(',')]
    for i in range(len(swapLists)):
        swapPosition1 = int(swapLists[i].split('-')[0])
        swapPosition2 = int(swapLists[i].split('-')[1])
        stash = theList[swapPosition1]
        theList[swapPosition1] = theList[swapPosition2]
        theList[swapPosition2] = stash
    print ' '.join(map(str, theList))
