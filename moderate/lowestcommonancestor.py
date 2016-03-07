#!/usr/bin/python

import sys

tree = [30, 8, 52, 3, 20, -1, -1, -1, -1, 10, 29]

# get left child
def left(indexOfNode):
    return indexOfNode * 2 + 1

# get right child
def right(indexOfNode):
    return indexOfNode * 2 + 2

# get parent
def parent(indexOfNode):
    if indexOfNode == 0:
        return indexOfNode

    return (indexOfNode / 2 - 1) if indexOfNode % 2 == 0 else (indexOfNode / 2)

# traverse path to get to the node in question
def traversalPath(nodeValue):
    currentNodeIndex = tree.index(nodeValue) # starting from node in question

    temp = []
    while currentNodeIndex != 0: # until we find root
        temp.append(tree[currentNodeIndex]) # catalog the node
        currentNodeIndex = parent(currentNodeIndex) # goto parent

    # add the root
    temp.append(30)
    
    return temp

# find the common ancestor between two binary tree lists
def findCommonAncestor(path1, path2):
    for x in path1:
        if x in path2:
            return x

for line in open (sys.argv[1], "r"):
    node1, node2 = map(int, line.rstrip().split(' '))
    
    print findCommonAncestor(traversalPath(node1), traversalPath(node2))
