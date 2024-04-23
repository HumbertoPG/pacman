from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random

control = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 5, 0, 2, 1, 0, 5, 0, 2],
[0, 8, 0, 9, 5, 7, 7, 5, 9, 0, 6],
[0, 3, 0, 6, 3, 2, 1, 4, 8, 0, 4],
[0, 0, 0, 0, 1, 7, 7, 2, 0, 0, 0],
[0, 0, 0, 8, 6, 0, 0, 8, 6, 0, 0],
[0, 0, 0, 0, 8, 0, 0, 6, 0, 0, 0], 
[0, 1, 0, 9, 0, 2, 1, 0, 9, 0, 2],
[0, 3, 2, 8, 5, 7, 7, 5, 6, 1, 4],
[0, 1, 7, 4, 3, 2, 1, 4, 3, 7, 2],
[0, 3, 0, 0, 0, 7, 7, 0, 0, 0, 4]]

px_X = []

for i in range(0, 547):
    px_X.append(-1)

px_X[1] = 1
px_X[39] = 2
px_X[99] = 3
px_X[159] = 4
px_X[217] = 5
px_X[277] = 6
px_X[337] = 7
px_X[397] = 8
px_X[456] = 9
px_X[496] = 10

px_Y = []

for i in range(0, 547):
    px_Y.append(-1)

px_Y[1] = 1
px_Y[71] = 2
px_Y[124] = 3

px_Y[177] = 4
px_Y[230] = 5
px_Y[283] = 6

px_Y[336] = 7
px_Y[389] = 8
px_Y[442] = 9
px_Y[495] = 10

directions = [[], [-1, -2], [-1, 2], [1, -2], [1, 2], [-1, 2, -2], [1, -1, 2], [1, 2, -2], [1, -1, -2], [1, -1, 2, -2]]
#  1: UP
# -1: Down
#  2: Left
# -2: Rigth

class Ghost:
    
    def __init__(self, size, boardSize):
        
        self.DimBoard = boardSize
        self.size = size
        self.x = 21
        self.y = 21
        self.z = -1
        
        self.currentDirection = 2

    def draw(self):
        
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_QUADS)
        
        glVertex3f(self.x, self.y, self.z)
        glVertex3f(self.x + self.size, self.y, self.z)
        glVertex3f(self.x + self.size, self.y + self.size, self.z)
        glVertex3f(self.x, self.y + self.size, self.z)
        
        glEnd()

    
    def update(self):
        
        if (px_X[(self.x - 20)] != -1 and px_Y[(self.y - 20)] != -1):
            
            if (control[px_Y[(self.y - 20)]][px_X[(self.x - 20)]] != 0):
                
                tmp = random.choice(directions[control[px_Y[(self.y - 20)]][px_X[(self.x - 20)]]])
                
                while tmp == (self.currentDirection * -1):
                    tmp = random.choice(directions[control[px_Y[(self.y - 20)]][px_X[(self.x - 20)]]])
                
                self.currentDirection = tmp
        
        if (self.currentDirection == 1):
            self.y -= 1
        elif (self.currentDirection == -1):
            self.y += 1
        elif (self.currentDirection == 2):
            self.x -= 1
        elif (self.currentDirection == -2):
            self.x += 1
            
            
    
    
    
