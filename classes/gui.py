import pygame
import pygame.font


class GuiClass(object):

    def __init__(self):

        # private attributes
        self.social_distancing_text = ''

        pygame.font.init()

        self.default_font = pygame.font.Font(pygame.font.get_default_font(), 15)
        self.renderable_surfaces = {}

    def set_social_distancing_factor(self, value):
        self.social_distancing_text = "Social Distancing: {}%".format(int(100 * value))

    def render_social_distancing_text(self, screen):
        surface = self.default_font.render(self.social_distancing_text, True, pygame.Color(255,255,255))
        position = ( 0, self.default_font.size(self.social_distancing_text)[1] )
        screen.blit(surface, position)

    def render(self, screen):
        self.render_social_distancing_text(screen)

# Import this
activeGui = GuiClass()