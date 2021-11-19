import sys
from game import constants
from game.action import Action
import Arcade

class HandleCollisionsAction(Action):
    """ Checks if the frog is overlaped by any other sprites.
    Returns true if overlapping, false if not. 
    """
    def check_collision(self):
        if self.frog.collides_with_sprite(Sprite):
            return True
        else:
            return False