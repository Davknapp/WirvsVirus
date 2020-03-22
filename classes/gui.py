import pygame
import pygame.font

from pygame import Rect

class Slider(object):
    '''
        A simpler Slider widget for the GUI
    '''
    def __init__(self, screen, position, width, radius, init_val, range):
        self.screen = screen
        self.width = width
        self.height = 2*radius
        self.surface = pygame.surface.Surface((self.width, self.height))
        self.position = position
        self.handle_position = 0
        self.hit = False
        self.value = init_val
        self.range = range
        self.radius = radius
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

    def draw(self, screen):

        # Static
        surf = self.surface.copy()

        # Dynamic
        self.handle_position = int((self.value / (self.range[-1] - self.range[0] )) * (self.width -2*self.radius) + self.radius)
        self.rect = self.button_surf.get_rect(center=(self.handle_position, self.radius))
        surf.blit(self.button_surf, self.rect)
        self.rect.move_ip(*self.position)

        # Display
        self.screen.blit(surf, self.position)


class Button(object):
    '''
        A simpler Button widget for the GUI
    '''
    def __init__(self, screen, position, size, name, color, color_pressed, callback):

        self.pressed = False

        self.screen = screen
        self.position = position
        self.size = size
        self.callback = callback
        self.color_pressed = color_pressed
        self.rect = None
        self.name = name
        self.color = color

        self.surf = pygame.surface.Surface(size)
        self.surf.fill(color)



    def update(self):
        if self.pressed:
            self.callback()

    def draw(self, screen):

        self.rect = self.surf.get_rect(center=(self.position[0]+self.size[0]//2,self.position[1]+self.size[1]//2))

        font = pygame.font.Font(pygame.font.get_default_font(), 42)
        color = pygame.Color(0, 0, 0)
        surface = font.render(self.name, True, color)
        if not self.pressed:
            self.surf.fill((100,100,100))
            pygame.draw.rect(self.surf, self.color, Rect((3,3), (self.size[0]-6,self.size[1]-6)))
        else:
            self.surf.fill((100,100,100))
            pygame.draw.rect(self.surf, self.color_pressed, Rect((3,3), (self.size[0]-6,self.size[1]-6)))
        self.surf.blit(surface, (50,25))
        screen.blit(self.surf, self.position)
