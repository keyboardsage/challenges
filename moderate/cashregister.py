#!/usr/bin/python

import sys
from collections import Counter

# Create a dictionary that can be used a constant
MONEY_DICT = {'PENNY': .01,'NICKEL': .05,'DIME': .10,'QUARTER': .25,'HALF DOLLAR': .50,'ONE': 1.00,'TWO': 2.00,'FIVE': 5.00,'TEN': 10.00,'TWENTY': 20.00,'FIFTY': 50.00,'ONE HUNDRED': 100.00}
MONEY_DICT = dict(zip(MONEY_DICT.values(), MONEY_DICT.keys()))

# For each of the lines...
for line in open(str(sys.argv[1]), "r"):
    theLine = map(float, line.split(';'))
    if theLine[0] > theLine[1]: # Show error if price more expensive than tinder...
        print "ERROR"
    elif theLine[0] == theLine[1]: # ZERO if equal
        print "ZERO"
    else: # Determine change
        theChangeAmount = theLine[1] - theLine[0]
        theChange = []

        for theMoneyVal in sorted(MONEY_DICT.keys(), reverse = True):
            temp = int(theChangeAmount / theMoneyVal)
            if temp > 0:
                theChangeAmount -= theMoneyVal
                theChange.append(MONEY_DICT[theMoneyVal])
        
        print ','.join(theChange)
