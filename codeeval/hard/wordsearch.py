#!/usr/bin/python

import sys
import itertools

class Board:
    def __init__(self, boardValue, rowsValue, colsValue):
        self.board = boardValue
        self.rows, self.cols = rowsValue, colsValue
        self.seen = []
        self.X_TO_CHECK = [-1, 0, 1, 0]
        self.Y_TO_CHECK = [0, 1, 0, -1]

    def __str__(self):
        return self.board

    def getSearchLine(self):
        return self.seen
    
    def reset(self):
        self.seen = []
    
    def getPosition(self, theRow, theColumn): # topleft of board is 0,0
        return self.board[self.cols * theRow + theColumn]

    def getCoordList(self):
        # create coordinate list
        coord = [[(x, y) for y in range(self.cols)] for x in range(self.rows)]
        coord = coord[0] + coord[1] + coord[2]

        return coord

    def testGetPosition(self):
        coord = self.getCoordList()
    
        return ''.join([self.getPosition(x, y) for x, y in coord]) == self.board

    # check if word exists starting from top left
    def wordExists(self, r, c, theWord):
        if len(theWord) == 0: # no more letters? it exists
            return True
        elif self.getPosition(r, c) == theWord[0]: # first letter exists in this spot
            # catalog coordinates so we don't reuse the letter
            self.seen.append((r, c))
            
            # dispose of the unnecessary letter
            theWord = theWord[1:]

            # check neighbors for next letter
            for neigh in zip(self.X_TO_CHECK, self.Y_TO_CHECK):
                if (r + neigh[0]) < 0 or (c + neigh[1]) < 0: # skip low coord
                    continue
                elif (r + neigh[0]) == self.rows or (c + neigh[1]) == self.cols: # skip high coord
                    continue
                elif (r + neigh[0], c + neigh[1]) in self.seen: # skip already seen
                    continue
                elif self.wordExists(r + neigh[0], c + neigh[1], theWord): # other, check avenue
                    return True
    
        return False
    
theBoard = Board('ABCESFCSADEE', 3, 4)
COORDINATES = theBoard.getCoordList()
for line in open(sys.argv[1],'r'):
    exists = False
    
    # check for word starting from all locations
    for x, y in COORDINATES:
        theBoard.reset()
        if theBoard.wordExists(x, y, line.rstrip()):
            # testing purposes
            #print theBoard.getSearchLine()
            #print [theBoard.getPosition(x, y) for x, y in theBoard.getSearchLine()]

            exists = True
            break

    # report
    print exists
