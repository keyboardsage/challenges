#!/usr/bin/env python

import sys

def isPalindrome(word):
    revWord = ''.join(reversed(list(word)))
    return word == revWord

def isPrime(number):
    if number < 2: # must be positive integer greater than 1
        return False
    elif number % 2 == 0: # evens can never be prime
        return False

    # if number other than 1 and itself lacks a remainder, it is not prime
    # Note: This could be more efficient by skipping evens in the range
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

for i in range(1000,-1,-1):
    if isPalindrome(str(i)) and isPrime(i):
        print i
        break
