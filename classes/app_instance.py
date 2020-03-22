from classes.abstract_controller import AbstractController

class Application:
    def __init__(self):
        self.running = False
        self.active_controller = None
        self.next_controller = None


    def set_next_controller(self, controller : AbstractController):
        self.next_controller = controller

AppInstance = Application()