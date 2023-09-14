#!/usr/bin/env python

import sys

for line in open(sys.argv[1], "r"):
    mainStr, subStr = tuple(line.rstrip().split(','))
    found = "false"
    
    if len(subStr) <= len(mainStr):
        # clean up the substring so it is findable
        # convert asterisks prepended by backslash into just asterisk (makes it findable as an exact pattern)
        # convert asterisks into ~, it will be used as an indication to act as a wildcard
        subStrLst = list(subStr)
        subStrClean = [(("*" if subStrLst[i-1] == "\\" else "~") if l == "*" else l) for i, l in enumerate(subStrLst) if l != "\\"]
        subStrClean = ''.join(subStrClean)

        # now actually find the substring
        stack1 = []
        mainStrLst = list(mainStr)
        for i, l in enumerate(mainStrLst):
            stack1.append(l)
            
            # check 1: exact match
            temp = ''.join(stack1[-(len(subStrClean)):])
            if temp == subStrClean: # check for literal pattern match (1 for 1 exact match)
                found = "true"
                break
            
            # check 2: wildcard match
            temp = subStrClean.split('~')
            if len(temp) > 1 and mainStr.find(temp[0])+len(temp[0]) <= mainStr.find(temp[1]): # wild card match
                found = "true"
                break

            # testing purposes
            #print '-' + ''.join(stack1[-(len(subStr)):]) + '-', '-' + subStr + '-'
            #print subStrClean.split('~')
            #print mainStr.find(subStrClean.split('~')[0]), len(subStrClean.split('~')[0])#, mainStr.find(subStrClean.split('~')[1])
    
    print found
