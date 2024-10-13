import heapq
import math


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
    
    def __eq__(self, other):
        return self.position == other.position



def euclidean_distance(node, goal):
    h_score = math.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)
    return h_score


def a_star(graph, start, goal):
    start_node = Node(start, h=euclidean_distance(start, goal))
    #instantiate 'open' min heap and add start node
    open_list = []
    heapq.heappush(open_list, start_node)
    #create set for closed nodes
    closed_set = set()

    while open_list:
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
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
            next_pos = (current_node.position[0] + dx, current_node.position[1] + dy)
            #if out of bounds, or an obstacle, or traversed, continue
            if (next_pos[0] < 0 or next_pos[0] >= len(graph) or next_pos[1] < 0 or next_pos[1] >= len(graph[0]) or graph[next_pos[0]][next_pos[1]] == 1 or next_pos in closed_set):
                continue
            #add to current path cost 
            new_g = current_node.g + + euclidean_distance(current_node.position, next_pos)
            #calculate heuristic for new_node
            new_h = euclidean_distance(next_pos, target)
            #instantiate new_node
            new_node = Node(position=next_pos, g=new_g, h=new_h, parent=current_node)

            if new_node not in open_list:
                heapq.heappush(open_list, new_node)
            else:
                index = open_list.index(new_node)
                #if new path is more efficient, use it
                if open_list[index].g > new_g:
                    open_list[index] = new_node
                    heapq.heapify(open_list)
    return None

graph = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
goal = (4, 4)

path = a_star(graph, start, goal)
print(f"Path found: {path}")

