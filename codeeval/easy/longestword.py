#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    print sorted(line.rstrip().split(' '), key = len, reverse = True)[0]
