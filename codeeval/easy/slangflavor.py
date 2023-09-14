#!/usr/bin/python

import sys

SLANG_LIST = [', yeah!', ', this is crazy, I tell ya.', ', can U believe this?', ', eh?', ', aw yea.', ', yo.', '? No way!', '. Awesome!' ]

def nextSlang(number):
    return SLANG_LIST[number % len(SLANG_LIST)]

count = 0
for line in open (str(sys.argv[1]), "r"):
    for character in list(line):
        if character == '.' or character == '!' or character == '?':
            count += 1
            if count % 2 == 0:
                sys.stdout.write(nextSlang((count / 2) - 1))
                continue
        sys.stdout.write(character)
