#!/usr/bin/env python

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

for line in open(sys.argv[1], "r"):
    (low, high) = tuple(map(int,line.rstrip().split(',')))
    high += 1

    print sum([1 for i in range(low,high) if isPrime(i)])
