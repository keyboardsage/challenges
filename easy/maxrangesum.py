#!/usr/bin/python

import sys

fo = open (str(sys.argv[1]), "r")

for line in fo:
	#Prepare variables
	splitLine = line.strip().split(';')
	theN = int(splitLine[0])
	theDays = map(int, str(splitLine[1]).split(' '))

	#Find largest number
	largestNumber = 0;
	for base in range(len(theDays)-theN+1):
		chunkOfDays = sum(theDays[base:(base+theN)])
		if (chunkOfDays > largestNumber):
			largestNumber = chunkOfDays

	# check the sum, make 0 if necessary
	print ( 0 if (largestNumber < 0) else largestNumber)
