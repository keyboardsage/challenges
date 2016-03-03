#!/usr/bin/python

import sys

for line in open(sys.argv[1], "r"):
    d = [map(int, i) for i in map(str.split, map(str.strip, line.rstrip().split('|')))]
    u = sorted(list(set(sum(d, []))))
    output = ""

    for i in u:
        c = 0
        output += str(i) + ":"
        temp = []

        for j in d:
            c += 1
            if i in j:
                temp.append(c)
        
        output += ",".join(map(str, temp)) + "; "

    print output.rstrip()
