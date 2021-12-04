import arcade
from game import constants

class Meteor(arcade.Sprite):
    """A code template for the meteor sprite. The responsibility of 
    this class of objects is to setup the meteor sprite.
    """
    def __init__(self, x_value,y_value, x_speed):
        """The class constructor.
        
        Args:
            self (Meteor): an instance of Meteor.
        """
        #Set sprite and scale
        self.sprite = arcade.Sprite(":resources:images/space_shooter/meteorGrey_big3.png", constants.METEOR_SCALING)

        #Initialize Position, direction, speed
        self.sprite.center_x = x_value
        self.sprite.center_y = y_value
        self.sprite.change_x = x_speed

    #Wraps around edge of screen
    def wraps_screen(self):
        if self.sprite.left > constants.SCREEN_WIDTH:
            self.sprite.right = 0
        elif self.sprite.right < 0:
            self.sprite.left = constants.SCREEN_WIDTH