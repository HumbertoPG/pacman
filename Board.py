import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import sys
sys.path.append('..')

from Pacman import Pacman
from Ghost import Ghost

screen_width = 546
screen_height = 546

FOVY = 55.0
ZNEAR = 0.1
ZFAR = 1000.0

DimBoard = 546
textures = []
filename1 = "board.png"

X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500
Z_MIN=-500
Z_MAX=500

pygame.init()

def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(X_MIN,0.0,0.0)
    glVertex3f(X_MAX,0.0,0.0)
    glEnd()
    #Y axis in green
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,Y_MIN,0.0)
    glVertex3f(0.0,Y_MAX,0.0)
    glEnd()
    #Z axis in blue
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,Z_MIN)
    glVertex3f(0.0,0.0,Z_MAX)
    glEnd()
    glLineWidth(1.0)

def Texturas(filepath):
    textures.append(glGenTextures(1))
    id = len(textures) - 1
    glBindTexture(GL_TEXTURE_2D, textures[id])
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    image = pygame.image.load(filepath).convert()
    w, h = image.get_rect().size
    image_data = pygame.image.tostring(image,"RGBA")
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D) 

def Init():
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: Pacman")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(DimBoard/2, DimBoard/2, -DimBoard,  # Posición de la cámara
          DimBoard/2, DimBoard/2, 0,  # Punto al que la cámara está mirando
          0, -1, 0) 

    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    Texturas(filename1)
    
def PlanoTexturizado():
    #Activate textures
    # glColor3f(1.0,1.0,1.0)
    # glEnable(GL_TEXTURE_2D)
    # #front face
    # glBindTexture(GL_TEXTURE_2D, textures[0])    
    # glBegin(GL_QUADS)
    # glTexCoord2f(0.0, 1.0)  # Cambiado a (0.0, 1.0)
    # glVertex3d(0, 0, 0) # Esquina inferior izquierda
    # glTexCoord2f(1.0, 1.0)  # Cambiado a (1.0, 1.0)
    # glVertex3d(DimBoard, 0, 0)  # Esquina inferior derecha
    # glTexCoord2f(1.0, 0.0)  # Cambiado a (1.0, 0.0)
    # glVertex3d(DimBoard, DimBoard, 0)  # Esquina superior derecha
    # glTexCoord2f(0.0, 0.0)  # Cambiado a (0.0, 0.0)
    # glVertex3d(0, DimBoard, 0)  # Esquina superior izquierda
    # glEnd()              
    # glDisable(GL_TEXTURE_2D)
    
    
    glColor3f(1, 1, 1)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textures[0])    
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)  # Cambiado a (1.0, 0.0)
    glVertex3d(0, 0, 0)
    glTexCoord2f(1.0, 1.0)  # Cambiado a (1.0, 1.0)
    glVertex3d(0, DimBoard, 0)
    glTexCoord2f(0.0, 1.0)  # Cambiado a (0.0, 1.0)
    glVertex3d(DimBoard, DimBoard, 0)
    glTexCoord2f(0.0, 0.0)  # Cambiado a (0.0, 0.0)
    glVertex3d(DimBoard, 0, 0)
    glEnd()              
    glDisable(GL_TEXTURE_2D)


pacman = Pacman(10, DimBoard)
ghost = Ghost(10, DimBoard)

def display():
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Axis()
    PlanoTexturizado()
    # pacman.draw()
    # pacman.update()
    
    ghost.draw()  # Dibuja el cubo
    ghost.update()

done = False
Init()
while not done:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True

    

    # pacman.x += 1
    display()
    

    pygame.display.flip()
    pygame.time.wait(5)

pygame.quit()