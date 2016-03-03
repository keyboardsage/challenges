#!/usr/bin/env python

import sys
import math

for line in open(sys.argv[1],'r'):
    data = line.rstrip().split(' ')
    n = int(math.sqrt(len(''.join(data))))
    output = []
    for j in range(n):
        for i in reversed(range(n)):
            output += data[(i*n)+j]
    print ' '.join(output)
