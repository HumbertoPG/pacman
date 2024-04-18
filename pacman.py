import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Pacman:
    
    def __init__(self, size, boardSize):
        
        self.DimBoard = boardSize
        self.size = size
        self.x = 21
        self.y = 21
        self.z = -1

    def draw(self):
        
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_QUADS)
        # Front face
        glVertex3f(self.x, self.y, self.z)
        glVertex3f(self.x + self.size, self.y, self.z)
        glVertex3f(self.x + self.size, self.y + self.size, self.z)
        glVertex3f(self.x, self.y + self.size, self.z)
        # ... (definir las otras caras del cubo aquí) ...
        glEnd()
    
    def update(self):
        
        # ghost.x += 1  # Mueve el cubo en la dirección x
        # ghost.y += 1  # Mueve el cubo en la dirección y
        
        # self.x += 1  # Mueve el cubo en la dirección x
        # ghost.y += 1

        # Comprueba si el cubo ha alcanzado el borde del tablero
        # if self.x + self.size > self.DimBoard - 21 or self.y + self.size > self.DimBoard:
        #     self.x = self.DimBoard - self.size - 21  # Mantiene el cubo dentro del tablero
            # ghost.y = DimBoard - ghost.size  # Mantiene el cubo dentro del tablero
    
        keys = pygame.key.get_pressed()  # Obtiene el estado de todas las teclas
        if keys[pygame.K_RIGHT]:  # Comprueba si la tecla de flecha derecha está presionada
            self.x += 1
        elif keys[pygame.K_DOWN]:
            self.y += 1
        elif keys[pygame.K_UP]:
            self.y -= 1
        elif keys[pygame.K_LEFT]:
            self.x -= 1