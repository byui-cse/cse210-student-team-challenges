import arcade
from scaling import SPRITE_SCALING

class Obstacle(arcade.Sprite):
    
    def __init__(self, image):
        self.__obstacle = arcade.Sprite(f"{image}",
                                    SPRITE_SCALING)

    def position_obstacle(self, left, bottom):
        self.__obstacle.left = left
        self.__obstacle.bottom = bottom

    @property
    def obstacle(self):
        return self.__obstacle