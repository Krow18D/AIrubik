from ScrambleRubixcube import xInitial, make_move
import numpy as np
from datetime import datetime
import time
import sys
from cube import *
import random
import math
from itertools import permutations
usedto = []
ls = []
glo_node = 0
glo_depth = 0
glo_time = 0
patt = ['R','R\'','L','L\'','U','U\'','D','D\'','F','F\'','B','B\'']

array = np.array([
    [[0, 0, 2], [1, 0, 2], [2, 0, 2]],
    [[0, 0, 1], [1, 0, 1], [2, 0, 1]],
    [[0, 0, 0], [1, 0, 0], [2, 0, 0]],

    [[0, 0, 2], [0, 0, 1], [0, 0, 0]],
    [[0, 1, 2], [0, 1, 1], [0, 1, 0]],
    [[0, 2, 2], [0, 2, 1], [0, 2, 0]],

    [[0, 0, 0], [1, 0, 0], [2, 0, 0]],
    [[0, 1, 0], [1, 1, 0], [2, 1, 0]],
    [[0, 2, 0], [1, 2, 0], [2, 2, 0]],

    [[2, 0, 0], [2, 0, 1], [2, 0, 2]],
    [[2, 1, 0], [2, 1, 1], [2, 1, 2]],
    [[2, 2, 0], [2, 2, 1], [2, 2, 2]],

    [[2, 0, 2], [1, 0, 2], [0, 0, 2]],
    [[2, 1, 2], [1, 1, 2], [0, 1, 2]],
    [[2, 2, 2], [1, 2, 2], [0, 2, 2]],
    
    [[0, 2, 0], [1, 2, 0], [2, 2, 0]],
    [[0, 2, 1], [1, 2, 1], [2, 2, 1]],
    [[0, 2, 2], [1, 2, 2], [2, 2, 2]],
])


# Initialise pieces
corners = [Corner(0, 0, 'ryb'), Corner(1, 0, 'rgy'), Corner(2, 0, 'rwg'), Corner(3, 0, 'rbw'), Corner(4, 0, 'owb'), Corner(5, 0, 'ogw'), Corner(6, 0, 'oyg'), Corner(7, 0, 'oby')]
edges = [Edge(0, 0, 'ry'), Edge(1, 0, 'rg'), Edge(2, 0, 'rw'), Edge(3, 0, 'rb'), Edge(4, 0, 'yb'), Edge(5, 0, 'wb'), Edge(6, 0, 'wg'), Edge(7, 0, 'yg'), Edge(8, 0, 'ow'), Edge(9, 0, 'og'), Edge(10, 0, 'oy'), Edge(11, 0, 'ob')]
centers = [Center(0, 'r'), Center(1, 'b'), Center(2, 'w'), Center(3, 'g'), Center(4, 'y'), Center(5, 'o')]
current_cube = Cube()
current_cube.cos = deepcopy(corners)
current_cube.eds = deepcopy(edges)
current_cube.ces = deepcopy(centers)

goal_cube = deepcopy(current_cube)

class State:
    cube = None
    g = 0
    h = 0
    parent = None
    move = None


# checks if goal reached. if reached writes goal state in output.txt
def goal_reached(curr):
    if curr.h != 0:
        return False

    # goal reached
    cube = curr.cube
    file = open('output.txt', 'w')
    file.write("              " + str(cube[0, 0:3]) + '\n')
    file.write("              " + str(cube[1, 0:3]) + '\n')
    file.write("              " + str(cube[2, 0:3]) + '\n')
    file.write(str(cube[3, 0:3]) + ' ' + str(cube[6, 0:3]) + ' ' + str(cube[9, 0:3]) + ' ' + str(cube[12, 0:3]) + '\n')
    file.write(str(cube[4, 0:3]) + ' ' + str(cube[7, 0:3]) + ' ' + str(cube[10, 0:3]) + ' ' + str(cube[13, 0:3]) + '\n')
    file.write(str(cube[5, 0:3]) + ' ' + str(cube[8, 0:3]) + ' ' + str(cube[11, 0:3]) + ' ' + str(cube[14, 0:3]) + '\n')
    file.write("              " + str(cube[15, 0:3]) + '\n')
    file.write("              " + str(cube[16, 0:3]) + '\n')
    file.write("              " + str(cube[17, 0:3]) + '\n')

    return True


# checks if child ascendant of parent
def contains1(child, parent):
    curr = parent.parent
    while curr is not None:
        if np.array_equal(curr.cube, child): return True
        curr = curr.parent

    return False


# checks if frontier contains child
def contains2(child, frontier):
    for curr in frontier:
        if np.array_equal(curr.cube, child): return True

    return False


