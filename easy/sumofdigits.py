#!/usr/bin/env python

import sys

for line in open(str(sys.argv[1]), "r"):
    print sum(map(int, list(line.rstrip())))
