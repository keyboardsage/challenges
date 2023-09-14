#!/usr/bin/python

import sys
import itertools

for line in open (sys.argv[1],'r'):
    cn = line.rstrip().replace(' ', '')
    cn_doubled = [sum(map(int,list(str(digit + digit if i % 2 == 1 else digit)))) for i,digit in enumerate(reversed(map(int,list(cn))))]
    print 0 if sum(cn_doubled) % 10 != 0 else 1
