import pygame
from pygame.locals import *

import conf

from menu import menu

def launch():

    pygame.init()
    clock = pygame.time.Clock()

    if conf.fullscreen:
        window = pygame.display.set_mode((800, 600), FULLSCREEN)
    else:
        window = pygame.display.set_mode((800, 600))

    # hide cursor
    pygame.mouse.set_visible(False)

    menu(window, clock)

if __name__=="__main__":
    launch()
