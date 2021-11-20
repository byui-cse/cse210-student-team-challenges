
from game import constants
from game.point import Point
from game.actor import Actor
import arcade

class Bird(Actor):
    """A visible, moveable thing that participates in the game. In this case, a bird.
    Stereotype:
        Information Holder
    Attributes:
        abc
    """

    def __init__(self):
      """The class constructor."""
      super().__init__()
      self.set_sprite(arcade.Sprite("../assets/bird.png",0.25))
      self._sprite.center_x = 400
      self._sprite.center_y = 500