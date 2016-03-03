#!/usr/bin/env python

import sys

class Stack():
    def __init__(self):
        self.stack = []

    def push(self,theValue):
        self.stack = self.stack + [theValue]

    def pop(self):
        retVal = self.stack[len(self.stack)-1]
        self.stack = self.stack[:-1]
        return retVal

    def size(self):
        return len(self.stack)

theStack = Stack()
for line in open(sys.argv[1], "r"):
    for digit in line.strip().split(' '):
        theStack.push(digit)

    output = []
    for i in range(0,theStack.size(),2):
        try:
            output.append(theStack.pop())
            theStack.pop()
        except IndexError:
            break

    print ' '.join(output)
