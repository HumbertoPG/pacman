from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random

from Control import Control

control = Control()

class Ghost:
    
    def __init__(self, size, type):
        
        self.type = type
        self.size = size
        self.x = 25
        self.y = 520
        self.z = -1
        
        self.currentDirection = -2

    def draw(self):
        
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_QUADS)
        
        half_size = self.size / 2
        glVertex3f(self.x - half_size, self.y - half_size, self.z)
        glVertex3f(self.x + half_size, self.y - half_size, self.z)
        glVertex3f(self.x + half_size, self.y + half_size, self.z)
        glVertex3f(self.x - half_size, self.y + half_size, self.z)
        
        glEnd()

    
    def update(self, pX, pY):
        
        if (control.px_X[(self.x)] != -1 and control.px_Y[(self.y)] != -1):
            
                if (control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]] < 10):
                    
                    if (self.type == 0):

                        tmp = random.choice(control.directions[control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]]])
                        
                        while tmp == (self.currentDirection * -1):
                            tmp = random.choice(control.directions[control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]]])
                        
                        self.currentDirection = tmp
                    
                    else:

                        moves = control.finding((self.x - 25, self.y - 26), (pX - 25, pY - 25))
                        
                        print("Path: ")

                        for i in range(0, 10):
                            print(moves[i].x, moves[i].y)
                        
                        if (moves[1].x + 25 > self.x):
                            self.currentDirection = -2
                        elif (moves[1].x + 25 < self.x):
                            self.currentDirection = 2
                        elif (moves[1].y + 26 > self.y):
                            self.currentDirection = -1
                        elif (moves[1].y + 26 < self.y):
                            self.currentDirection = 1
        
        if (self.currentDirection == 1):
            self.y -= 1
        elif (self.currentDirection == -1):
            self.y += 1
        elif (self.currentDirection == 2):
            self.x -= 1
        elif (self.currentDirection == -2):
            self.x += 1
            
            
    
    
    
