#!/usr/bin/env python

import sys

for line in open(str(sys.argv[1]), "r"):
    for character in list(line.strip()):
        if character.isupper():
            sys.stdout.write(character.lower())
        elif character.islower():
            sys.stdout.write(character.upper())
        else:
            sys.stdout.write(character)
    print 
