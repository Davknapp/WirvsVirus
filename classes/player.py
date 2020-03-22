import pygame
from img_lib import get_image
from classes.abstract_human import AbstractHuman

import numpy as np

BASE_VELOCITY = 4

class player(AbstractHuman):

    def __init__(self, screen, model):

        super(AbstractHuman, self).__init__()
        
        self.posx = 400
        self.posy = 300
        self.screen = screen
        self.model = model
        #self.img = pygame.transform.scale(get_image('myself3.png'), (30, 30))
        self.r = 15
        self.collisions_active = True
        self.state = 'well'
        self.time_infected = None
        # Set velocity
        self.current_velocity = BASE_VELOCITY

        #self.render_img()

        self.movx = 0
        self.movy = 0
        self.v = 0

        self.imgcode = {'well': 'myself3.png',
                   'infected': 'myselfInfected.png',
                   'ill': 'myselfSeriouslyInfected.png',
                   'recovered': 'recovered3.png',
                   'dead': 'myselfDead.png'
                   }

    def handle_input(self, key):
        # linke Pfeiltaste wird gedrueckt
        if key == pygame.K_LEFT:
            # x-Position der Spielfigur anpassen,
            self.posx -= self.current_velocity
        # und nochmal die rechte Pfeiltaste
        if key == pygame.K_RIGHT:
            self.posx += self.current_velocity
        if key == pygame.K_UP:
            self.posy -= self.current_velocity
        if key == pygame.K_DOWN:
            self.posy += self.current_velocity

        limit_x, limit_y = self.screen.get_size()
        if self.posx < 0: 
            self.posx = 0
        
        if self.posx > limit_x-2 * self.r:
            self.movx = limit_x-2 * self.r
            
        if self.posy < 0:
            self.posy = 0

        if self.posy > limit_y-2*self.r:
            self.movy = limit_y-2 * self.r

    def change_speed(self, new_speed):
        """ Changes the speed with which the player moves.
            This is most important when the player dies and its speed
            is set to 0
        """
        self.current_velocity = new_speed


    # def movement(self):

    #     if self.state == 'dead':
    #         return

    #     self.posx += self.movx
    #     self.posy += self.movy

        

    # render_img was migrated to AbstractHuman