def ida(start):
    start.h = corner_edge_sum_max(start.cube)
    cost_limit = start.h
    nodes = 0
    frontier = list()
    branching_factors = list()

    while True:
        minimum = None
        frontier.append(start)

        while len(frontier) != 0:
            curr = frontier.pop(\
                    [i.g + i.h for i in frontier].index(\
                    min([i.g+i.h for i in frontier])\
                    ))

            if goal_reached(curr):
                print('Goal Height:', curr.g)
                #print('Branching Factor:', sum(branching_factors)/len(branching_factors))
                # while curr is not None:
                #    if curr.move is not None:
                #        print(curr.move)
                #    curr = curr.parent

                #print("mem ",nodes.__sizeof__)
                print("Nodes Generated:", nodes)
                
                return curr.g,nodes

            b = 0
            nodes = nodes + 12
            for i in range(12):
                new = State()
                new.cube = np.array(curr.cube)
                new.g = curr.g + 1
                new.parent = curr
                new.move = make_move(new.cube, i + 1, 0)
                new.h = corner_edge_sum_max(new.cube)

                if new.g + new.h > cost_limit:
                    if minimum is None or new.g + new.h < minimum:
                        minimum = new.g + new.h
                    continue
                if curr.parent is not None and (contains1(new.cube, curr) or contains2(new.cube, frontier)):
                    continue
                frontier.append(new)
                b = b + 1
            if b != 0:
                branching_factors.append(b)

        cost_limit = minimum
     

def manhattan_distance(cube, i, z, corner):
    c1 = array[i, z]
    center = None
    for c in [1, 4, 7, 10, 13, 16]:
        if cube[i, z] == cube[c, 1]:
            center = c
            break

    if corner:
        c2 = array[center - 1, 0]
        d1 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[center - 1, 2]
        d2 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[center + 1, 0]
        d3 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[center + 1, 2]
        d4 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        return min(d1, d2, d3, d4)
    else:
        c2 = array[center - 1, 1]
        d1 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[center, 0]
        d2 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[center, 2]
        d3 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[center + 1, 1]
        d4 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        return min(d1, d2, d3, d4)


def corner_edge_sum_max(cube):
    corners = 0
    edges = 0
    for i in range(18):
        if i % 3 == 0 or i % 3 == 2:
            corners = corners + manhattan_distance(cube, i, 0, True) + manhattan_distance(cube, i, 2, True)
            edges = edges + manhattan_distance(cube, i, 1, False)
        else:
            edges = edges + manhattan_distance(cube, i, 0, False) + manhattan_distance(cube, i, 2, False)
    return max(corners / 12, edges / 8)


##########################################

#set in loop

#handle = open('input.txt')

for Are in range(1,7):
    curr = State()
    curr.cube = np.array(xInitial)
    print("r = ",Are)
    scram = permutations(patt,Are)    
    for el in scram:
        #print(el)
        temp = ' '.join(el)
        ls.append(temp)
    if Are > 1:
        for _ in range(100):
            x = random.randint(1,math.factorial(12)/(math.factorial(12-Are)))        
            while x  in usedto:
                x = random.randint(1,math.factorial(12)/(math.factorial(12-Are)))       
            else :
                usedto.append(x)
            # current_cube.scramble(ls[x-1])
            # current_cube.print_cube()
    else :
        for _ in range(11):
            x = random.randint(1,math.factorial(12)/(math.factorial(12-Are)))        
            while x  in usedto:
                x = random.randint(1,math.factorial(12)/(math.factorial(12-Are)))       
            else :
                usedto.append(x)
    ite = 1
    for runnum in usedto:
        print("A* ite : ",ite)
        ite += 1
        print("pattern : ",ls[runnum-1])
        current_cube = Cube()
        current_cube.cos = deepcopy(corners)
        current_cube.eds = deepcopy(edges)
        current_cube.ces = deepcopy(centers)
        current_cube.scramble(ls[runnum-1])
        current_cube.print_cube()
        handle = open('input.txt')
        indexes = [0, 1, 2, 3, 6, 9, 12, 4, 7, 10, 13, 5, 8, 11, 14, 15, 16, 17]
        index = 0
        for line in handle:
            line = line.replace(' ', '')
            for row in line.split('['):
                if len(row) != 0:
                    i = indexes[index]
                    curr.cube[i, 0] = row[1]
                    curr.cube[i, 1] = row[4]
                    curr.cube[i, 2] = row[7]
                    index = index + 1

        time.ctime()
        fmt = '%H:%M:%S'
        start = time.strftime(fmt)

        glo_depth,glo_node=ida(curr)

        time.ctime()
        end = time.strftime(fmt)
        glo_time = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
        print("Time taken(sec):", datetime.strptime(end, fmt) - datetime.strptime(start, fmt))
        #write txt
        with open('dataAS.txt','a') as f:
            #depth,time,node
            f.write(''.join(str(glo_depth)+','+str(glo_time)+','+str(glo_node)+'\n'))    
    ls = []
    usedto = []
