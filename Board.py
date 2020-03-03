# -*- coding: utf-8 -*-

import math
from Priority_Queue import Priority_Queue
from Moves import check_move_up, check_move_down, check_move_left, check_move_right, blank_tile_up, blank_tile_down, blank_tile_left, blank_tile_right
N_Board = 8
MATRIX_SIZE = int(math.sqrt(N_Board+1))
number_of_nodes = 0

#Definitions for the Board class
class Board(object):
    def __init__(self, initial_state=None):
            self.initial_state = initial_state
            self.explored = []
            self.path=[]
#get initial state
    def get_initial_state(self):
            return self.initial_state
#print initial state
    def print_initial_state(self):
            print_state(self.initial_state)
#test if goal
    def test_if_goal(self, node, move):
            self.explored.append(node)
            self.path.append(move)
            return node == self.goal_state  
#get length of explored nodes          
    def get_explored_length(self):
            return len(self.explored)
#check if explored
    def is_explored(self, node):
            return node in self.explored
#get goal state
    def get_goal_state(self,goal_state=None):
            self.goal_state=goal
            return self.goal_state 

            
#misplaced tile heuristic 
def misplaced_tile(nodes, new_nodes):
    while not new_nodes.empty():
            node = new_nodes.get_child()
            nodes.insert_element(node[3], h_misplaced_tiles(node[3]), node[2], h_misplaced_tiles(node[3]) + node[2],node[4])
    print ("\n")
    
#manhattan distance heuristic
def manhattan_distance(nodes, new_nodes):
    while not new_nodes.empty():
            node = new_nodes.get_child()
            nodes.insert_element(node[3], h_manhattan_distance(node[3]), node[2], h_manhattan_distance(node[3]) + node[2],node[4])
    print ("\n")
    
#Calculating the h of misplaced tiles 
def h_misplaced_tiles(node):
    count = 0
    h = Board.get_goal_state()
    for i in range(N_Board+1):
            if node[i] == 0:
                continue
            if h[i] != node[i]:
                    count += 1
    return count

#Calculating the h of manhattan distance 
def h_manhattan_distance(node):
    count = 0
    h = Board.get_goal_state()
    for i in range(N_Board+1):
            if i == 0:
                continue
            hindex = h.index(i)
            index = node.index(i)
            row_difference = abs((hindex / MATRIX_SIZE) - (index / MATRIX_SIZE))
            column_difference = abs((hindex % MATRIX_SIZE) - (index % MATRIX_SIZE))
            count += (row_difference + column_difference)
    return count




#Main search strategy
def select_strategy(Board, heuristic_func):
    depth = 0
    nodes = Priority_Queue()
    nodes.insert_element(Board.get_initial_state())
    while not nodes.empty():
            total_node = nodes.get_child()
            node = total_node[3]
            move = total_node[4]
            if (total_node[2] or total_node[1]):
                    print ("The next best state to expand is with g(n) = %d and h(n) = %d " % (total_node[2], total_node[1]),)
            print_state(node)
            if Board.test_if_goal(node,move):
                    print ("We reached goal state")
                    print("The goal path is \n")
                    for p in Board.path:
                        print(p,end="->")
                    print ("\nTotal number of nodes expanded are %d ." % Board.get_explored_length())
                    print ("The number of unexpanded nodes are %d."% nodes.get_rem_elements())
                    print ("The depth of the goal node is %d." % total_node[2])
                    return None
            print ("After expanding this \n")
            print ("||\n")
            print ("\/\n")
            heuristic_func(nodes, expansion(total_node, Board))
            depth += 1


#All the possible nodes are generated and added to priority queue if not explored
def expansion(node, Board):
    possible_child_nodes = Priority_Queue()
    node1 = blank_tile_up(node[3][:], MATRIX_SIZE)
    node2 = blank_tile_down(node[3][:], MATRIX_SIZE, N_Board)
    node3 = blank_tile_left(node[3][:], MATRIX_SIZE)
    node4 = blank_tile_right(node[3][:], MATRIX_SIZE)
    if node1 and not Board.is_explored(node1):
            possible_child_nodes.insert_element(node1, 0, node[2] + 1, 0,'u')
    if node2 and not Board.is_explored(node2):
            possible_child_nodes.insert_element(node2, 0, node[2] + 1, 0,'d')
    if node3 and not Board.is_explored(node3):
            possible_child_nodes.insert_element(node3, 0, node[2] + 1, 0,'l')
    if node4 and not Board.is_explored(node4):
            possible_child_nodes.insert_element(node4, 0, node[2] + 1, 0,'r')
    global number_of_nodes
    number_of_nodes = number_of_nodes + len(possible_child_nodes.elements)
    return possible_child_nodes

    
#Print the current state in the Board solving
def print_state(mat_input):
    print ("-" * 6 * MATRIX_SIZE)
    for index, val in enumerate(mat_input):
            if (index + 1) % MATRIX_SIZE == 0:
                    print (val if val != 0 else "0", end="\n")
            else:
                    print (val if val != 0 else "0", " ", end=" ")
    print ("-" * 6 * MATRIX_SIZE)
            

#Logic where initial state and goal state are given and search strategy is defined for 8 Board program
if __name__ == "__main__":
    print ("*****Welcome to 8 Puzzle Solver*****")
    mat_input = []
    print ("Enter elements for %d Board." % N_Board)
    print ("NOTE: Use \"0\" for blank.\n")
    for i in range(9):
            print ("Enter element %d:" % (i + 1))
            mat_input.extend([int(x) for x in input()])
    goal = []
    print ("Enter goal state elements for %d Board." % N_Board)
    print ("NOTE: Use \"0\" for blank.\n")
    for i in range(9):
            print ("Enter element %d:" % (i + 1))
            goal.extend([int(x) for x in input()])
    Board = Board(mat_input)
    print ("Initial State",)
    Board.print_initial_state()
    print ("Goal State",)
    print_state(Board.get_goal_state())
    print ("\n\n")
    print ("Enter algorithm:\n1. A* with the Misplaced Tile heuristic.\n2. A* with the Manhattan distance heuristic.")
    yourchoice = int(input())
    t1 = 0
    if yourchoice == 1:
            select_strategy(Board, misplaced_tile)
    elif yourchoice == 2:
            select_strategy(Board, manhattan_distance)
    else:
            print ("Invalid choice.")
    print ("The algorithm has generated %d nodes in total including goal state." % number_of_nodes)
    
