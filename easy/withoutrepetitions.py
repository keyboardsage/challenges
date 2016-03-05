#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    # prepare line
    line = list(line.rstrip())
    # keep first letter and each successive letter AS LONG as previous adjacent letter is unique
    temp = [val for index, val in enumerate(line) if (index == 0 or val != line[index-1])]
    # show output
    print ''.join(temp)
