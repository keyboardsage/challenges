#!/usr/bin/env python

for y in range (1,13):
    for x in range(1,13):
        if x == 1:
            print (x*y),
        else:
            print '%3d' % (x*y),
    print
