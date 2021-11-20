from game.player import Player
from game.background import Background
from game.platforms import Platforms
from game import K

import arcade
import time

class Screen(arcade.Window):
    #The inheritance of the window class automatically starts the screen
    #Is important to notice that the method arcade.open_window is in the arcade.Window class
    #Also is important to notice that the Window class creates the window in the __init__
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        #Creating an instance that manages the players
        self.sprite_list = arcade.SpriteList()
        #Setting Background color
        arcade.set_background_color(arcade.color.BLACK)

        # Move this elsewhere
        self.platforms = Platforms.make_platforms(K.SCREEN_WIDTH * 5, 0, (106, 106, 86), 0.7, 0.5)

        self.physics_engine = None
        self.scene = None

    def setup(self):

        # Initialize Scene
        self.scene = arcade.Scene()

        # Find some kind of fire
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.2) # Last parameter is for resizing.
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

    
    def create_player(self):
        
        """Create the player sprite, specify his position and append it to the list of all sprites"""
        self.player = Player("project/game/images/player.png", K.SPRITE_SCALING) #THE PLAYER OBJECT
        self.player.center_x = 64
        self.player.center_y = 128
        self.sprite_list.append(self.player)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player, gravity_constant=K.GRAVITY, walls=self.scene["Walls"]
        )

    def draw_background(self):
        self.background = Background("project/game/images/lab_background.png", K.BACKGROUND_SCALE)
        self.background.center_y = 280 #Sets the y and x position of the sprite
        self.background.left = 0
        self.sprite_list.append(self.background)
        
    def on_draw(self):
        """
        Render the screen, and show the sprites with the .draw() method
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        self.sprite_list.draw()
        self.scene.draw()

        # Draw all the sprites.
        # self.platforms.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = K.PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -K.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = K.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player.change_x = 0

        self.background = Background("project/game/images/lab_background.png", K.BACKGROUND_SCALE)
        self.background.center_y = 280 #Sets the y and x position of the sprite

        self.background.left = 0
        self.sprite_list.append(self.background)

=======
>>>>>>> a971626 (Physics engine done)
    def on_update(self, delta_time):
        """ Update the movement data done in the key detecting functions"""

        # Move the player
        self.physics_engine.update()
        self.sprite_list.update()
        
        # Allow the platforms to keeep moving           
        self.platforms.center_x -= 1   
    
