#!/usr/bin/python

import sys
from collections import Counter

for line in open(sys.argv[1], "r"):
    wines, letters = line.rstrip().split('|')
    wines = wines.rstrip().split()
    letters = letters.lstrip()
    output = []

    # each word...
    for word in wines:
        wc = Counter(word)
        lc = Counter(letters)
        ws = set(word)
        ls = set(letters)
        keep = True

        # check
        if not ls < ws: # no point keeping the word if the letters aren't a subset
            continue
        else:
            for lkey in lc:
                if lc[lkey] > wc[lkey]: # if not enough of each letter...
                    keep = False # don't keep this word...
                    break # ...and stop check because we already have reason to disregard
        
        # if word still worth keeping, even after checks, record the word
        if keep:
            output.append(word)

    print " ".join(output) if len(output) != 0 else "False"
