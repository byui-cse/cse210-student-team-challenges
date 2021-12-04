import arcade
from game import constants

class Saucer(arcade.Sprite):
    """A code template for the saucer sprite. The responsibility of 
    this class of objects is to setup the saucer sprite.
    """
    def __init__(self, x_value, y_value, angle, x_speed):
        """The class constructor.
        
        Args:
            self (Saucer): an instance of saucer.
        """
        #Set sprite and scale
        self.sprite = arcade.Sprite(":resources:images/tiles/switchGreen.png", constants.SAUCER_SCALING)

        #Initialize Position, direction, speed
        self.sprite.center_x = x_value
        self.sprite.center_y = y_value
        self.sprite.angle = angle
        self.sprite.change_x = x_speed

    #Wraps around edge of screen
    def wraps_screen(self):
        if self.sprite.left > constants.SCREEN_WIDTH:
            self.sprite.right = 0
        elif self.sprite.right < 0:
            self.sprite.left = constants.SCREEN_WIDTH