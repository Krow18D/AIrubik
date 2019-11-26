#! /usr/bin/env python3

"""
    Version:        1.0
    Date:           30.JUN.2019
    Author:         Robert Riordan
    Email:          robert.riordan@ucdconnect.ie
    
    Goal(s):        Output an unfolded ASCII template of Rubik's Cube with colour of each piece given scramble.
    
    Method:         1. Get an input scramble.
                    2. Set up position, orientation, and colour of corner, edge and center objects.
                    3. Deconstruct scramble into series of moves.
                    4. Perform the scramble on each piece.
                        4.1. Centers can be ignored.
                    5. Create array of colours based on the position and orientation of each piece.
                    6. Place each colour in the template.
    
    Dependncies:    sys
    
    Usage:          ./ascii_template.py "SCRAMBLE"
                    SCRAMBLE must be a single string of moves seperated by spaces.
"""
# Modules
import sys
from copy import deepcopy

# Get command line inputs
msg = "Only one scramble as a single string can be input"
assert(len(sys.argv) <= 2), msg


"""
    Class to represent a corner object
    
    Corner properties:  p - position of corner on cube (0 - 7)
                        o - orientation of corner (0 - 2)
                        c - colour of corner (3 characters)
                        
    Corner moves:       R, L, U, D, F, B    - Turn the Right, Left, Up, Down, Front, or Back face clockwise (90 degrees)
                                            - Cycle p for 4 corners in R, L, ... face
                                            - +/- to o for 4 corners in R, L, ... face if required
                                            - No change to c
                        Rp, Lp, ...         - Turn anticlockwise (-90 or 270 degrees)
                                            - Cycle p for 4 corners in R, L, ... face
                                            - +/- to o for 4 corners in R, L, ... face if required
                                            - No change to c
                        R2, L2, ...         - Turn 180 degrees
                                            - Swap opposite corners on R, L, ... face i.e. 2 cycles in p
                                            - No change to o or c
"""
class Corner:
    p = 0
    o = 0
    c = 'wrg'
    def __init__(self, position, orientation, colour):
        self.p = position
        self.o = orientation
        self.c = colour
    
    def R(self):        
        if self.p == 1:
            self.p = 6
            self.o = (self.o + 2)%3
        elif self.p == 2:
            self.p = 1
            self.o = (self.o + 1)%3
        elif self.p == 5:
            self.p = 2
            self.o = (self.o + 2)%3
        elif self.p == 6:
            self.p = 5
            self.o = (self.o + 1)%3
    
    def R2(self):
        self.R()
        self.R()
    
    def Rp(self):
        self.R2()
        self.R()
    
    def L(self):
        if self.p == 0:
            self.p = 3
            self.o = (self.o + 1)%3
        elif self.p == 3:
            self.p = 4
            self.o = (self.o + 2)%3
        elif self.p == 4:
            self.p = 7
            self.o = (self.o + 1)%3
        elif self.p == 7:
            self.p = 0
            self.o = (self.o + 2)%3        
    
    def L2(self):
        self.L()
        self.L()
    
    def Lp(self):
        self.L2()
        self.L()
        
    def F(self):
        if self.p == 0:
            self.p = 1
        elif self.p == 1:
            self.p = 2
        elif self.p == 2:
            self.p = 3
        elif self.p == 3:
            self.p = 0
    
    def F2(self):
        self.F()
        self.F()
    
    def Fp(self):
        self.F2()
        self.F()
    
    def B(self):
        if self.p == 4:
            self.p = 5
        elif self.p == 5:
            self.p = 6
        elif self.p == 6:
            self.p = 7
        elif self.p == 7:
            self.p = 4
    
    def B2(self):
        self.B()
        self.B()
    
    def Bp(self):
        self.B2()
        self.B()

    def D(self):
        if self.p == 2:
            self.p = 5
            self.o = (self.o + 2)%3
        elif self.p == 5:
            self.p = 4
            self.o = (self.o + 1)%3
        elif self.p == 4:
            self.p = 3
            self.o = (self.o + 2)%3
        elif self.p == 3:
            self.p = 2
            self.o = (self.o + 1)%3
    
    def D2(self):
        self.D()
        self.D()
    
    def Dp(self):
        self.D2()
        self.D()
    
    def U(self):
        if self.p == 0:
            self.p = 7
            self.o = (self.o + 2)%3
        elif self.p == 7:
            self.p = 6
            self.o = (self.o + 1)%3
        elif self.p == 6:
            self.p = 1
            self.o = (self.o + 2)%3
        elif self.p == 1:
            self.p = 0
            self.o = (self.o + 1)%3        
    
    def U2(self):
        self.U()
        self.U()
    
    def Up(self):
        self.U2()
        self.U()

