import pygame
from pygame.locals import *

import conf

def launch():

    pygame.init()

    if conf.fullscreen:
        window = pygame.display.set_mode((800, 600), FULLSCREEN)
    else:
        window = pygame.display.set_mode((800, 600))

    # hide cursor
    pygame.mouse.set_visible(False)

    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                loop = False

if __name__=="__main__":
    launch()
