#!/usr/bin/env python

import sys
import itertools

possibilities = [[0],[1],list('abc'),list('def'),list('ghi'),list('jkl'),list('mno'),list('pqrs'),list('tuv'),list('wxyz')]

for line in open(sys.argv[1], "r"):
    temp = []
    for digit in map(int,list(line.rstrip())):
        temp.append(possibilities[digit])
    print ','.join([''.join(map(str, x)) for x in list(itertools.product(*temp))])
