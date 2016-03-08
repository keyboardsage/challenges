#!/usr/bin/env python

import sys
from collections import Counter
import operator

for line in open (sys.argv[1], "r"):
    # prepare variables
    wordLen, lastChar, encMessage = map(str.strip,line.split('|'))
    l = int(wordLen)
    encMessage = encMessage.split()
    
    iterationsNeeded = range(len(encMessage) - (l-1))
    charSlices = [' '.join(encMessage[i:i+l]) for i in iterationsNeeded] # slices
    slices = [(' '.join(encMessage[i:i+l]), i, i+l, charSlices.count(' '.join(encMessage[i:i+l]))) for i in iterationsNeeded] # slices w/ begin & end
    
    # find space character
    delta = 0
    # for each tuple...
    for theTuple in slices:
        theSlice, beg, end, c = theTuple
        if c == 2: # ...if the slice shows up twice
            # find both occurrences
            both = [s for s in slices if s[0] == theSlice]

            # prune out all the impossible indices
            neighbors = [encMessage[e] for e in [both[0][1] - 1, both[0][2], both[1][1] - 1, both[1][2]] if e != -1]
            neighbors = map(int, neighbors)

            # confirm that all indices are the same number
            if all(e == neighbors[0] for e in neighbors) :
                # if all indices are the same then this COULD be the pattern in question
                spaceChar = neighbors[0]
                
                # a delta (n) added to slice's last letter should result in the last letter provided to us
                SPACE_ASCII = 32
                delta = -(spaceChar - SPACE_ASCII)
                if int(theSlice.split()[-1]) + delta == ord(lastChar):
                    break
    
    # print the message
    print ''.join([chr(m+delta) for m in map(int, encMessage)])
