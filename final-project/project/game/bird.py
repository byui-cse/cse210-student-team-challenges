
from game import constants
from game.point import Point
from game.actor import Actor
from game.point import Point
import arcade

class Bird(Actor):
    """A visible, moveable thing that participates in the game. In this case, a bird.
    Stereotype:
        Information Holder
    Attributes:
        Same as Actor.
    """

    def __init__(self):
        """The class constructor."""
        super().__init__()
        self.set_sprite(arcade.Sprite("cse210-student-team-challenges/final-project/assets/bird.png",0.15))
        self.set_position(Point(100,525))
        self.set_velocity(Point(0,0))
    def move_right(self):
        """Move the bird to the right."""
        self.set_velocity(Point(3,0))
        self.move()
    def move_left(self):
        """Move the bird to the left."""
        self.set_velocity(Point(-3,0))
        self.move()