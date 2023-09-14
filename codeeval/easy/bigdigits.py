#!/usr/bin/python

import sys

# list of lists representing the digits
theDigits = [
    ['-**-','*--*','*--*','*--*','-**-'],
    ['--*-','-**-','--*-','--*-','-***'],
    ['***-','---*','-**-','*---','****'],
    ['***-','---*','-**-','---*','***-'],
    ['-*--','*--*','****','---*','---*'],
    ['****','*---','***-','---*','***-'],
    ['-**-','*---','***-','*--*','-**-'],
    ['****','---*','--*-','-*--','-*--'],
    ['-**-','*--*','-**-','*--*','-**-'],
    ['-**-','*--*','-***','---*','-**-']
]

WIDTH_OF_EACH_NUMBER = 4
for line in open(sys.argv[1],'r'):
    digits = ''.join([x for x in list(line.rstrip()) if x.isdigit()])
    n = len(digits)
    for i in range(5):
        c = 0
        for digit in digits:
            c += 1
            sys.stdout.write(theDigits[int(digit)][i] + '-')
        print
    print '-' * ((n*WIDTH_OF_EACH_NUMBER) + n) # plus n represents the trailing -
