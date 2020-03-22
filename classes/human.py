import pygame
import random
import numpy as np
from img_lib import get_image
from pygame.time import get_ticks as time_now

from classes.abstract_human import AbstractHuman

class human(AbstractHuman):
    #define position of the human,  and the current movement.
    #draw a cricle representing the human.

    def __init__(self, game_state, id, screen, model, v=5, r=10):

        super(AbstractHuman, self).__init__()

        self.game_state = game_state
        limit_x, limit_y = screen.get_size()
        self.id = id
        self.screen = screen
        self.model = model
        self.r = r
        self.v = v
        self.posx = random.randint(0,limit_x-2*r)
        self.posy = random.randint(0,limit_y-2*r)
        self.alpha = random.random()*2*np.pi
        self.movx = np.cos(self.alpha)*self.v
        self.movy = np.sin(self.alpha)*self.v
        self.img = None
        self.set_velocity_vector(self.v)
        self.next_behaviour_change = 0

        self.imgcode = {'well': 'healthy.png',
                   'infected': 'infected.png',
                   'ill': 'infected2.png',
                   'recovered': 'recovered3.png',
                   'dead': 'dead2.png'
                   }
        
        self.collisions_active = True
        self.state = 'well'
        self.time_infected = None


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
            v, next_change = self.game_state.social_distancing.next_velocity()
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


    def collisions(self, humans, player):
        # Collisions mechanics
        # Can't collide with anything when you're six feet under ground.
        if not self.collisions_active:
            return
        
        #for id in range(self.id+1, len(humans)):
        for other in humans[self.id + 1:] + [player]:
            dx = self.posx - other.posx
            dy = self.posy - other.posy
            if (dx**2 + dy**2) < (self.r + other.r)**2:

                if not other.collisions_active:
                    continue

                angle = np.arctan2(dy, dx)
                self.movx = np.cos(angle) * self.v
                self.movy = np.sin(angle) * self.v

                if other != player:
                    other.movx = -np.cos(angle) * other.v
                    other.movy = -np.sin(angle) * other.v

                if (other.state == 'infected' or other.state == 'ill'):
                    self.infection()
                if (self.state == 'infected' or self.state == 'ill'):
                    other.infection()

    #   check_state was migrated to AbstractHuman

    #   infection was migrated to AbstractHuman

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

    # render_img was migrated to AbstractHuman
