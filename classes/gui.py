import pygame
import pygame.font

from pygame import Rect

class Slider(object):
    def __init__(self, screen, position):
        self.screen = screen
        self.width = 200
        self.height = 20

        self.surface = pygame.surface.Surface((self.width, self.height))
        self.position = position
        self.handle_position = 10

        self.hit = False
        self.value = 0
        self.range = [0, 1]
        self.radius = 10
        self.color_c1 = (50, 50, 50)
        self.color_c2 = (150, 150, 150)
        self.color_bar = (0, 0, 0)
        self.rec = None
        self.name = 'Slider'

        # Static
        self.surface.fill((255, 255, 255))
        pygame.draw.rect(self.surface, self.color_bar, Rect((self.radius,self.height//2-2), (self.width-2*self.radius, 4)))


        # Dynamic
        self.button_surf = pygame.surface.Surface((2*self.radius, 2*self.radius))
        self.button_surf.fill((1, 1, 1))
        self.button_surf.set_colorkey((1, 1, 1))
        pygame.draw.circle(self.button_surf, self.color_c1, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.button_surf, self.color_c2, (self.radius, self.radius), self.radius-4)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()[0]
        if self.hit:
            # self.delta = mouse_pos - self.handle_position - self.radius
            self.value = (mouse_pos - self.position[0] - self.radius) / (self.width - 2*self.radius) * (self.range[-1] - self.range[0]) + self.range[0]
            if (self.value > self.range[-1]):
                self.value = self.range[-1]
            if (self.value < self.range[0]):
                self.value = self.range[0]

    def draw(self):

        # Static
        surf = self.surface.copy()

        # Dynamic
        self.handle_position = int((self.value / (self.range[-1] - self.range[0] )) * (self.width -2*self.radius) + self.radius)
        self.rect = self.button_surf.get_rect(center=(self.handle_position, self.position[1]))
        surf.blit(self.button_surf, self.rect)
        self.rect.move_ip(*self.position)

        # Display
        self.screen.blit(surf, self.position)
