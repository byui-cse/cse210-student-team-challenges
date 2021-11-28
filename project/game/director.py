from game.player import Player
from game.background import Background
from game.sounds import Sounds
from game.platforms import Platforms
from game.enemies import Enemies
from game import K


import arcade
import random

class Screen(arcade.Window):
    #The inheritance of the window class automatically starts the screen
    #Is important to notice that the method arcade.open_window is in the arcade.Window class
    #Also is important to notice that the Window class creates the window in the __init__
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        # Creating an instance that manages the sprites
        self.sprite_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()
        self.sounds = Sounds()
        self.enemies = Enemies()

        self.physics_engine = None
        self.scene = None

        self.sounds.play_music()
    def setup(self):
        # Initialize Scene
        self.scene = arcade.Scene()

        # Populate the ground with spikes
        for x in range(0, 1250, 37):
            wall1 = arcade.Sprite("project\game\images\metalblock.png", 0.2) # Last parameter is for resizing (optional)
            wall1.center_x = x
            wall1.center_y = 15

            self.scene.add_sprite("Walls", wall1)
        for y in range(0,7):
            block = arcade.Sprite("project/game/images/rockblock.jpg",0.2)
            block.center_x = random.randint(50, 990)
            block.center_y = random.randint(15, 490)
            self.scene.add_sprite("Walls", block)
            
        # Create the platforms
        self.platforms = Platforms.make_platforms(K.SCREEN_WIDTH * 5, 0, arcade.color.ARSENIC, 0.7, 0.5)
        # Platforms are still not "solid"
        # self.scene.add_sprite("Walls", self.platforms)   
        for z in range(0,3):
            self.enemy = Enemies("project/game/images/podooboo.png", K.ENEMY_SCALING)
            self.enemy.center_x = random.randint(90, 990)
            self.enemy.center_y = random.randint(60, 70)
            self.enemies_list.append(self.enemy)
             
    def create_player(self):
        """Create the player sprite, specify his position and append it to the list of all sprites"""
        self.player = Player(":resources:images/animated_characters/robot/robot_walk0.png", K.SPRITE_SCALING) #THE PLAYER OBJECT
        self.player.center_x = 64
        self.player.center_y = 128
        self.sprite_list.append(self.player)

        # Adds physics engine to the player
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player, gravity_constant=K.GRAVITY, walls=self.scene["Walls"]
        )

    def draw_background(self):
        #Setting Background color, only needed if the background is not callable
        arcade.set_background_color(arcade.color.BLACK)

        self.background = Background("project/game/images/lab_background.png", K.BACKGROUND_SCALE)
        self.background.center_y = 280 #Sets the y and x position of the sprite
        self.background.left = 0
        self.background_list.append(self.background)
                        
    def on_draw(self):
        """
        Render the screen, and show the sprites with the .draw() method
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        
        # Draw all the sprites.
        self.background_list.draw()
        self.platforms.draw()
        self.sprite_list.draw()
        self.scene.draw()
        self.enemies_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = K.PLAYER_JUMP_SPEED
            self.player.change_y = K.PLAYER_JUMP_SPEED
            self.sounds.play_jump_sound()
        elif key == arcade.key.DOWN:
            self.player.change_y = -K.MOVEMENT_SPEED

        elif key == arcade.key.LEFT:
            self.player.change_x = -K.MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            self.player.change_x = K.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_update(self, delta_time):
        """ Update the movement data done in the key detecting functions"""
        # Move the player
        self.physics_engine.update()
        self.sprite_list.update()

        # Allow the platforms to keeep moving      
        self.platforms.center_x -= K.PLATFORM_SPEED

        #Enemy moving
    
        UP = True
        for a in self.enemies_list:
            if a.top < K.SCREEN_HEIGHT and UP == True:
                a.center_y += 5
            if a.top > K.SCREEN_HEIGHT:
                UP = False
            if UP == False:
                a.center_y -= 5
            if a.bottom < 20:
                UP = True

        #collitions
        colliding = arcade.check_for_collision_with_list(self.player, self.enemies_list)
        if colliding:
            exit()    
