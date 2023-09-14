#!/usr/bin/env python

import sys

def ageDistribution(x):
    if x < 3:
        return 'Still in Mama\'s arms'
    elif x < 5:
        return 'Preschool Maniac'
    elif x < 12:
        return 'Elementary school'
    elif x < 15:
        return 'Middle school'
    elif x < 19:
        return 'High school'
    elif x < 23:
        return 'College'
    elif x < 66:
        return 'Working for the man'
    elif x < 101:
        return 'The Golden Years'
    else:
        'This program is for humans'

for line in open(str(sys.argv[1]), "r"):
    print ageDistribution(int(line.strip()))
