#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    word = max(line.rstrip().split(), key=len)
    print ' '.join([('*' * i) + l for i,l in enumerate(word)])
