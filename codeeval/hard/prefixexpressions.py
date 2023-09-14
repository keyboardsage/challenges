#!/usr/bin/env python

import sys

stack = []
for line in open(sys.argv[1], "r"):
    for token in reversed(line.rstrip().split(' ')):
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            stack.append(stack.pop() - stack.pop())
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            stack.append(stack.pop() / stack.pop())
        else:
            stack.append(float(token))

    print int(stack.pop())
