#!/usr/bin/env python

import sys

for line in open(str(sys.argv[1]), "r"):
    for word in reversed(line.strip().split(' ')):
        print word,
    print
