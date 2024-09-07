import heapq

class Node:
    def __init__(self, position, g=0, h=0, parent=None):
        pass

open = []
#heapify
closed = []

#pop from minheap
#if node is goal:
#   retrace and return path
#add to closed
#
#for each neighbor
#   if not in open:
#       compute g, h, and f scores
#       set parent to current node
#       add to open
#   if in open:
#       if current path has lower g score:
#           update score and parent

