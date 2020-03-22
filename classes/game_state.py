import pygame

from classes.human import human
from classes.player import player

N_HUMANS = 100
HUMAN_RADIUS = 10
HUMAN_INITIAL_SPEED = 5

class GameState:
    
    def __init__(self, screen, model):
        self.humans = [human(id, screen, model,  v=HUMAN_INITIAL_SPEED,  r=HUMAN_RADIUS) for id in range(N_HUMANS)]
        self.humans[0].infection()
        self.dead_humans = []
        self.the_player = player(screen)

    def frame_update(self):
        
        deceased = []
        for id, person in enumerate(self.humans):
            # normalize = True -> Geschwindigkeit ist konstant
            # normalize = False -> Geschwindigkeit ist "physikalisch"
            person.collisions(self.humans, normalize=True)
            person.check_state()
            if person.state == 'dead':
                deceased.append(person)
            person.movement()

        # Remove the set of recently deceased from the set of living humans and add it to the dead
        for corpse in deceased:
            self.humans.remove(corpse)
            self.dead_humans.append(corpse)

    def frame_render(self, screen):
        #   First, render the dead
        for h in self.dead_humans:
            h.render_img(screen)

        #   Then, render the living
        for h in self.humans:
            h.render_img(screen)

        #   Render the player last, at the highest layer
        self.the_player.render_img()

#   Import these:

def initGameState(screen, model):
    activeGameState = GameState(screen, model)
    return activeGameState

activeGameState = None