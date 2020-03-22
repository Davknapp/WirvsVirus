import pygame

from classes.abstract_controller import AbstractController
from classes.human import human
from classes.player import player
from classes.game_gui import GameGui
from classes.social_distancing import SocialDistancing

from classes.app_instance import AppInstance

N_HUMANS = 100
HUMAN_RADIUS = 10
HUMAN_INITIAL_SPEED = 5

class GameState(AbstractController):

    def __init__(self, screen, model):
        """
            Initializes a game state, along with humans and the player
        """
        self.humans = [human(self, id, screen, model,  v=HUMAN_INITIAL_SPEED,  r=HUMAN_RADIUS) for id in range(model.N_humans)]
        self.humans[0].infection()
        self.dead_humans = []
        self.the_player = player(screen, model)
        self.game_gui = GameGui()
        self.social_distancing = SocialDistancing(self, model.social_distancing)

    def start(self):
        pass

    def finish(self):
        pass

    def frame_update(self):
        """
            Runs a single frame update. Moves, collides and updates sickness state of all humans.
        """

        # Alle aufgelaufenen Events holen und abarbeiten.
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                AppInstance.running = False
            # Wir interessieren uns auch für "Taste gedrückt"-Events.
            if event.type == pygame.KEYDOWN:
                self.the_player.handle_input(event.key)
                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        self.the_player.check_state()
        #self.the_player.movement()

        deceased = []
        for id, person in enumerate(self.humans):
            # normalize = True -> Geschwindigkeit ist konstant
            # normalize = False -> Geschwindigkeit ist "physikalisch"
            person.collisions(self.humans, self.the_player)
            person.check_state()
            if person.state == 'dead':
                deceased.append(person)
            person.movement()

        # Remove the set of recently deceased from the set of living humans and add it to the dead
        for corpse in deceased:
            self.humans.remove(corpse)
            self.dead_humans.append(corpse)

    def frame_render(self, screen):
        """
            Renders all humans (living, dead, player) to the screen.
        """
        #   First, render the dead
        for h in self.dead_humans:
            h.render_img()

        #   Then, render the living
        for h in self.humans:
            h.render_img()

        #   Render the player last, at the highest layer
        self.the_player.render_img()
        self.game_gui.render(screen)
