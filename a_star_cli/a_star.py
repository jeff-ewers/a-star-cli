import heapq
import math

target = (4, 4)

def create_graph():
    #create sample graph with some variation
    graph = {}
    for x in range(5):
        for y in range(5):
            neighbors = {}
            #vary x and y coordinate to iterate neighbors
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        weight = 1
                        if (x, y) == (1, 1) and (nx, ny) == (1, 2):
                            weight = 3
                        elif (x, y) == (3, 3) and (nx, ny) == (3, 4):
                            weight = 5
                        elif (x, y) == (2, 2) and (nx, ny) == (3, 2):
                            weight = 3
                        neighbors[(nx, ny)] = weight
            graph[(x, y)] = neighbors
    return graph

test_graph = create_graph()
print(test_graph)

class Node:
    def __init__(self, position, g=0, h=0, parent=None):
        self.position=position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
    
    def __lt__(self, other):
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

        if current_node.position == goal:
            path = []
            path.append(current_node.position)
            current_node = current_node.parent
        return path[::-1]



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

