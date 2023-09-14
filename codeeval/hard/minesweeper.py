#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    parts = line.rstrip().split(';')
    rows = int(parts[0].split(',')[0])
    cols = int(parts[0].split(',')[1])
    matrix = [[('0' if j == '.' else j) for j in list((parts[1])[x*cols:(x*cols)+cols])] for x in range(rows)]
    adjacentNodes = zip([-1,-1,-1,0,0,1,1,1],[1,0,-1,1,-1,1,0,-1])
    output = []

    # for every cell..
    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == '*': # if cell is a star...
                for node in adjacentNodes: # then for all adjacent nodes...
                    if (x+node[0]) < 0 or (y+node[1]) < 0 or (x+node[0]) == rows or (y+node[1]) == cols:
                        continue
                    elif matrix[x+node[0]][y+node[1]] == '*':
                        continue
                    else: # that are digits... 
                        matrix[x+node[0]][y+node[1]] = str(int(matrix[x+node[0]][y+node[1]])+1)
        output += matrix[x]

    print ''.join([''.join(x) for x in matrix])
