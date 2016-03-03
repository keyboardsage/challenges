#!/usr/bin/env python

import sys

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0 for y in range(cols)] for x in range(rows)]

    def setCol(self, col, number):
        for t in range(self.rows):
            self.board[t][col-1] = number

    def setRow(self, row, number):
        self.board[row-1] = [number for t in self.board[row-1]]

    def queryCol(self, col):
        counter =0
        for t in range(self.rows):
            counter += self.board[t][col-1]
        return counter

    def queryRow(self, row):
        return sum(self.board[row-1])

    def debug(self):
        print self.board

theBoard = Board(*(256,256))
for line in open(sys.argv[1], "r"):
    theLine = line.rstrip().split(' ')
    if theLine[0] == "SetCol":
        theBoard.setCol(int(theLine[1]),int(theLine[2]))
    elif theLine[0] == "SetRow":
        theBoard.setRow(int(theLine[1]),int(theLine[2]))
    elif theLine[0] == "QueryCol":
        print theBoard.queryCol(int(theLine[1]))
    elif theLine[0] == "QueryRow":
        print theBoard.queryRow(int(theLine[1]))
