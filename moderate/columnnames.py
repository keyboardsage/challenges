#!/usr/bin/env python

import sys

for line in open (sys.argv[1], 'r'):
    n = int(line.rstrip())
    name = ""
    
    if n < 27: # 1 letter (26 possibilities)
        name = chr(n+64)
    elif n < 703: # 2 letters (26 + 26**2 possibilities)
        # determine characters taking into account 0 would be @, so make 0 a 26
        first = n / 26 if n % 26 != 0 else n / 26 - 1
        second = n % 26 if n % 26 != 0 else 26
        
        name = chr(first+64) + chr(second+64)
    else: # 3 letters (26 + 26**2 + 26**3 possibilities)
        # third character, 26 possible characters mod 26 gives last character
        third = n % 26 if n % 26 != 0 else 26

        # adjust number, divide to remove worries of the 3rd character from equation
        n = n / 26

        # same logic as before when we had only 2 letters
        second = n % 26 if n % 26 != 0 else 26
        first = n / 26 if n % 26 != 0 else n / 26 - 1
        
        name = chr(first+64) + chr(second+64) + chr(third+64)

    print name
