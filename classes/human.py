import pygame
import random
import numpy as np
from img_lib import get_image

class human(object):
    #define position of the human,  and the current movement.
    #draw a cricle representing the human.

    def __init__(self, id, screen,  img,  v=5, r=10):
        limit_x, limit_y = screen.get_size()
        self.id = id
        self.screen = screen
        self.collisions_active = True
        self.r = r
        self.v = v
        self.posx = random.randint(0,limit_x)
        self.posy = random.randint(0,limit_y)
        self.alpha = random.random()*2*np.pi
        self.movx = np.cos(self.alpha)*self.v
        self.movy = np.sin(self.alpha)*self.v
        self.infected = False
        self.img = img
        self.render(screen)
        #screen.blit(self.img, (self.posx, self.posy) )

    def movement(self):
        # Boundary reflection
        limit_x, limit_y = self.screen.get_size()
        if (self.posx <= 0) or (self.posx >= limit_x):
            self.movx *= (-1)
        if (self.posy <= 0) or (self.posy >= limit_y):
            self.movy *= (-1)

        self.posx += self.movx
        self.posy += self.movy
       # screen.blit(self.img, (self.posx, self.posy) )

    def collisions(self, humans, normalize=True):
        # Collisions mechanics
        for id in range(self.id+1, len(humans)):
            dx = self.posx - humans[id].posx
            dy = self.posy - humans[id].posy
            if not self.collisions_active: continue
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

                if (humans[id].state == 'infected') and (not self.state == 'infected'):
                    self.infection()
                if (self.state == 'infected') and (not humans[id].state == 'infected'):
                    humans[id].infection()

    def check_state(self):
        self.model.set_state(self)

        if (self.state == 'dead'):
            self.collisions_active = False

        colorcode = {'well': (255,255,255),
                     'infected': (0,255,0),
                     'recovered': (0,0,255),
                     'dead': (255,0,0)
                    }

        self.color = colorcode[self.state]

    def infection(self):
        self.infected = True
        self.img = pygame.transform.scale(get_image('infected2.png'), (20, 20))

    def render(self, screen):
        screen.blit(self.img, (self.posx, self.posy) )
