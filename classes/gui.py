import pygame
import pygame.font

from pygame import Rect

class Slider(object):
    '''
        A simpler Slider widget for the GUI
    '''
    def __init__(self, position, width, radius, init_val, range):

        self.hit = False

        self.width = width
        self.height = 2*radius
        self.position = position
        self.handle_position = 0
        self.value = init_val
        self.range = range
        self.radius = radius
        self.rec = None

        # Static (Backgtound, Bar, etc.)
        self.static_surf = pygame.surface.Surface((self.width, self.height))
        self.static_surf.fill((255, 255, 255))
        # Design of slider bar goes here
        bar_width = width - 2*radius
        bar_height = 4
        bar_pos = (radius, self.height//2-bar_height)
        bar_color = (0, 0, 0)
        bar = Rect(bar_pos, (bar_width, bar_height))
        pygame.draw.rect(self.static_surf, bar_color, bar)

        # Dynamic (Button that slides)
        self.button_surf = pygame.surface.Surface((2*self.radius, 2*self.radius))
        # Make background transparent
        TRANS = pygame.Color(1, 1, 1)
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        # Design of silder button goes here
        color_c1 = pygame.Color(50, 50, 50)
        color_c2 = pygame.Color(150, 150, 150)
        pygame.draw.circle(self.button_surf, color_c1, (radius, radius), radius)
        pygame.draw.circle(self.button_surf, color_c2, (radius, radius), radius - bar_height)

    def update(self):
        '''
            Calculate value of slider depending on mouse position
        '''
        mouse_pos = pygame.mouse.get_pos()[0]
        if self.hit:
            self.value = (mouse_pos - self.position[0] - self.radius) \
                       / (self.width - 2*self.radius) \
                       * (self.range[-1] - self.range[0]) \
                       + self.range[0]
            if (self.value > self.range[-1]):
                self.value = self.range[-1]
            if (self.value < self.range[0]):
                self.value = self.range[0]

    def draw(self, screen):
        '''
            Draw the static and dynamic parts of the slider
        '''
        # Static
        surf = self.static_surf.copy()

        # Dynamic
        button_position = (self.value / (self.range[-1] - self.range[0])) \
                        * (self.width - 2*self.radius) + self.radius
        button_position = int(button_position)
        self.rect = self.button_surf.get_rect(center=(button_position, self.radius))

        # Combine static and dynamic parts and draw on screen
        surf.blit(self.button_surf, self.rect)
        self.rect.move_ip(*self.position)
        screen.blit(surf, self.position)


class Button(object):
    '''
        A simpler Button widget for the GUI
    '''
    def __init__(self, position, size, name, color, color_pressed, callback):

        self.pressed = False

        self.position = position
        self.size = size
        self.callback = callback
        self.color_pressed = color_pressed
        self.rect = None
        self.name = name
        self.color = color

        self.surf = pygame.surface.Surface(size)


    def update(self):
        if self.pressed:
            self.callback()

    def draw(self, screen):

        pos = (self.position[0] + self.size[0]//2, self.position[1] + self.size[1]//2)
        self.rect = self.surf.get_rect(center=pos)

        font = pygame.font.Font(pygame.font.get_default_font(), 42)
        color = pygame.Color(0, 0, 0)
        surface = font.render(self.name, True, color)
        if not self.pressed:
            self.surf.fill((100,100,100))
            pygame.draw.rect(self.surf, self.color, Rect((3,3), (self.size[0]-6,self.size[1]-6)))
        else:
            self.surf.fill((100,100,100))
            pygame.draw.rect(self.surf, self.color_pressed, Rect((3,3), (self.size[0]-6,self.size[1]-6)))

        # Center the text on Button
        text_size = font.size(self.name)
        text_posx = self.size[0] // 2 - text_size[0] // 2
        text_posy = self.size[1] // 2 - text_size[1] // 2
        self.surf.blit(surface, (text_posx, text_posy))
        screen.blit(self.surf, self.position)
