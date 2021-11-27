
from game import constants
import arcade
import os

class Bird(arcade.Sprite):
    """A visible, moveable thing that participates in the game. In this case, a bird.
    Stereotype:
        Information Holder
    Attributes:
        Same as Sprite.
    """

    def __init__(self):
        """The class constructor."""
        base = constants.get_base()
        super().__init__(f"{base}/bird.png",0.15)
        self.set_position(center_x=100,center_y=525)
    def move_right(self):
        """Move the bird to the right."""
        self.change_x = constants.BIRD_SPEED
        #self.update()
        #self.forward(speed=constants.BIRD_SPEED)
    def move_left(self):
        """Move the bird to the left."""
        self.change_x = -constants.BIRD_SPEED
        #self.update()
        #self.forward(speed=-constants.BIRD_SPEED)