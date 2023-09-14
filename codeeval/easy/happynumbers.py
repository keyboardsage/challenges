#!/usr/bin/env python

import sys
from sets import Set

for line in open(sys.argv[1],'r'):
    n = int(line.strip())
    seen = Set()
    while n != 1 and (n not in seen):
        seen.add(n)
        n = sum([i**2 for i in map(int,list(str(n)))])
    print 0 if n in seen else 1
