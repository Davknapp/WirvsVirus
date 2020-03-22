import pygame

from classes.abstract_controller import AbstractController
from classes.gui import Slider

from classes.app_instance import AppInstance

N_HUMANS = 100
HUMAN_RADIUS = 10
HUMAN_INITIAL_SPEED = 5

class GUIState(AbstractController):

    def __init__(self, screen):
        """
            Initializes GUI
        """
        self.buttons = []
        self.sliders = [Slider(screen, (10,10))]

    def start(self):
        pass

    def finish(self):
        pass

    def frame_update(self):
        """
            Runs a single frame update.
        """

        # Alle aufgelaufenen Events holen und abarbeiten.
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                AppInstance.running = False

            #   Erfasse Maus-Interakionen
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Slider
                for s in self.sliders:
                    if s.rect.collidepoint(mouse_position):
                        s.hit = True
                # Buttons
                for b in self.buttons:
                    pass

            elif event.type == pygame.MOUSEBUTTONUP:
                for s in self.sliders:
                    s.hit = False
                for b in self.buttons:
                    pass


        #   Update Sliders
        for s in self.sliders:
            s.update()


    def frame_render(self, screen):
        """
            Renders all GUI elements
        """
        #   Render Sliders and Buttons
        for s in self.sliders:
            s.update()
        for b in self.buttons:
            b.update()
