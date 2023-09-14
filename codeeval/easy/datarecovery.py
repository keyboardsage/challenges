#!/usr/bin/python

import sys
from sets import Set

for line in open (sys.argv[1],'r'):
    (sentence, hints) = line.rstrip().split(';')
    sentence = sentence.split(' ')
    hints = hints.split(' ')
    hints = hints + ([0] * (len(sentence) - len(hints)))
    tempList = sorted(zip(hints, sentence), key=lambda x: int(x[0]))
    output  = []
    last = 0

    missingNumberList = list((Set([i for i in range(max(map(int,hints))+1)]) - Set(map(int,hints))))
    missingNumber = missingNumberList[0] if len(missingNumberList) != 0 else 0

    for t in tempList:
        if int(t[0]) == 0:
            continue

        output.append(t[1])

    if missingNumber != 0:
        output.insert(missingNumber-1, tempList[0][1])
    else:
        output.append(tempList[0][1])

    print ' '.join(output)
