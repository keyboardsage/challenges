#!/usr/bin/python

import sys

count = 0

def challengeFunc(n):
    global count
    count += 1

    # reverse digits of chosen number
    new_n = str(int(n) + int(n[::-1]))

    # if palindrome return palindrome, otherwise rince & repeat
    return (new_n if new_n == new_n[::-1] else challengeFunc(new_n))

for line in open (sys.argv[1], "r"):
    count = 0
    print ' '.join(reversed([challengeFunc(line.strip()), str(count)]))
