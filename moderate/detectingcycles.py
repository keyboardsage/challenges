#!/usr/bin/python

import sys
from collections import Counter

# find all subsequences of a list for the given pattern length
def allSubsequences(l, patLen):
    return zip(*[l[i:] for i in range(patLen)])

for line in open (sys.argv[1], "r"):
    answer = ()
    patCount = 0
    for n in range(len(line)-1,-1,-1): # range string length to 1
        sequences = allSubsequences(line.rstrip().split(' '), n)
        
        # skip empty sequences
        if len(sequences) == 0:
            continue

        # catalog
        temp = Counter(sequences).most_common(1)
        if temp[0][1] > patCount:
            #print "Replacing ", answer, "with count of", patCount, "with ", temp[0][0], "with count of", temp[0][1]
            answer = temp[0][0]
            patCount = temp[0][1]

    # print the answer
    print ' '.join(answer)
