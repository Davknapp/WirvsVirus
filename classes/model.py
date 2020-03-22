import numpy
from random import randint
#import math as m


class model(object):
    def __init__(self):
        self.prameter = {'mean_incubation_time': 6,
                         'infection_prob':0.05,
                         'symptoms_rate': 0.2,
                         'hospital_rate': 0.1,
                         'death_rate': 0.1,
                         'recover_time': 14,
                         }

    def get_time():
        time = pygame.time.get_ticks()

    # so far, very rudimentary... 
    def model_incubation_period(h):
        smear = (randint(0,20) - 10))*0.1
        h.incubation_time = self.parameter['mean_incubation_time'] * (1+smear)
        return h

    # at contact, probability to get infected / infect others:
    def infect(h1, ip.inf_prob, hlist):
        infecting = False
        for h2 in hlist:
            inf_score = randint(0, 100)
            if inf_score > self.parameter['infection_prob']:
                
                if h1.state == 'infected' and h2.state == 'susceptible':
                    h2.state = 'infected'
                    h2.time_infected = get_time()
                    h2.incubation_time = model_incubation_period(h)
                elif h1.state == 'susceptible' and h2.state == 'infected':
                    h1.state = 'infected'
                    h1.time_infected = get_time()
                    h1.incubation_time = model_incubation_period(h)
        return h1, hlist

    # probability to get symptoms, depends on preconditions (alpha_pre, (0...1) for (no...all) preconditions, and age in years):
    def develop_symptoms(h):
        if h.state == 'infected' and h.symptoms == False:
            asymptomatic = 1-(self.parameter['symptoms_rate']*(h.alpha_pre + 0.01*h.age))
            symp_prob = radint(0, 100)
            if symp_prob < 100.* asymptomatic:
                h.symptoms = True
        return h
    
    # it takes time to get sick
    def get_sick(h):
        if h.state == 'infected' and h.symptoms == True:
            if h.incubation_time < (get_time()-h.time_infected):
                h.state = 'ill'
                h.hospital = False
        return h
        
    # probability to need to go to the hospital:
    def need_hospital(h):
        if h.state == 'ill':
            hospital_prob = self.parameter['hospital_rate']
            if randint(0, 100) > 100 * hospital_prob:
                h.hospital = True
        else:
                h.hospital = False
        return h

    # probability to die, depends on the number of available hospital beds:
    def dies(h, num_beds=100, num_patients=0):
        if h.hospital == False:
            h.death = False
        else:
            h.death = self.parameter['death_rate']*(1+2*((num_beds / num_patients)-1))
        return h


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
