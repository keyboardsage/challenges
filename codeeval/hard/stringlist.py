#!/usr/bin/python

import sys
import itertools

for line in open (str(sys.argv[1]), "r"):
    t = line.rstrip().split(',')
    n = int(t[0])
    s = list(t[1])
    print ",".join(["".join(prod) for prod in sorted(list(set(itertools.product(s, repeat=n))))])
