import arcade
from game import K

class Player(arcade.Sprite):
    """ Player Class """

    def update(self):
        """ Move the player """
     
        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > K.SCREEN_WIDTH - 1:
            self.right = K.SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > K.SCREEN_HEIGHT - 1:
            self.top = K.SCREEN_HEIGHT - 1