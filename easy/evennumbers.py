#!/usr/bin/env python

import sys

for line in open(str(sys.argv[1]), "r"):
    print (int(line.strip()) % 2) ^ 1
