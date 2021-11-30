# My First Pygame, Jermaine Jeffcoat, 11/30/21, 2:13pm, v0.2

import pygame, sys
from pygame.locals import *

# Start PyGame 
pygame.init()

# Setup the game window.
windowsurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')