#!/usr/bin/env python

import sys

ONES = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifthteen','Sixthteen','Seventeen','Eighteen','Nineteen'] # ones and special combos really
TENS = ['Zero','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']

'''
Used for digit groups in thousands and above
'''
def digitGroupNumber(digits):
    digits = str(digits).zfill(3)
    hundreds = int(digits[0])
    tens = int(digits[1])
    ones = int(digits[2])
    numAsLetters = []

    if hundreds != 0:
        numAsLetters.append(ONES[hundreds]+"Hundred")
    
    if tens != 0:
        numAsLetters.append(ONES[tens+9]) if tens == 1 else numAsLetters.append(TENS[tens])
    
    if ones != 0:
        numAsLetters.append(ONES[ones])

    return ''.join(numAsLetters)

for line in open(sys.argv[1], "r"):
    output = []
    target = int(line.rstrip())
    for position in [1000000000,1000000,1000,100,10,1]:
        # find digit for position and setup words to print
        posDigit = target / position

        # new target
        target = target % position
        
        # continue to the next iteration because there is a zero in place other than ones
        if posDigit == 0 and position != 1:
            continue
        
        # number to text
        if position == 1000000000:
            output.append(digitGroupNumber(posDigit)+"Billion")
        elif position == 1000000:
            output.append(digitGroupNumber(posDigit)+"Million")
        elif position == 1000:
            output.append(digitGroupNumber(posDigit)+"Thousand")
        elif position == 100:
            output.append(ONES[posDigit]+"Hundred")
        elif position == 10:
            if posDigit == 1:
                output.append(ONES[posDigit+9])
            else:
                output.append(TENS[posDigit])
        elif position == 1:
            output.append(ONES[posDigit])

        # short circuit if necessary
        if target == 0:
            break
    
    print ''.join(output) + "Dollars"
