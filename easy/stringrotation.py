#!/usr/bin/python

import sys
import collections

for line in open (sys.argv[1], "r"):
    s1 = line.strip().split(',')[0]
    s2 = list(line.strip().split(',')[1])
    
    isS1Satisfiable = True
    if len(s1) > len(s2): # more letters in s1, false
        isS1Satisfiable = False
    elif len(set(list(s1)).difference(set(s2))) > 0: # letters in s1 not present in s2, false
        isS1Satisfiable = False
    else:
        # otherwise check that s2 has enough of each letter to satisfy s1
        setOfLettersInS1 = set(list(s1))
        s1CountList = collections.Counter(list(s1)) 
        s2CountList = collections.Counter(s2)
        for letter in setOfLettersInS1:
            if (letter in s1CountList.keys()) and (letter in s2CountList.keys()):
                if s1CountList[letter] > s2CountList[letter]:
                    isS1Satisfiable = False
                    break
#            elif (letter in s1CountList.keys()) and (letter not in s2CountList.keys()):
#                isS1Satisfiable = False
#                break

    print "True" if isS1Satisfiable else "False"
