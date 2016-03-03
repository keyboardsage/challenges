#!/usr/bin/python

import sys
import re

for line in open(sys.argv[1], "r"):
    l = []
    l = line.rstrip().split()
    accum = 0
    output = []
    
    # normalizing by fixing sementics
    l[0] = l[0].replace('.','\.')
    l[0] = l[0].replace('?','.{1}')
    l[0] = l[0].replace('*','.*')
    l[0] = "^" + l[0] + "$"

    for word in l[1:]:
    #    try:
            if len(re.findall(l[0], word)):
                output.append(word)
    #    except:
    #        print l[0]
    #        break

    print " ".join(output) if len(output) != 0 else "-"
