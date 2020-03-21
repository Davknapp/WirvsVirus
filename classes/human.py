import pygame
import random
import numpy as np

class human(object):
    #define position of the human,  and the current movement.
    #draw a cricle representing the human.
    def __init__(self, limit_x, limit_y,  screen):
        self.posx = random.randint(0,limit_x)
        self.posy = random.randint(0,limit_y)
        self.alpha = random.randint(0,359)
        self.movx = int(np.cos(self.alpha)*10)
        self.movy = int(np.sin(self.alpha)*10)
        self.infected = False
        self.color=(255,255,255)
        pygame.draw.circle(screen, self.color, (self.posx, self.posy), 10)

    def movement(self, screen):

        # Boundary reflection
        limit_x, limit_y = screen.get_size()
        if (self.posx <= 0) or (self.posx >= limit_x):
            self.movx *= (-1)
        if (self.posy <= 0) or (self.posy >= limit_y):
            self.movy *= (-1)

        self.posx += self.movx
        self.posy += self.movy
        pygame.draw.circle(screen, self.color, (self.posx, self.posy), 10)

    def infection(self):
        self.infected = True
        self.color = (0,255,0)