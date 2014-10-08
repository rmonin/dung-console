import pygame
import pygame.gfxdraw

class Arrow(object):

    def __init__(self, orientation, screen_size):
        self.screen_x = screen_size[0]
        self.screen_y = screen_size[1]
        self.big = False
        self.orientation = orientation

        if orientation == "right":
            self.points = (
                ((self.screen_x/10)*9, self.screen_y/3),
                (self.screen_x-20, self.screen_y/2),
                ((self.screen_x/10)*9, (self.screen_y/3*2))
            )
        else:
            self.points = (
                (self.screen_x/10, self.screen_y/3),
                (20, self.screen_y/2),
                (self.screen_x/10, (self.screen_y/3*2))
            )

    def draw(self, screen):
        if not self.big:
            pygame.gfxdraw.filled_polygon(screen, (self.points), (0, 0, 0, 128))
        else:
            if self.orientation == "right":
                points_big = (
                    (self.points[0][0]+20, self.points[0][1]),
                    (self.points[1][0]+20, self.points[1][1]),
                    (self.points[2][0]+20, self.points[2][1])
                )
            else:
                points_big = (
                    (self.points[0][0]-20, self.points[0][1]),
                    (self.points[1][0]-20, self.points[1][1]),
                    (self.points[2][0]-20, self.points[2][1])
                )

            pygame.gfxdraw.filled_polygon(screen, (points_big), (0, 0, 0, 128))
            self.big = False
