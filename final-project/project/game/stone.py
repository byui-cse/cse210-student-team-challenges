
from game import constants
import arcade

class Stone(arcade.Sprite):
    """A visible, moveable thing that participates in the game. In this case, a stone.
    Stereotype:
        Information Holder
    Attributes:
        Same as Actor.
    """

    def __init__(self, center_x, center_y):
        """The class constructor.
        
        Args:
            self (Stone): An instance of Stone
            pos (List): An initial position
        """
        base = constants.get_base()
        super().__init__(f"{base}/stone.png",0.04)
        self.set_position(center_x, center_y)
        self.change_y = -constants.STONE_SPEED
    def on_update(self, time_delta):
        self.change_y -= self.G
        pass