import pygame
import random
import numpy as np
from img_lib import get_image
from pygame.time import get_ticks as time_now

from classes.social_distancing import SocialDistancingSimulation

class human(object):
    #define position of the human,  and the current movement.
    #draw a cricle representing the human.

    def __init__(self, id, screen, model, v=5, r=10):
        limit_x, limit_y = screen.get_size()
        self.id = id
        self.screen = screen
        self.model = model
        self.collisions_active = True
        self.r = r
        self.v = v
        self.posx = random.randint(0,limit_x-2*r)
        self.posy = random.randint(0,limit_y-2*r)
        self.alpha = random.random()*2*np.pi
        self.movx = np.cos(self.alpha)*self.v
        self.movy = np.sin(self.alpha)*self.v
        self.state = 'well'
        self.time_infected = None
        self.img = None
        self.set_velocity_vector(self.v)
        self.next_behaviour_change = 0


    def set_velocity_vector(self,  v):
        self.v = v
        self.movx = np.cos(self.alpha) * v
        self.movy = np.sin(self.alpha) * v

    def movement(self):
        # The dead can't move!
        if self.state == 'dead':
            return

        # Maybe change behaviour
        if pygame.time.get_ticks() > self.next_behaviour_change:
            v, next_change = SocialDistancingSimulation.next_velocity()
            self.next_behaviour_change += next_change
            self.change_speed(v)

        # Boundary reflection
        limit_x, limit_y = self.screen.get_size()
        if (self.posx <= 0) or (self.posx >= limit_x-2*self.r):
            self.movx *= (-1)
        if (self.posy <= 0) or (self.posy >= limit_y-2*self.r):
            self.movy *= (-1)

        self.posx += self.movx
        self.posy += self.movy


    def collisions(self, humans):
        # Collisions mechanics

        # Can't collide with anything when you're six feet under ground.
        if not self.collisions_active:
            return

        for id in range(self.id+1, len(humans)):
            dx = self.posx - humans[id].posx
            dy = self.posy - humans[id].posy

            if (dx**2 + dy**2) < (2*self.r)**2:
                other = humans[id]

                if not other.collisions_active:
                    continue

                angle = np.arctan2(dy, dx)
                self.movx = np.cos(angle) * self.v
                self.movy = np.sin(angle) * self.v
                other.movx = -np.cos(angle) * other.v
                other.movy = -np.sin(angle) * other.v

                if (other.state == 'infected' or other.state == 'ill'):
                    self.infection()
                if (self.state == 'infected' or self.state == 'ill'):
                    other.infection()

    def check_state(self):
        self.model.set_state(self)

        if (self.state == 'dead'):
            self.change_speed(0)
            self.collisions_active = False

        imgcode = {'well': 'healthy.png',
                   'infected': 'infected.png',
                   'ill': 'infected2.png',
                   'recovered': 'recovered3.png',
                   'dead': 'dead2.png'
                   }

        self.img = pygame.transform.scale(get_image(imgcode[self.state]), (2*self.r, 2*self.r))

    def infection(self):
        if self.state in ['recovered','ill','dead']: return
        self.state = 'infected'
        self.time_infected = time_now()

    def change_speed(self, new_v):
        """
            Changes this human's speed while maintaining its direction of movement
        """
        if (self.v != 0):
            angle = np.arctan2(self.movy, self.movx)
        else:
            angle = 2*np.pi*np.random.random()
        self.v = new_v
        self.movx = new_v * np.cos(angle)
        self.movx = new_v * np.sin(angle)


    def render_img(self):
        self.screen.blit(self.img, (self.posx, self.posy) )
