# PyGame Collison Detection Practice, Jermaine Jeffcoat, Januaryv 04, 2022, 2:26pm, v0.3

import pygame, sys, random 
from pygame.locals import *

# Setup PyGame 
pygame.init()
mainClock = pygame.time.Clock() 

# Setup the PyGame Window
WINDOWWIDTH = 400 
WINDOWHEIGHT = 400
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGH), 0, 32)
pygame.display.set_caption('Collision Detection 2022')

# Setup colors. 
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

