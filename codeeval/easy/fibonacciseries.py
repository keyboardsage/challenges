#!/usr/bin/env python

import sys

def fibseq(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibseq(n-1) + fibseq(n-2)

for line in open(str(sys.argv[1]), "r"):
    print fibseq(int(line.strip()))
