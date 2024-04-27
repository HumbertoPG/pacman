import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Control import Control

control = Control()

class Pacman:
    
    def __init__(self, size):

        self.size = size
        self.x = 25
        self.y = 25
        self.z = -1
        
        self.currentDirection = 0

    def draw(self):
        
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_QUADS)
        
        half_size = self.size / 2
        glVertex3f(self.x - half_size, self.y - half_size, self.z)
        glVertex3f(self.x + half_size, self.y - half_size, self.z)
        glVertex3f(self.x + half_size, self.y + half_size, self.z)
        glVertex3f(self.x - half_size, self.y + half_size, self.z)
        
        glEnd()
    
    def update(self):
        
        keys = pygame.key.get_pressed()
        if (control.px_X[(self.x)] != -1 and control.px_Y[(self.y)] != -1):

            if keys[pygame.K_RIGHT] and (-2 in control.directions[control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]]]):
                self.currentDirection = -2
            elif keys[pygame.K_DOWN] and (-1 in control.directions[control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]]]):
                self.currentDirection = -1
            elif keys[pygame.K_UP] and (1 in control.directions[control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]]]):
                self.currentDirection = 1
            elif keys[pygame.K_LEFT] and (2 in control.directions[control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]]]):
                self.currentDirection = 2

        if (control.px_X[(self.x)] != -1 and control.px_Y[(self.y)] != -1):
            if ((self.currentDirection in control.directions[control.intersections[control.px_Y[(self.y)]][control.px_X[(self.x)]]]) == False):
                self.currentDirection = 0

        if (self.currentDirection == 1):
            self.y -= 1
        elif (self.currentDirection == -1):
            self.y += 1
        elif (self.currentDirection == 2):
            self.x -= 1
        elif (self.currentDirection == -2):
            self.x += 1
