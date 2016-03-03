#!/usr/bin/env python

import sys
import urllib

def prepCompare(theURI):
    theURI = theURI.split('/')
    theURI[0] = theURI[0].lower() # scheme insensitive
    theURI[2] = theURI[2].lower() # host insensitive
    if theURI[2].find(':') == -1:
        theURI[2] = theURI[2] + ":80" # fix port if necessary
    return str('/').join(theURI)

for line in open(str(sys.argv[1]), "r"):
    uri1 = prepCompare(urllib.unquote(line.strip().split(';')[0]).decode('utf8'))
    uri2 = prepCompare(urllib.unquote(line.strip().split(';')[1]).decode('utf8'))
    print (True if uri1 ==  uri2 else False)
