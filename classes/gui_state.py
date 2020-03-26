import pygame

from classes.abstract_controller import AbstractController
from classes.gui import Slider, Button
from classes.game_state import GameState

from classes.app_instance import AppInstance

class GUIState(AbstractController):

    def __init__(self, screen, model):
        """
            Initializes GUI
        """
        self.screen = screen
        self.model = model
        self.buttons = [Button((300,400), (200,100), 'Start', (159,255,148), (255,136,77), self.start_game)]
        self.sliders = [
                        Slider((450,150), 250, 15, 50, [1,100]),
                        Slider((450,250), 250, 15, 0.5, [0,1]),
                        ]

        screen.fill((255, 255, 255))

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
                    if s.rect.collidepoint(pygame.mouse.get_pos()):
                        s.hit = True
                # Buttons
                for b in self.buttons:
                    if b.rect.collidepoint(pygame.mouse.get_pos()):
                        b.pressed = True

            elif event.type == pygame.MOUSEBUTTONUP:
                for s in self.sliders:
                    s.hit = False
                for b in self.buttons:
                    b.pressed = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start_game()


        #   Update Sliders
        for s in self.sliders:
            s.update()

        #   Update Sliders
        for b in self.buttons:
            b.update()


    def frame_render(self, screen):
        """
            Renders all GUI elements
        """
        screen.fill((255, 255, 255))

        font_heading = pygame.font.Font(pygame.font.get_default_font(), 32)
        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        color = pygame.Color(0, 0, 0)

        # Ueberschrift
        heading_xpos =  self.get_aligned_x_pos(screen, 'Einstellungen', font_heading, 'center')
        self.render_text(screen, 'Einstellungen', font_heading, color, (heading_xpos,20))

        # Anzahl Menschen
        name = 'Anzahl Menschen (1 - 100)'
        xpos = self.get_aligned_x_pos(screen, name, font, 'left_of_center')
        ypos = 150
        self.render_text(screen, name, font, color, (xpos,ypos))

        # Social Distancing
        name = 'Social Distancing (0% - 100%)'
        xpos = self.get_aligned_x_pos(screen, name, font, 'left_of_center')
        ypos += 100
        self.render_text(screen, name, font, color, (xpos,ypos))



         # Render Sliders and Buttons
        for s in self.sliders:
            s.draw(screen)
        for b in self.buttons:
            b.draw(screen)

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

    def start_game(self):
        self.model.N_humans  = int(self.sliders[0].value)
        self.model.social_distancing  = self.sliders[1].value
        gameState = GameState(self.screen, self.model)
        AppInstance.set_next_controller(gameState)
