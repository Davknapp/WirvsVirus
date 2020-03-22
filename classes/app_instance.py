from classes.abstract_controller import AbstractController

class Application:
    """
        Singleton class which manages the global application state.
    """
    def __init__(self):
        self.running = False
        self.active_controller = None
        self.next_controller = None

    
    def set_next_controller(self, controller : AbstractController):
        """
            Sets the controller which replaces the active controller at the start of the next frame.
        """
        self.next_controller = controller

AppInstance = Application()