#!/usr/bin/env python

import sys

for line in open (sys.argv[1], 'r'):
    w, b = line.rstrip().split()
    output = ""
    
    for w, b in zip(w, b):
        if int(b):
            output += w.upper()
        else:
            output += w

    print output
