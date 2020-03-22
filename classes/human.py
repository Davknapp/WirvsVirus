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
        self.v=v
        self.posx = random.randint(0,limit_x)
        self.posy = random.randint(0,limit_y)
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
        self.movx = np.cos(self.alpha) *v
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
        if (self.posx <= 0) or (self.posx >= limit_x):
            self.movx *= (-1)
        if (self.posy <= 0) or (self.posy >= limit_y):
            self.movy *= (-1)

        self.posx += self.movx
        self.posy += self.movy


    def collisions(self, humans, normalize=True):
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

                if normalize:
                    vx, vy = self.v, self.v
                else:
                    vx = np.sqrt(self.movx**2 + other.movx**2)
                    vy = np.sqrt(self.movy**2 + other.movy**2)
                angle = np.arctan2(dy, dx)
                self.movx = np.cos(angle)*vx
                self.movy = np.sin(angle)*vy
                humans[id].movx = -np.cos(angle)*vx
                humans[id].movy = -np.sin(angle)*vy

                if (humans[id].state == 'infected' or humans[id].state == 'ill'):# and (self.state != 'infected' and self.state != 'ill'):
                    self.infection()
                if (self.state == 'infected' or self.state == 'ill'): #and (humans[id].state == 'infected' and humans[id].state == 'ill'):
                    humans[id].infection()

    def check_state(self):
        self.model.set_state(self)

        if (self.state == 'dead'):
            self.movx = 0
            self.movy = 0
            self.collisions_active = False

        imgcode = {'well': 'healthy.png',
                   'infected': 'infected.png',
                   'ill': 'infected2.png',
                   'recovered': 'recovered.png',
                   'dead': 'dead.png'
                   }

        self.img = pygame.transform.scale(get_image(imgcode[self.state]), (20, 20))

    def infection(self):
        if self.state in ['recovered','ill','dead']: return
        self.state = 'infected'
        self.time_infected = time_now()

    def change_speed(self, new_v_magnitude):
        """
            Changes this human's speed while maintaining its direction of movement
        """
        v_norm = np.sqrt(self.movx**2 + self.movy**2)
        v_direction_x = self.movx / v_norm
        v_direction_y = self.movy / v_norm
        
        self.movx = v_direction_x * new_v_magnitude
        self.movy = v_direction_y * new_v_magnitude

    def render_img(self, screen):
        screen.blit(self.img, (self.posx, self.posy) )
