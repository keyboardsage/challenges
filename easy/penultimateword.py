#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    print line.strip().split(' ')[-2]
