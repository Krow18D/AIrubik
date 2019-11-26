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
glo_cost = 0
patt = ['R','R\'','L','L\'','U','U\'','D','D\'','F','F\'','B','B\'']


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
    cost = 0
    parent = None
    move = None


# checks if goal reached. if reached writes goal state in output.txt
def goal_reached(cube):
    for ref in [0, 3, 6, 9, 12, 15]:
        first = cube[ref, 0]
        for i in range(3):
            for j in range(3):
                if first != cube[ref + i, j]:
                    return False

    # goal reached
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


def idfs(start):
    cost_limit = 6
    nodes = 0
    frontier = list()
    branching_factors = list()

    while True:
        frontier.append(start)

        while len(frontier) != 0:
            curr = frontier.pop()
            # print("xxx")
            if goal_reached(curr.cube):
                print('Goal Height:', curr.cost)
                print("Nodes Generated:", nodes)
                return curr.cost,nodes

            if curr.cost + 1 <= cost_limit:
                child_cost = curr.cost + 1
                b = 0
                for i in range(12):
                    nodes = nodes + 1
                    new = State()
                    new.cube = np.array(curr.cube)
                    new.cost = child_cost
                    new.parent = curr
                    new.move = make_move(new.cube, i + 1, 0)
                    # if curr.parent is not None and np.array_equal(curr.parent.cube, new.cube):
                    if curr.parent is not None and (contains1(new.cube, curr) or contains2(new.cube, frontier)):
                        continue
                    frontier.append(new)
                    b = b + 1
                branching_factors.append(b)

        branching_factors.clear()

##########################################

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
        print("DLS ite : ",ite)
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

        glo_cost,glo_node = idfs(curr)

        time.ctime()
        end = time.strftime(fmt)
        print("Time taken(sec):", datetime.strptime(end, fmt) - datetime.strptime(start, fmt))
        #write txt
        with open('dataDLS.txt','a') as f:
            #depth,time,node
            f.write(''.join(str(glo_cost)+','+str(glo_time)+','+str(glo_node)+'\n'))    
    ls = []
    usedto = []