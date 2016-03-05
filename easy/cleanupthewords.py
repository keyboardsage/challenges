#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    output = ""
    for c in line.rstrip():
        if c.isalpha():
            output += c
        elif (not c.isalpha()) and len(output) > 0 and output[-1] != " ":
            output += " "
    print output.lower()
