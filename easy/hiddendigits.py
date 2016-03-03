#!/usr/bin/env python

import sys

for line in open (sys.argv[1], 'r'):
    output = ""
    for c in line.rstrip():
        if 96 < ord(c) < 107:
            output += str(ord(c) - 97)
        elif c.isdigit():
            output += c

    if output == "":
        print 'NONE'
    else:
        print ''.join(output)
