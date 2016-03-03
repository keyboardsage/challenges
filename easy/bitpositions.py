#!/usr/bin/python

import sys

fo = open (str(sys.argv[1]), "r")

for line in fo:
	# prepare variables
	theNumber = bin(int(line.strip().split(',')[0]))[2:].zfill(128)
	position1 = theNumber[int("-" + line.strip().split(',')[1])]
	position2 = theNumber[int("-" + line.strip().split(',')[2])]

    # print results
	print 'true' if position1 == position2 else 'false'
