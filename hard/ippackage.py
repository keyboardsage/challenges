#!/usr/bin/env python

import sys

def ip2hex(ip):
    return ['%02x' % h for h in map(int,ip.split('.'))]

for line in open(sys.argv[1], 'r'):
    # setup
    src, dst, pktHex = line.rstrip().split(' ', 2)
    src = ip2hex(src)
    dst = ip2hex(dst)
    pkt = pktHex.split()
    
    # replace ip addresses
    pkt[12], pkt[13], pkt[14], pkt[15] = src[0], src[1], src[2], src[3]
    pkt[16], pkt[17], pkt[18], pkt[19] = dst[0], dst[1], dst[2], dst[3]
    
    # calculate checksum
    ipLen = int((pkt[0])[1]) * 4
    ipHeader = ''.join(pkt[:(ipLen)]).replace(" ", "")
    #ipHeader="4500 003c 1c46 4000 4006 b1e6 ac10 0a63 ac10 0a0c".replace(" ", "") # thegeekstuff example
    #ipHeader="4500 0073 0000 4000 4011 b861 c0a8 0001 c0a8 00c7".replace(" ", "") # wikipedia example
    #ipHeader="4504 05dc b73a 4000 2e06 11cd bea8 0060 bea8 0060".replace(" ", "") # codeeval example
    ipHeader = map(''.join, zip(*[iter(''.join(ipHeader))]*4)) # pythonic way of splitting into groups of 4
    ipHeader[5] = '0000' # do not include checksum field
    sumHex = 0
    for x in ipHeader:
        #print sumHex, "+", int(x,16), hex(sumHex)
        sumHex = sumHex + int(x,16)
        #print "Giving", hex(sumHex)
        if len("{0:b}".format(sumHex)) > 16:
            sumHex = sumHex & 0x0FFFF
            sumHex += 1
    theChecksum = '%04x' % (~sumHex & 0xFFFF)

    # replace checksum
    ipHeader[5] = theChecksum[:2] + theChecksum[2:]

    # print in proper format
    print ' '.join([x[:2] + ' ' + x[2:] for x in ipHeader])
