
class AbstractHuman(object):

    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.movx = 0
        self.movy = 0
        self.state = 'well'
        self.collisions_active = True
        self.time_infected = None
        self.img = None
