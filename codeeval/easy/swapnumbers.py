#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    output = []
    for word in line.strip().split(' '):
        output.append(word[-1] + word[1:-1] + word[0])
    print ' '.join(output)
