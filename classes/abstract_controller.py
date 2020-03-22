from abc import ABC, abstractmethod


class AbstractController(ABC):
    
    @abstractmethod
    def frame_update(self):
        """
            Called each frame when this controller is active. Should run game logic.
        """
        raise NotImplementedError('This is an abstract method!')

    @abstractmethod
    def frame_render(self, screen):
        """
            Called each frame when this controller is active. Should render graphics.
        """
        raise NotImplementedError('This is an abstract method!')

    @abstractmethod
    def start(self):
        """
            Called when this controller becomes active.
        """
        raise NotImplementedError('This is an abstract method!')

    @abstractmethod
    def finish(self):
        """
            Called when this controller is replaced.
        """
        raise NotImplementedError('This is an abstract method!')