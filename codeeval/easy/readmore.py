#!/usr/bin/python

import sys

def readMore(theText):
    if len(theText) <= 55: print theText
    else:
        temp = theText[:40]
        print temp.rsplit(" ", 1)[0] + "... <Read More>"

for line in open(sys.argv[1], "r"):
    readMore(line.rstrip())
