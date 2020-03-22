import pygame

from classes.abstract_controller import AbstractController
from classes.gui import Slider
from classes.game_state import GameState

from classes.app_instance import AppInstance

N_HUMANS = 100
HUMAN_RADIUS = 10
HUMAN_INITIAL_SPEED = 5

class GUIState(AbstractController):

    def __init__(self, screen, model):
        """
            Initializes GUI
        """
        self.screen = screen
        self.model = model
        self.buttons = []
        self.sliders = [Slider(screen, (10,10))]

        screen.fill((255, 255, 255))

    def start(self):
        pass

    def finish(self):
        '''
            Save Parameters
        '''


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
                    if s.rect.collidepoint(pygame.mouse.get_pos()):
                        s.hit = True
                # Buttons
                for b in self.buttons:
                    pass

            elif event.type == pygame.MOUSEBUTTONUP:
                for s in self.sliders:
                    s.hit = False
                for b in self.buttons:
                    pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.model.social_distancing  = self.sliders[0].value
                    gameState = GameState(self.screen, self.model)
                    AppInstance.set_next_controller(gameState)


        #   Update Sliders
        for s in self.sliders:
            s.update()


    def frame_render(self, screen):
        """
            Renders all GUI elements
        """
        screen.fill((255, 255, 255))

        #   Render Sliders and Buttons
        for s in self.sliders:
            s.draw()
        for b in self.buttons:
            b.draw()
