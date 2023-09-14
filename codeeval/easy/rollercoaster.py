#!/usr/bin/env python

import sys

makeNextUpper = True;
def rollercoasterfy(theString):
    global makeNextUpper
    tempLine = ""
    makeNextUpper = True;
    for aChar in theString:
        if aChar.isalpha():
            tempLine += aChar.upper() if (makeNextUpper == True) else aChar.lower()
            makeNextUpper = makeNextUpper ^ True
        else:
            tempLine += aChar
    return tempLine

for line in open(str(sys.argv[1]), "r"):
    print rollercoasterfy(line),
