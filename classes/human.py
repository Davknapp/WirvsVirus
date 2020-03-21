import pygame
import random
import numpy as np

class human(object):
    #define position of the human,  and the current movement.
    #draw a cricle representing the human.
    def __init__(self, id, screen, v=5, r=10):
        limit_x, limit_y = screen.get_size()
        self.id = id
        self.screen = screen
        self.r = r
        self.v = v
        self.posx = random.randint(0,limit_x)
        self.posy = random.randint(0,limit_y)
        self.alpha = random.random()*2*np.pi
        self.movx = np.cos(self.alpha)*self.v
        self.movy = np.sin(self.alpha)*self.v
        self.infected = False
        self.color=(255,255,255)
        self.render()

    def movement(self):
        # Boundary reflection
        limit_x, limit_y = self.screen.get_size()
        if (self.posx <= 0) or (self.posx >= limit_x):
            self.movx *= (-1)
        if (self.posy <= 0) or (self.posy >= limit_y):
            self.movy *= (-1)

        self.posx += self.movx
        self.posy += self.movy

    def collisions(self, humans, normalize=False):
        # Collisions mechanics
        for id in range(self.id+1, len(humans)):
            dx = self.posx - humans[id].posx
            dy = self.posy - humans[id].posy
            if (dx**2 + dy**2) < (2*self.r)**2:
                if normalize:
                    vx, vy = self.v, self.v
                else:
                    vx = np.sqrt(self.movx**2 + humans[id].movx**2)
                    vy = np.sqrt(self.movy**2 + humans[id].movy**2)
                angle = np.arctan2(dy, dx)
                self.movx = np.cos(angle)*vx
                self.movy = np.sin(angle)*vy
                humans[id].movx = -np.cos(angle)*vx
                humans[id].movy = -np.sin(angle)*vy

    def infection(self):
        self.infected = True
        self.color = (0,255,0)

    def render(self):
        pygame.draw.circle(self.screen, self.color, (int(self.posx), int(self.posy)), self.r)
