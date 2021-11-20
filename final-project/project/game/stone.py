
from game import constants
from game.point import Point
from game.actor import Actor
from game.point import Point
import arcade

class Stone(Actor):
    """A visible, moveable thing that participates in the game. In this case, a stone.
    Stereotype:
        Information Holder
    Attributes:
        Same as Actor.
    """

    def __init__(self, pos):
        """The class constructor.
        
        Args:
            self (Stone): An instance of Stone
            pos (Point): An initial position
        """
        super().__init__()
        self.set_sprite(arcade.Sprite("../assets/stone.png",0.1))
        self.set_position(pos)
        self.set_velocity(Point(0,-3))