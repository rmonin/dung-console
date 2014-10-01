import pygame
from pygame.locals import *

def launch():

    pygame.init()

    fenetre = pygame.display.set_mode((640, 480))

    continuer = True

    while continuer:
        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    continuer = False

if __name__=="__main__":
    launch()
