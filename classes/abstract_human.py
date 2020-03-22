import pygame
from img_lib import get_image
from pygame.time import get_ticks as time_now


class AbstractHuman(object):
    """
        Common Base Class for Human and Player
    """

    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.movx = 0
        self.movy = 0
        self.state = 'well'
        self.collisions_active = True
        self.time_infected = None
        self.img = None
        self.imgcode = None

    def check_state(self):
        """
            Check and update this human's infection state, based on time elapsed since infection.
        """
        state_before = self.state
        self.model.set_state(self)

        if state_before != self.state:
            #   Only update all these things when the state has changed!

            self.update_image()

            if self.state == 'dead':
                self.change_speed(0)
                self.collisions_active = False
                self.game_state.level_stats.increment('died')
                if self.infector == self.game_state.the_player:
                    self.game_state.level_stats.increment('killed_by_player')
                self.game_state.infected_count -= 1
                if self == self.game_state.the_player:
                    self.game_state.player_died()

            if self.state == 'recovered':
                self.game_state.level_stats.increment('recovered')
                self.game_state.infected_count -= 1


    def update_image(self):
        self.img = pygame.transform.scale(get_image(self.imgcode[self.state]), (2*self.r, 2*self.r))

    def infection(self, infector):
        """
            Infects this human with the virus. Also, tracks the person who infected this human.
        """
        if self.state in ['infected','recovered','ill','dead']: 
            return
        self.state = 'infected'
        self.time_infected = time_now()
        self.infector = infector
        self.game_state.level_stats.increment('infected_total')
        if self.infector == self.game_state.the_player:
            self.game_state.level_stats.increment('infected_by_player')
        self.game_state.infected_count += 1
        self.update_image()


    def render_img(self):
        """
            Render this human to the screen.
        """
        self.screen.blit(self.img, (self.posx, self.posy) )