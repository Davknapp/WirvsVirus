"""
    Social Distancing Simulation
"""

import random

MAX_VELOCITY = 5
KEEP_BEHAVIOUR_FOR_MS = 1000

_social_distancing = 1.

def set_social_distancing(value):
    """ 
        Sets 'social distancing' to a value between zero and one; zero indicating everyone constantly partying and one meaning (almost) everyone stays at home.
    """
    if value < 0 or value > 1:
        raise ValueError('Value must be between zero and one')

    _social_distancing = value

def get_social_distancing():
    return _social_distancing


def next_velocity():
    rand_shift = -0.3 + (random.random() * 0.6)
    distancing = _social_distancing + rand_shift
    if distancing < 0:
        distancing = 0
    if distancing > 1:
        distancing = 1

    rand_time = 0.5 + random.random()

    return int(MAX_VELOCITY * (1-distancing)), int(rand_time * KEEP_BEHAVIOUR_FOR_MS)