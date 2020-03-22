import pygame
from img_lib import get_image

class player(object):

    def __init__(self, screen):
        self.posx = 400
        self.posy = 300
        self.screen = screen
        self.img = pygame.transform.scale(get_image('myself3.png'), (30, 30))
        self.render_img()

    def handle_input(self, key):
        # linke Pfeiltaste wird gedrueckt
        if key == pygame.K_LEFT:
            # x-Position der Spielfigur anpassen,
            self.posx -= 1
        # und nochmal die rechte Pfeiltaste
        if key == pygame.K_RIGHT:
            self.posx += 1
        if key == pygame.K_UP:
            self.posy -= 1
        if key == pygame.K_DOWN:
            self.posy += 1

    def render_img(self):
        self.screen.blit(self.img, (self.posx, self.posy) )
