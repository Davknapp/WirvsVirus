import pygame

    
class player(object):
    def __init__(self, screen,  img):
        self.posx = 400
        self.posy = 300
        self.img = img
        screen.blit(self.img, (self.posx, self.posy) )
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

    def render(self, screen):
        screen.blit(self.img, (self.posx, self.posy) )
