#!/usr/bin/python

import sys

def capitalizeRestStringUnchanged(theString):
	return theString[0].upper() + theString[1:]

fo = open (str(sys.argv[1]), "r")

str2 = ' '
for line in fo:
	print str2.join(map(capitalizeRestStringUnchanged, line.strip().split(' ')))
