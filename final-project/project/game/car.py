
from game import constants
import arcade
import os
import random

class Car(arcade.Sprite):
    """A visible, moveable thing that participates in the game. In this case, a car.
    Stereotype:
        Information Holder
    Attributes:
        _direction: Which way the car is moving
    """

    def __init__(self):
        """The class constructor."""
        base = constants.get_base()
        car_type = random.choice(["car1.png","car2.png"])
        super().__init__(f"{base}/{car_type}",0.15)
        self.set_position(center_x=200,center_y=30)
        self.change_x = random.choice([1, -1])*constants.CAR_SPEED
