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

        #   Draw the win/lose message


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

