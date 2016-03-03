#!/usr/bin/env python

import sys

for line in open(str(sys.argv[1]), "r"):
    digits = []
    words = []
    for temp in line.strip().split(','):
        digits.append(temp) if temp.isdigit() else words.append(temp)
    if len(words) != 0 and len(digits) != 0:
        print str(',').join(words) + '|' + str(',').join(digits)
    elif len(words) != 0:
        print str(',').join(words)
    else:
        print str(',').join(digits)
