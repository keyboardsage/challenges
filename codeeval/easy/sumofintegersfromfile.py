#!/usr/bin/env python

import sys

print sum([int(line.strip()) for line in open(str(sys.argv[1]), "r")])
