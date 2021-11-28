from game.actor import Actor
from game.point import Point

class Score(Actor):
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
      Information Holder

    Attributes: 
      _points (integer): The number of points.
    """