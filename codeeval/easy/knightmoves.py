#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    pos = list(line.strip())
    C = ord(pos[0])
    N = int(pos[1])
    output = []
    colsToCheck = [chr(C+col) for col in [-2, -2, -1, -1, 1, 1, 2, 2]]
    rowsToCheck = [N+row for row in [1, -1, 2, -2, 2, -2, 1, -1,]]
    for move in zip(colsToCheck, rowsToCheck):
        if move[0] < 'a' or move[0] > 'h' or move[1] < 1 or move[1] > 8:
            continue
        else:
            output.append(move[0] + str(move[1]))
    print ' '.join(sorted(output))
