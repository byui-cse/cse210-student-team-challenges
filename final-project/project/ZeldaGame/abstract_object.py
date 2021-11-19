from abc import ABC, abstractmethod

class MainObjects(ABC):

    @property
    def sprite_list(self):
        pass

    @abstractmethod
    def add_sprite(self):
        pass