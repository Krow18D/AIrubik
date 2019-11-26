
#! /usr/bin/env python3
from ascii_template import *
        
class Cube :
    def __init__(self):
        self.cos = []
        self.eds = []
        self.ces = []
    def append_corner(self, corner):
        self.cos.append(corner)
    def append_edge(self, edge):
        self.eds.append(edge)
    def append_center(self, center):
        self.ces.append(center)

    # For each piece in the cube cycle through the scramble updating the piece at each move
    def scramble(self, scramble):
        # Parse scramble
        scramble = scramble.split(' ')
        s = []
        for m in scramble:
            if not m == '':
                s.append(m)
                
        corners = deepcopy(self.cos)
        edges = deepcopy(self.eds)
        # Move corners
        for corner in corners:
            for move in s:
                if move.strip() == 'R':
                    corner.R()
                elif move.strip() == 'R\'':
                    corner.Rp()
                elif move.strip() == 'R2':
                    corner.R2()
                elif move.strip() == 'L':
                    corner.L()
                elif move.strip() == 'L\'':
                    corner.Lp()
                elif move.strip() == 'L2':
                    corner.L2()
                elif move.strip() == 'U':
                    corner.U()
                elif move.strip() == 'U\'':
                    corner.Up()
                elif move.strip() == 'U2':
                    corner.U2()
                elif move.strip() == 'D':
                    corner.D()
                elif move.strip() == 'D\'':
                    corner.Dp()
                elif move.strip() == 'D2':
                    corner.D2()
                elif move.strip() == 'F':
                    corner.F()
                elif move.strip() == 'F\'':
                    corner.Fp()
                elif move.strip() == 'F2':
                    corner.F2()
                elif move.strip() == 'B':
                    corner.B()
                elif move.strip() == 'B\'':
                    corner.Bp()
                elif move.strip() == 'B2':
                    corner.B2()
        # Move edges
        for edge in edges:
            for move in s:
                if move.strip() == 'R':
                    edge.R()
                elif move.strip() == 'R\'':
                    edge.Rp()
                elif move.strip() == 'R2':
                    edge.R2()
                elif move.strip() == 'L':
                    edge.L()
                elif move.strip() == 'L\'':
                    edge.Lp()
                elif move.strip() == 'L2':
                    edge.L2()
                elif move.strip() == 'U':
                    edge.U()
                elif move.strip() == 'U\'':
                    edge.Up()
                elif move.strip() == 'U2':
                    edge.U2()
                elif move.strip() == 'D':
                    edge.D()
                elif move.strip() == 'D\'':
                    edge.Dp()
                elif move.strip() == 'D2':
                    edge.D2()
                elif move.strip() == 'F':
                    edge.F()
                elif move.strip() == 'F\'':
                    edge.Fp()
                elif move.strip() == 'F2':
                    edge.F2()
                elif move.strip() == 'B':
                    edge.B()
                elif move.strip() == 'B\'':
                    edge.Bp()
                elif move.strip() == 'B2':
                    edge.B2()
        self.cos = deepcopy(corners)
        self.eds = deepcopy(edges)

    # Print the scrambled cube to the screen
    def print_cube(self):
        c = self.make_layout(self.cos, self.eds, self.ces)
        # print('              ___ ___ ___')
        # print('             |   |   |   |')
        # print('             |', c[0][0], '|', c[0][1], '|', c[0][2], '|')
        # print('             |___|___|___|')
        # print('             |   |   |   |')
        # print('             |', c[1][0], '|', c[1][1], '|', c[1][2], '|')
        # print('             |___|___|___|')
        # print('             |   |   |   |')
        # print('             |', c[2][0], '|', c[2][1], '|', c[2][2], '|')
        # print('             |___|___|___|')
        # print(' ___ ___ ___  ___ ___ ___  ___ ___ ___  ___ ___ ___')
        # print('|   |   |   ||   |   |   ||   |   |   ||   |   |   |')
        # print('|', c[3][0], '|', c[3][1], '|', c[3][2], '||', c[3][3], '|', c[3][4], '|', c[3][5], '||', c[3][6], '|', c[3][7], '|', c[3][8], '||', c[3][9], '|', c[3][10], '|', c[3][11], '|')
        # print('|___|___|___||___|___|___||___|___|___||___|___|___|')
        # print('|   |   |   ||   |   |   ||   |   |   ||   |   |   |')
        # print('|', c[4][0], '|', c[4][1], '|', c[4][2], '||', c[4][3], '|', c[4][4], '|', c[4][5], '||', c[4][6], '|', c[4][7], '|', c[4][8], '||', c[4][9], '|', c[4][10], '|', c[4][11], '|')
        # print('|___|___|___||___|___|___||___|___|___||___|___|___|')
        # print('|   |   |   ||   |   |   ||   |   |   ||   |   |   |')
        # print('|', c[5][0], '|', c[5][1], '|', c[5][2], '||', c[5][3], '|', c[5][4], '|', c[5][5], '||', c[5][6], '|', c[5][7], '|', c[5][8], '||', c[5][9], '|', c[5][10], '|', c[5][11], '|')
        # print('|___|___|___||___|___|___||___|___|___||___|___|___|')
        # print('              ___ ___ ___')
        # print('             |   |   |   |')
        # print('             |', c[6][0], '|', c[6][1], '|', c[6][2], '|')
        # print('             |___|___|___|')
        # print('             |   |   |   |')
        # print('             |', c[7][0], '|', c[7][1], '|', c[7][2], '|')
        # print('             |___|___|___|')
        # print('             |   |   |   |')
        # print('             |', c[8][0], '|', c[8][1], '|', c[8][2], '|')
        
        # print('             |___|___|___|')
        

        
        print('                    [\'',c[0][0],'\' \'',c[0][1],'\' \'',c[0][2],'\']')
        print('                    [\'', c[1][0], '\' \'', c[1][1], '\' \'', c[1][2], '\']')
        print('                    [\'', c[2][0], '\' \'', c[2][1], '\' \'', c[2][2], '\']')
        print('[\'', c[3][0], '\' \'', c[3][1], '\' \'', c[3][2], '\'] [\'', c[3][3], '\' \'', c[3][4], '\' \'', c[3][5], '\'] [\'', c[3][6], '\' \'', c[3][7], '\' \'', c[3][8], '\'] [\'', c[3][9], '\' \'', c[3][10], '\' \'', c[3][11], '\']')
        print('[\'', c[4][0], '\' \'', c[4][1], '\' \'', c[4][2], '\'] [\'', c[4][3], '\' \'', c[4][4], '\' \'', c[4][5], '\'] [\'', c[4][6], '\' \'', c[4][7], '\' \'', c[4][8], '\'] [\'', c[4][9], '\' \'', c[4][10], '\' \'', c[4][11], '\']')
        print('[\'', c[5][0], '\' \'', c[5][1], '\' \'', c[5][2], '\'] [\'', c[5][3], '\' \'', c[5][4], '\' \'', c[5][5], '\'] [\'', c[5][6], '\' \'', c[5][7], '\' \'', c[5][8], '\'] [\'', c[5][9], '\' \'', c[5][10], '\' \'', c[5][11], '\']')
        print('                    [\'', c[6][0], '\' \'', c[6][1], '\' \'', c[6][2], '\']')
        print('                    [\'', c[7][0], '\' \'', c[7][1], '\' \'', c[7][2], '\']')
        print('                    [\'', c[8][0], '\' \'', c[8][1], '\' \'', c[8][2], '\']')
        with open('D:/Work/3D/1/ai/final/Rubiks-Cube-Solver/input.txt','w') as f:
            f.write(''.join('              [\''+str(c[0][0])+'\' \''+str(c[0][1])+'\' \''+str(c[0][2])+'\']\n              [\''+ str(c[1][0])+ '\' \''+ str(c[1][1])+ '\' \''+ str(c[1][2])+ '\']\n              [\''+ str(c[2][0])+ '\' \''+ str(c[2][1])+ '\' \''+ str(c[2][2])+ '\']\n[\''+ str(c[3][0])+ '\' \''+ str(c[3][1])+ '\' \''+ str(c[3][2])+ '\'] [\''+ str(c[3][3])+ '\' \''+ str(c[3][4])+ '\' \''+ str(c[3][5])+ '\'] [\''+ str(c[3][6])+ '\' \''+ str(c[3][7])+ '\' \''+ str(c[3][8])+ '\'] [\''+ str(c[3][9])+ '\' \''+ str(c[3][10])+ '\' \''+ str(c[3][11])+ '\']\n[\''+ str(c[4][0])+ '\' \''+ str(c[4][1])+ '\' \''+ str(c[4][2])+ '\'] [\''+ str(c[4][3])+ '\' \''+ str(c[4][4])+ '\' \''+ str(c[4][5])+ '\'] [\''+ str(c[4][6])+ '\' \''+ str(c[4][7])+ '\' \''+ str(c[4][8])+ '\'] [\''+ str(c[4][9])+ '\' \''+ str(c[4][10])+ '\' \''+ str(c[4][11])+ '\']\n[\''+ str(c[5][0])+ '\' \''+ str(c[5][1])+ '\' \''+ str(c[5][2])+ '\'] [\''+ str(c[5][3])+ '\' \''+ str(c[5][4])+ '\' \''+ str(c[5][5])+ '\'] [\''+ str(c[5][6])+ '\' \''+ str(c[5][7])+ '\' \''+ str(c[5][8])+ '\'] [\''+ str(c[5][9])+ '\' \''+ str(c[5][10])+ '\' \''+ str(c[5][11])+ '\']\n              [\''+ str(c[6][0])+ '\' \''+ str(c[6][1])+ '\' \''+ str(c[6][2])+ '\']\n              [\''+ str(c[7][0])+ '\' \''+ str(c[7][1])+ '\' \''+ str(c[7][2])+ '\']\n              [\''+ str(c[8][0])+ '\' \''+ str(c[8][1])+ '\' \''+ str(c[8][2])+ '\']'))
        
    # Using the scrambled pieces, fit the colours to an array based on location in the template
    def make_layout(self, Corners, Edges, Centers):
        c = [[],[],[],[],[],[],[],[]]
        e = [[],[],[],[],[],[],[],[],[],[],[],[]]
        for corner in Corners:
            if corner.o == 0:
                c[corner.p] = corner.c
            elif corner.o == 1:
                c[corner.p] = corner.c[1:] + corner.c[0]
            else:
                c[corner.p] = corner.c[2] + corner.c[:2]
        for edge in Edges:
            if edge.o == 0:
                e[edge.p] = edge.c
            else:
                e[edge.p] = edge.c[1] + edge.c[0]
        layout = [[c[7][2], e[10][1], c[6][1]], [e[4][0], Centers[4].c, e[7][0]], [c[0][1], e[0][1], c[1][2]], [c[7][1], e[4][1], c[0][2], c[0][0], e[0][0], c[1][0], c[1][1], e[7][1], c[6][2], c[6][0], e[10][0], c[7][0]], [e[11][1], Centers[1].c, e[3][1], e[3][0], Centers[0].c, e[1][0], e[1][1], Centers[3].c, e[9][1], e[9][0], Centers[5].c, e[11][0]], [c[4][2], e[5][1], c[3][1], c[3][0], e[2][0], c[2][0], c[2][2], e[6][1], c[5][1], c[5][0], e[8][0], c[4][0]], [c[3][2], e[2][1], c[2][1]], [e[5][0], Centers[2].c, e[6][0]], [c[4][1], e[8][1], c[5][2]]]
        return layout
    
    def check_is_goal(self, goal_state):
        #check position and orientation
        #for i,j in zip(self.cos, goal_state.cos):
            #print(str(i.p) +":"+str(j.p))

        #check goal
        if (all(i.p == j.p for i,j in zip(goal_state.ces, self.ces)) and all(i.p == j.p and i.o == j.o for i,j in zip(goal_state.cos, self.cos)) and all(i.p == j.p and i.o == j.o for i,j in zip(goal_state.eds, self.eds))):
            return True
