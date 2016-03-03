#!/usr/bin/python

import sys
import itertools

for line in open (str(sys.argv[1]), "r"):
    s = line.strip()
    print ",".join(["".join(perm) for perm in sorted(itertools.permutations(s, len(s)))])
