import heapq
import math

target = (4, 4)



class Node:
    def __init__(self, position, g=0, h=0, parent=None):
        self.position=position
        # g = cost of the path from the start node to n
        self.g = g
        # h = heuristic estimate of the cost of the cheapest path from n to the goal
        self.h = h
        # f = f-score for minimization
        self.f = g + h
        self.parent = parent
    
    def __lt__(self, other):
        #less than
        return self.f < other.f


def euclidean_distance(node, target):
    h_score = math.sqrt((node[0] - target[0])**2 + (node[1] - target[1])**2)
    return h_score


def astar(test_graph, start, goal):
    start_node = Node(start, h=euclidean_distance(start, goal))
    #instantiate 'open' min heap and add start node
    open_list = []
    heapq.heappush(open_list, start_node)
    #create set for closed nodes
    closed_set = set()

    while open:
        current_node = heapq.heappop(open_list)
        #if current node is goal, retrace path and return inverse
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
    
        closed_set.add(current_node.position)
        #for each neighbor

    return None

test_graph = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
goal = (4, 4)

path = astar(test_graph, start, goal)
print(f"Path found: {path}")



#heapify
# heapq.heapify(open)
# closed = []

#pop from minheap
# current_node = heapq.heappop(open)
#if node is goal:
# if current_node == target:
#     pass
    #while not origin
        #get parent
        #add parent

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

