from pygame.time import get_ticks as time_now
from random import random

class Model(object):
        def __init__(self):
            self.prameter = {'incubation_time': 1000,
                             'illness_rate': 0.4,
                             'death_rate': 0.02,
                             'survival_time': 2000,
                             'recover_time': 5000,
                             }
        def set_state(self, human):

            if (human.state == 'infected'):
                time_diff = time_now() - human.time_infected
                if (time_diff > self.prameter ['incubation_time']):
                    if (random() < self.prameter['illness_rate']):
                        human.state = 'ill'

            if (human.state == 'ill'): #'ill'):
                time_diff = time_now() - human.time_infected  - self.prameter ['incubation_time']
                if (time_diff > self.prameter['recover_time']):
                    if (random() < self.prameter['death_rate']):
                        human.state = 'dead'
                    else:
                        human.state = 'recovered'
