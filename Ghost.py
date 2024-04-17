import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math
import numpy as np

class Ghost:
    
    def __init__(self, size, boardSize):
        
        self.DimBoard = boardSize
        self.size = size
        self.x = 26
        self.y = 546 - 520
        self.z = 0

    def draw(self):
        glBegin(GL_QUADS)
        # Front face
        glVertex3f(self.x, self.y, self.z + self.size)
        glVertex3f(self.x + self.size, self.y, self.z + self.size)
        glVertex3f(self.x + self.size, self.y + self.size, self.z + self.size)
        glVertex3f(self.x, self.y + self.size, self.z + self.size)
        # ... (definir las otras caras del cubo aquí) ...
        glEnd()
    
    def update(self):
        
        # ghost.x += 1  # Mueve el cubo en la dirección x
        # ghost.y += 1  # Mueve el cubo en la dirección y
        
        self.x += 1  # Mueve el cubo en la dirección x
        # ghost.y += 1

        # Comprueba si el cubo ha alcanzado el borde del tablero
        if self.x + self.size > self.DimBoard - 25 or self.y + self.size > self.DimBoard:
            self.x = self.DimBoard - self.size - 25  # Mantiene el cubo dentro del tablero
            # ghost.y = DimBoard - ghost.size  # Mantiene el cubo dentro del tablero
    
    
    
