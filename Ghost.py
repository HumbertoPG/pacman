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

    def draw(self, texture, id):
        
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture[id])
        
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_QUADS)
        
        half_size = self.size / 2
        
        glTexCoord2f(0.0, 0.0)
        glVertex3f(self.x - half_size, self.y - half_size, self.z)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(self.x + half_size, self.y - half_size, self.z)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(self.x + half_size, self.y + half_size, self.z)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(self.x - half_size, self.y + half_size, self.z)
        
        glEnd()
        glDisable(GL_TEXTURE_2D)

    
    def update(self, pX, pY):

        if (self.x == pX and self.y == pY):
            print("Game Over")
            return
        
        if (control.px_X[(self.x)] != -1 and control.px_Y[(self.y)] != -1):
            
                if (control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]] < 10):
                    
                    if (self.type == 0):

                        tmp = random.choice(control.directions[control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]]])
                        
                        while tmp == (self.currentDirection * -1):
                            tmp = random.choice(control.directions[control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]]])
                        
                        self.currentDirection = tmp
                    
                    else:

                        if (abs(self.x - pX) > 2 or abs(self.y - pY)):

                            moves = []
                            
                            moves = control.finding((self.x - 25, self.y - 25), (pX - 25, pY - 25))
                            
                            print(pX, pY)
                            
                            if (moves[1].x + 25 > self.x):
                                self.currentDirection = -2
                            elif (moves[1].x + 25 < self.x):
                                self.currentDirection = 2
                            elif (moves[1].y + 25 > self.y):
                                self.currentDirection = -1
                            elif (moves[1].y + 25 < self.y):
                                self.currentDirection = 1
        
        if (self.currentDirection == 1):
            self.y -= 1
        elif (self.currentDirection == -1):
            self.y += 1
        elif (self.currentDirection == 2):
            self.x -= 1
        elif (self.currentDirection == -2):
            self.x += 1
            
            
    
    
    
