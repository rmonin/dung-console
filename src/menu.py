import pygame
from pygame.locals import *

import conf
from arrow import Arrow

def menu(window, clock):

    arrow_right = Arrow("right", window.get_size())
    arrow_left = Arrow("left", window.get_size())

    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    loop = False
                if event.key == K_RIGHT:
                    print "right"
                    arrow_right.big = True
                if event.key == K_LEFT:
                    print "left"
                    arrow_left.big = True

        window.fill((30,130,184))
        arrow_right.draw(window)
        arrow_left.draw(window)
        pygame.display.flip()
        clock.tick(30)
