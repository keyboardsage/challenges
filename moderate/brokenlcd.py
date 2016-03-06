#!/usr/bin/env python

import sys
import re

# The integer used to index a location, will find the bit pattern needed to display that integer
# ex:
# you have bit pattern 00000000
# bin2Seg[0] will hold 11111100 because you need all segments on except the dot and middle horizontal line
bin2Seg = {0:0b11111100, 1:0b01100000, 2:0b11011010, 3:0b11110010, 4:0b01100110, 5:0b10110110, 6:0b10111110, 7:0b11100000, 8:0b11111110, 9:0b11110110}

# Integer to Binary String
# ex:
# 2 is converted into '00000010'
def i2bs(y):
    return bin(y)[2:].zfill(8)

for line in open(sys.argv[1],'r'):
    # extract data from line
    capable, num = line.rstrip().split(';')
    capable = map(lambda y: int(y, 2), capable.split()) # represents segment's capabilities

    # find the segments needed to display the desired number
    segs = []
    for e in list(num):
        if e.isdigit(): # add binary version of segments needed
            segs.append(bin2Seg[int(e)])
        else: # but if a dot appears, put it in MSB of previous element added
            segs.append(segs.pop() | int('00000001', 2))

    # now time to check if desired number can be displayed on broken screen
    # done by using regex that ensures 1s exist but doesn't care if the other bits are 0 or 1
    desired = ' '.join(map(i2bs, segs)).replace('0', '[01]{1}')
    state = ' '.join(map(i2bs, capable))
    print 1 if re.search(desired, state) else 0