"""
    Class to represent a center object
    
    Center properties:  p - position of center on cube (0 - 5)
                        c - colour of center (1 character)
"""
class Center:
    p = 0
    c = 'w'
    
    def __init__(self, position, colour):
        self.p = position
        self.c = colour

"""
    Class to represent a edge object
    
    Edge properties:    p - position of edge on cube (0 - 11)
                        o - orientation of edge (0 - 1)
                        c - colour of edge (2 characters)
                        
    Edge moves:         R, L, U, D, F, B    - Turn the Right, Left, Up, Down, Front, or Back face clockwise (90 degrees)
                                            - Cycle p for 4 edges in R, L, ... face
                                            - + to o for 4 edges in R, L, ... face if required
                                            - No change to c
                        Rp, Lp, ...         - Turn anticlockwise (-90 or 270 degrees)
                                            - Cycle p for 4 edges in R, L, ... face
                                            - +/- to o for 4 edges in R, L, ... face if required
                                            - No change to c
                        R2, L2, ...         - Turn 180 degrees
                                            - Swap opposite edges on R, L, ... face i.e. 2 cycles in p
                                            - No change to o or c
"""
class Edge:
    p = 0
    o = 0
    c = 'wb'
    
    def __init__(self, position, orientation, colour):
        self.p = position
        self.o = orientation
        self.c = colour
        
    def R(self):
        if self.p == 1:
            self.p = 7
        elif self.p == 6:
            self.p = 1
        elif self.p == 9:
            self.p = 6
        elif self.p == 7:
            self.p = 9
    
    def R2(self):
        self.R()
        self.R()
        
    def Rp(self):
        self.R2()
        self.R()

    def L(self):
        if self.p == 3:
            self.p = 5
        elif self.p == 5:
            self.p = 11
        elif self.p == 11:
            self.p = 4
        elif self.p == 4:
            self.p = 3
    
    def L2(self):
        self.L()
        self.L()
        
    def Lp(self):
        self.L2()
        self.L()

    def F(self):
        if self.p == 0:
            self.p = 1
        elif self.p == 1:
            self.p = 2
        elif self.p == 2:
            self.p = 3
        elif self.p == 3:
            self.p = 0
    
    def F2(self):
        self.F()
        self.F()
        
    def Fp(self):
        self.F2()
        self.F()

    def B(self):
        if self.p == 8:
            self.p = 9
        elif self.p == 9:
            self.p = 10
        elif self.p == 10:
            self.p = 11
        elif self.p == 11:
            self.p = 8
    
    def B2(self):
        self.B()
        self.B()
        
    def Bp(self):
        self.B2()
        self.B()
        
    def D(self):
        if self.p == 2:
            self.p = 6
            self.o = (self.o + 1)%2
        elif self.p == 6:
            self.p = 8
            self.o = (self.o + 1)%2
        elif self.p == 8:
            self.p = 5
            self.o = (self.o + 1)%2
        elif self.p == 5:
            self.p = 2
            self.o = (self.o + 1)%2
    
    def D2(self):
        self.D()
        self.D()
        
    def Dp(self):
        self.D2()
        self.D()

    def U(self):
        if self.p == 0:
            self.p = 4
            self.o = (self.o + 1)%2
        elif self.p == 4:
            self.p = 10
            self.o = (self.o + 1)%2
        elif self.p == 10:
            self.p = 7
            self.o = (self.o + 1)%2
        elif self.p == 7:
            self.p = 0
            self.o = (self.o + 1)%2
    
    def U2(self):
        self.U()
        self.U()
        
    def Up(self):
        self.U2()
        self.U()
        
