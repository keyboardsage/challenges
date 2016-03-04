#!/usr/bin/env python

import sys

for line in open(sys.argv[1],'r'):
    # get symbols
    a, b, c, t = line.rstrip().split()
    
    # Starting with obvious winner...
    if a[1] == t and b[1] != t: # ...if A not the trump suit but B hand is
        hc = a
    elif a[1] != t and b[1] == t: # ...and vice versa is true of course
        hc = b
    else: # now here is the system, check if A hand has the higher special card
        if a[0] == 'A' and b[0] != 'A':
            hc = a
        #if a[0] == '2' and b[0] != '2':
        #    hc = a
        elif a[0] == 'K' and b[0] != 'K':
            hc = a
        elif a[0] == 'Q' and b[0] != 'Q':
            hc = a
        elif a[0] == 'J' and b[0] != 'J':
            hc = a
        elif a[:-1].isdigit() and b[:-1].isdigit() and int(a[:-1]) > int(b[:-1]): # or number
            hc = a
        elif a[:-1] == b[:-1]: # or if there is a draw
            hc = a + " " + b
        else: # if A hasn't won yet then A must have lossed
            hc = b

    print hc
