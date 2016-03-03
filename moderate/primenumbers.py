#!/usr/bin/python

import sys

# my primality code from prime palindrome
def isPrime(number):
    if number < 2: # must be positive integer greater than 1
        return False
    elif number ==  2:
        return True
    elif number % 2 == 0: # evens can never be prime
        return False

    # if number other than 1 and itself lacks a remainder, it is not prime
    # Note: This could be more efficient by skipping evens in the range
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

for line in open(str(sys.argv[1]), "r"):
    theN = int(line.strip())
    temp = ""
    for i in range (1, theN):
	    if isPrime(i) and i < theN:
			temp += str(i) + ","
    print temp[:-1]
