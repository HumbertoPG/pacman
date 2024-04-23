import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

directions = [[], [-1, -2], [-1, 2], [1, -2], [1, 2], [-1, 2, -2], [1, -1, 2], [1, 2, -2], [1, -1, -2], [1, -1, 2, -2]]

class Pacman:
    
    def __init__(self, size, boardSize):
        
        self.DimBoard = boardSize
        self.size = size
        self.x = 21
        self.y = 21
        self.z = -1
        
        self.currentDirection = 2

    def draw(self):
        
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_QUADS)
        
        glVertex3f(self.x, self.y, self.z)
        glVertex3f(self.x + self.size, self.y, self.z)
        glVertex3f(self.x + self.size, self.y + self.size, self.z)
        glVertex3f(self.x, self.y + self.size, self.z)
        
        glEnd()
    
    def update(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += 1
        elif keys[pygame.K_DOWN]:
            self.y += 1
        elif keys[pygame.K_UP]:
            self.y -= 1
        elif keys[pygame.K_LEFT]:
            self.x -= 1