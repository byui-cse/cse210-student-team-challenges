import arcade
import random

from scaling import SCREEN_HEIGHT, SCREEN_WIDTH, SCALING, SPRITE_SCALING
from obstacles import Obstacle
from room import Room
from weapon import Weapon
from obstacles_lists import boxes_room1

SCREEN_TITLE = "The remixed Legend of Zelda"


class ZeldaGame(arcade.Window):

    def __init__(self, width, height, title):
        """Initialize the game
        """

        super().__init__(width, height, title)

        self.enemies_list = arcade.SpriteList()
        self.missile_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.room = Room("project/images/zelda/room1.png")
        self.physics_engine = None
        # file_path = os.path.dirname(os.path.abspath(__file__))
        # os.chdir(file_path)


    def setup(self):
        """Get the game ready to play
        """

         # Set up the player
        self.player = arcade.Sprite("project/images/zelda/front_run1.png", SCALING/2.5)
        self.player.center_y = self.height/2
        self.player.left = 10
        self.all_sprites.append(self.player)
        self.paused = False

        # Spawn a new enemy every 3 seconds
        arcade.schedule(self.add_enemy, 2)

        for box in boxes_room1:
            self.box_room1 = Obstacle('project/images/zelda/metal_box.png')
            self.box_room1.position_obstacle(box[0], box[1])
            self.room.add_sprite(self.box_room1.obstacle)

        # self.obstacle1 =
        # self.obstacle1.position_obstacle(1, 1)

        # self.obstacle2 = Obstacle('images/zelda/metal_box.png')
        # self.obstacle2.position_obstacle(50, 1)

        # self.obstacle3 = Obstacle('images/zelda/metal_box.png')
        # self.obstacle3.position_obstacle(1, 50)
        
        # self.obstacle4 = Obstacle('images/zelda/metal_box.png')
        # self.obstacle4.position_obstacle(50, 50)


        # self.room.add_sprite(self.obstacle1.obstacle)
        # self.room.add_sprite(self.obstacle2.obstacle)
        # self.room.add_sprite(self.obstacle3.obstacle)
        # self.room.add_sprite(self.obstacle4.obstacle)

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.room.sprite_list)

        # Set the background colour
        # arcade.set_background_color(arcade.color.ARMY_GREEN)

# ########## Load background music
# ########## Sound source: http://ccmixter.org/files/Apoxode/59262
# ########## License: https://creativecommons.org/licenses/by/3.0/

        # self.background_music = arcade.load_sound(
        #     "project/sounds/Apoxode_-_Electric_1.wav"
        # )

# ########## Load all the sounds
# ########## Sound sources: Jon Fincher
#         self.collision_sound = arcade.load_sound("sounds/Collision.wav")
#         self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
#         self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")


# ########## Play the background music and schedule the loop
    #     self.play_background_music()
    #     arcade.schedule(self.play_background_music, 15)

    # def play_background_music(self, delta_time: int = 0):
    #     """Starts playing the background music
    # """
    #     self.background_music.play()

    def fire_missile(self):
        """Fires a missile against the incoming enemies
        """
        if self.paused:
            return

        missile = Weapon("project/images/zelda/arrow.png", SCALING)

        missile.center_x = self.player.center_x
        missile.center_y = self.player.center_y - 5
        missile.velocity = (500, 0)

        self.missile_list.append(missile)
        self.all_sprites.append(missile)

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen
    Arguments:
        delta_time {float} -- How much time has passed since the last call
    """

        if self.paused:
            return

        # First, create the the new enemy sprite
        enemy = Obstacle("project/images/monster1.png")

        # Set its position to a random height and off screen right
        enemy.position_obstacle(600, 150)
        # Set its speed to a random speed heading left
        # enemy.velocity = (random.randint(-200, -80), 0)

        # Add it to the enemies list
        self.enemies_list.append(enemy.obstacle)
        self.all_sprites.append(enemy.obstacle)
    
    def on_key_press(self, symbol, modifiers):

        """Handle user keyboard input
        Q: Quit the game
        P: Pause/unpause the game
        W/A/S/D: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right
        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """

        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.SPACE:
            self.fire_missile()

        if symbol == arcade.key.W or symbol == arcade.key.UP:
            # self.move_up_sound.play()
            self.player.change_y = 5
        elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -5
        elif symbol == arcade.key.S or symbol == arcade.key.DOWN:
            # self.move_down_sound.play()
            self.player.change_y = -5
        elif symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released
        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (
            symbol == arcade.key.W
            or symbol == arcade.key.S
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
            symbol == arcade.key.A
            or symbol == arcade.key.D
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        """Update all game objects
        """
        if self.paused:
            return

        # This line of code prevents player to go through the obstaclees
        self.physics_engine.update()


        if self.player.collides_with_list(self.enemies_list):
            # self.collision_sound.play()
            # Stop the game and schedule the game close
            self.paused = True
            arcade.schedule(lambda delta_time: arcade.close_window(), 0.5)

        for enemy in self.enemies_list:
            collisions = enemy.collides_with_list(self.missile_list)
            if collisions:
                enemy.remove_from_sprite_lists()
                for missile in collisions:
                    missile.remove_from_sprite_lists()

        # Update everything
        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )

        if self.player.top > self.height:
            self.player.top = self.height
        elif self.player.bottom < 0:
            self.player.bottom = 0
        
        if self.player.left < 0:
            self.player.left = 0
        elif self.player.right > self.width:
            self.player.right = self.width

        
    
    def on_draw(self):
        """Draw all game objects
        """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.room.background)
        # Draw all the walls in this room
        self.room.sprite_list.draw()

        self.all_sprites.draw()


if __name__ == "__main__":
    app = ZeldaGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    app.setup()
    arcade.run()