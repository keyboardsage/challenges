#!/usr/bin/env python

import sys

for line in open(str(sys.argv[1]), "r"):
    list1 = (line.strip().split('|')[0]).strip().split(' ')
    list2 = (line.strip().split('|')[1]).strip().split(' ')
    for x in range(len(list1)):
        print (int(list1[x]) * int(list2[x])),
    print
