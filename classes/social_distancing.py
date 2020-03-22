"""
    Social Distancing Simulation
"""

import random
import pygame

MIN_VELOCITY = 1
VELOCITY_SPAN = 5
KEEP_BEHAVIOUR_FOR_MS = 5000

class SocialDistancing(object):

    def __init__(self, game_state):
        self._social_distancing = 0.5
        self.game_state = game_state
        game_state.game_gui.set_social_distancing_factor(self._social_distancing)

        # Provisional: Set social distancing factor via command line.
        # Launch with 'python main.py 0.7' or any value between 0 and 1.
        try:
            import sys
            if len(sys.argv) > 1:
                self.set_social_distancing(float(sys.argv[1]))
        except ImportError:
            pass


    def set_social_distancing(self, value):
        """
            Sets 'social distancing' to a value between zero and one; zero indicating everyone constantly partying and one meaning (almost) everyone stays at home.
        """
        if value < 0 or value > 1:
            raise ValueError('Value must be between zero and one')

        self._social_distancing = value
        self.game_state.game_gui.set_social_distancing_factor(self._social_distancing)

    def get_social_distancing(self):
        """
            Returns the current social distancing factor
        """
        return self._social_distancing


    def next_velocity(self):
        """
            Called by a human to retrieve the velocity v it should maintain for the next few seconds.
            The velocity depends on the current rate of social distancing.
            Returns a tuple (v, time).
        """
        #   Randomize the velocity a little around the social distancing factor
        rand_shift = -0.3 + (random.random() * 0.6)
        distancing = self._social_distancing + rand_shift
        if distancing < 0:
            distancing = 0
        if distancing > 1:
            distancing = 1

        v = 0 if distancing == 1 else MIN_VELOCITY + (1 - distancing) * (VELOCITY_SPAN)

        rand_time = 0.5 + random.random()

        return int(v), int(rand_time * KEEP_BEHAVIOUR_FOR_MS)
