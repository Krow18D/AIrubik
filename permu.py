from itertools import permutations
from cube import *
import random
import math
usedto = []
ls = []
patt = ['R','R\'','L','L\'','U','U\'','D','D\'','F','F\'','B','B\'']


corners = [Corner(0, 0, 'ryb'), Corner(1, 0, 'rgy'), Corner(2, 0, 'rwg'), Corner(3, 0, 'rbw'), Corner(4, 0, 'owb'), Corner(5, 0, 'ogw'), Corner(6, 0, 'oyg'), Corner(7, 0, 'oby')]
edges = [Edge(0, 0, 'ry'), Edge(1, 0, 'rg'), Edge(2, 0, 'rw'), Edge(3, 0, 'rb'), Edge(4, 0, 'yb'), Edge(5, 0, 'wb'), Edge(6, 0, 'wg'), Edge(7, 0, 'yg'), Edge(8, 0, 'ow'), Edge(9, 0, 'og'), Edge(10, 0, 'oy'), Edge(11, 0, 'ob')]
centers = [Center(0, 'r'), Center(1, 'b'), Center(2, 'w'), Center(3, 'g'), Center(4, 'y'), Center(5, 'o')]
current_cube = Cube()
current_cube.cos = deepcopy(corners)
current_cube.eds = deepcopy(edges)
current_cube.ces = deepcopy(centers)

goal_cube = deepcopy(current_cube)





for i in range(3,4):
    print("i = ",i)
    scram = permutations(patt,i)    
    for el in scram:
        #print(el)
        temp = ' '.join(el)
        ls.append(temp)
    if i > 1:
        for count in range(100):
            x = random.randint(1,math.factorial(12)/(math.factorial(12-i)))        
            while x  in usedto:
                x = random.randint(1,math.factorial(12)/(math.factorial(12-i)))       
            else :
                usedto.append(x)
            print(ls[x-1])
            current_cube.scramble(ls[x-1])
            current_cube.print_cube()
    else :
        for count in range(11):
            x = random.randint(1,math.factorial(12)/(math.factorial(12-i)))        
            while x  in usedto:
                x = random.randint(1,math.factorial(12)/(math.factorial(12-i)))       
            else :
                usedto.append(x)
            print(ls[x-1])
            current_cube.scramble(ls[x-1])
            current_cube.print_cube()

