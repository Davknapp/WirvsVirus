import pygame

from classes.human import human
from classes.player import player

N_HUMANS = 100
HUMAN_RADIUS = 10
HUMAN_INITIAL_SPEED = 5

class GameState:

    def __init__(self, screen, model):
        """
            Initializes a game state, along with humans and the player
        """
        self.humans = [human(id, screen, model,  v=HUMAN_INITIAL_SPEED,  r=HUMAN_RADIUS) for id in range(N_HUMANS)]
        self.humans[0].infection()
        self.dead_humans = []
        self.the_player = player(screen)

    def frame_update(self):
        """
            Runs a single frame update. Moves, collides and updates sickness state of all humans.
        """
        deceased = []
        for id, person in enumerate(self.humans):
            # normalize = True -> Geschwindigkeit ist konstant
            # normalize = False -> Geschwindigkeit ist "physikalisch"
            person.collisions(self.humans)
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

#   Import these:

def initGameState(screen, model):
    """
        Creates and returns the game state singleton.
    """
    activeGameState = GameState(screen, model)
    return activeGameState

activeGameState = None
