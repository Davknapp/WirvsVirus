import pygame

from classes.abstract_controller import AbstractController
from classes.human import human
from classes.player import player
from classes.game_gui import GameGui
from img_lib import background
from classes.social_distancing import SocialDistancing
from classes.level_stats import LevelStats

from classes.results_view import ResultsView
from classes.app_instance import AppInstance

N_HUMANS = 100
HUMAN_RADIUS = 10
HUMAN_INITIAL_SPEED = 5

ENDGAME_DELAY = 3000    # 3 seconds

class GameState(AbstractController):

    def __init__(self, screen, model):
        """
            Initializes a game state, along with humans and the player
        """
        stat_names = [
            'infected_total',
            'infected_by_player',
            'died',
            'killed_by_player',
            'recovered',
            'level_time'
        ]

        stat_texts = {
            'infected_total'        : 'Anzahl Infizierte:',
            'infected_by_player'    : 'Durch dich Infiziert:',
            'died'                  : 'Gestorben:',
            'killed_by_player'      : 'Durch deine Infektion gestorben:',
            'recovered'             : 'Vom Virus erholt:',
            'level_time'            : 'Vergangene Zeit:'
        }

        self.level_stats = LevelStats(stat_names, stat_texts)

        self.the_player = player(self, screen, model)
        self.humans = [human(self, id, screen, model,  v=HUMAN_INITIAL_SPEED,  r=HUMAN_RADIUS) for id in range(model.N_humans)]
        self.dead_humans = []
        self.game_gui = GameGui()
        self.back = background('map.png', [0,0])
        self.social_distancing = SocialDistancing(self, model.social_distancing)
        self._infected_count = 0
        self.start_time = 0
        self.end_condition_met_at = -1.
        self.humans[0].infection(None)


    @property
    def infected_count(self):
        """
            Property to count the number of infected humans (including the player).
        """
        return self._infected_count

    @infected_count.setter
    def infected_count(self, value):
        """
            Sets the count of infected humans (including the player).
            If this counter reaches zero, initalize level shutdown.
        """
        self._infected_count = value
        if self._infected_count == 0:
            self.end_condition_met_at = pygame.time.get_ticks()
            self.level_stats.end_reason = 'Das Virus wurde ausgerottet!'

    def player_died(self):
        """
            Notify the GameState that the player has died and the funeral has to be arranged.
        """
        self.end_condition_met_at = pygame.time.get_ticks()
        self.level_stats.end_reason = 'Du bist gestorben!'

    def start(self):
        self.start_time = pygame.time.get_ticks()

    def finish(self):
        pass

    def frame_update(self):
        """
            Runs a single frame update. Moves, collides and updates sickness state of all humans.
        """

        #   If and end condition was met and the delay elapsed, close this level.
        if self.end_condition_met_at > 0:
            ctime = pygame.time.get_ticks()
            if ctime - self.end_condition_met_at >= ENDGAME_DELAY:
                self.end_level()
                return

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
        screen.blit(self.back.image, self.back.rect)

        #   First, render the dead
        for h in self.dead_humans:
            h.render_img()

        #   Then, render the living
        for h in self.humans:
            h.render_img()

        #   Render the player last, at the highest layer
        self.the_player.render_img()
        self.game_gui.render(screen)


    def end_level(self):
        """
            Wraps things up after the level is completed.
        """
        level_time_ms = self.end_condition_met_at - self.start_time
        self.level_stats.set_value('level_time', str(level_time_ms // 1000) + ' Sekunden')
        results_view = ResultsView(self.level_stats)

        AppInstance.set_next_controller(results_view)
