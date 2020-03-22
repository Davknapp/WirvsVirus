import pygame

from classes.abstract_controller import AbstractController
from classes.app_instance import AppInstance


class ResultsView (AbstractController):

    def __init__(self, level_stats):
        self.level_stats = level_stats
        
    def frame_update(self):
        """
            Called each frame when this controller is active. Should run game logic.
        """
        # Alle aufgelaufenen Events holen und abarbeiten.
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                AppInstance.running = False
            # Wir interessieren uns auch für "Taste gedrückt"-Events.
            if event.type == pygame.KEYDOWN:
                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

    def frame_render(self, screen):
        """
            Called each frame when this controller is active. Should render graphics.
        """
        screen.fill((0,102,204))

        color = pygame.Color(255,255,255)

        #   Draw the win/lose message
        font = pygame.font.Font(pygame.font.get_default_font(), 32)
        pos_x = self.get_aligned_x_pos(screen, self.level_stats.end_reason, font, 'center')
        self.render_text(screen, self.level_stats.end_reason, font, color, (pos_x, 100) )

    #   Render all the stats
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        y_pos = 200
        y_inc = font.size('H')[1] + 10

        for st in self.level_stats.stats:
            name = self.level_stats.get_text(st)
            value = '   ' + str(self.level_stats.get_value(st))

            name_x_pos = self.get_aligned_x_pos(screen, name, font, 'left_of_center')
            value_x_pos = self.get_aligned_x_pos(screen, value, font, 'right_of_center')
            
            self.render_text(screen, name, font, color, (name_x_pos, y_pos))
            self.render_text(screen, value, font, color, (value_x_pos, y_pos))

            y_pos += y_inc


    def render_text(self, screen, text, font, color, pos):
        """
            Renders text to the screen using a given font with a given color at a given position
        """
        surface = font.render(text, True, color)
        screen.blit(surface, pos)

    def get_aligned_x_pos(self, screen, text, font, alignment):
        """
            Gets the x-Position for center-aligned text.
        """
        text_size = font.size(text)
        if alignment == 'center':
            return screen.get_size()[0] // 2 - text_size[0] // 2
        if alignment == 'left_of_center':
            return screen.get_size()[0] // 2 - text_size[0]
        if alignment == 'right_of_center':
            return screen.get_size()[0] // 2

    def start(self):
        """
            Called when this controller becomes active.
        """
        pass

    def finish(self):
        """
            Called when this controller is replaced.
        """
        pass

