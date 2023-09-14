#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    u = 0
    l = 0
    for letter in list(line.strip()):
        if letter.isupper():
            u += 1
        else:
            l += 1

    print "lowercase: %.2f uppercase: %.2f"  % (((float(l)/float(l+u)) * 100), ((float(u)/float(l+u)) * 100))
