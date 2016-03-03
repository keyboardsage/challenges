#!/usr/bin/python

import sys

for line in open (sys.argv[1], 'r'):
    s = line.rstrip().split(' ')
    output = ""
    iterZeros = iter(s)
    for t in iterZeros:
        if t == '0':
            output += next(iterZeros)
        else:
            output += '1' * len(next(iterZeros))
    print int('0b' + output, 2)
