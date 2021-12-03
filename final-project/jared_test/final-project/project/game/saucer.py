import arcade
from game import constants

class Saucer(arcade.Sprite):
    """A code template for the saucer sprite. The responsibility of 
    this class of objects is to setup the saucer sprite.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Saucer): an instance of saucer.
        """
        #Set sprite and scale
        self.sprite = arcade.Sprite(":resources:images/tiles/switchGreen.png", constants.SAUCER_SCALING)

        #Position, angle, direction, speed
        self.sprite.center_x = 799
        self.sprite.center_y = 100
        self.sprite.angle = 0
        self.sprite.change_x = 3

    #Wraps around edge of screen
    def wraps_screen(self):
        if self.sprite.left > constants.SCREEN_WIDTH:
            self.sprite.right = 0
        elif self.sprite.right < 0:
            self.sprite.left = constants.SCREEN_WIDTH