#!/usr/bin/env python

import sys
import re

for line in open(sys.argv[1], "r"):
    if line.rstrip() == "":
        continue
    else:
        matchObj = re.match( r'^[\w\.\+]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$', line.rstrip(), re.M|re.I)
        print "true" if matchObj else "false"
