import arcade
from game import constants

class Ship(arcade.Sprite):
    """A code template for the ship sprite. The responsibility of 
    this class of objects is to setup the ship sprite.
    """
    def __init__(self, x_value, y_value, angle, x_speed):
        """The class constructor.
        
        Args:
            self (Ship): an instance of Ship.
        """
        #Set sprite and scale
        self.ship = arcade.Sprite(":resources:images/space_shooter/playerShip2_orange.png", constants.SHIP_SCALING)
        self.bomb = arcade.Sprite(":resources:images/topdown_tanks/tankRed_barrel1_outline.png", constants.BOMB_SCALING)

        #Set sound effect
        self.sound = arcade.Sound(":resources:sounds/lose4.wav")

        #Initialize Position, direction, speed
        self.ship.center_x = x_value
        self.ship.center_y = y_value
        self.ship.angle = angle
        self.ship.change_x = x_speed

    #Wraps around edge of screen
    def wraps_screen(self):
        if self.ship.left > constants.SCREEN_WIDTH:
            self.ship.right = 0
        elif self.ship.right < 0:
            self.ship.left = constants.SCREEN_WIDTH

    #Movement and actions
    def move_right(self):
        self.ship.change_x = constants.SHIP_SPEED
        self.ship.angle = 270

    def move_left(self):
        self.ship.change_x = -constants.SHIP_SPEED
        self.ship.angle = 90

    def drop_bomb(self):
        self.bomb.center_x = self.ship.center_x
        self.bomb.center_y = self.ship.center_y
        self.sound.play()
        self.bomb.change_y = constants.BOMB_SPEED