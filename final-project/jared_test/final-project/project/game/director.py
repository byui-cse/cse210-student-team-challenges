import arcade
import os
from game import constants

class Director(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        self.player_list = None
        self.stone_list = None
        self.car_list = None
        self.cloud_list = None
        self.street_list = None

        self.player_sprite = None
        self.score = 0
        self.level = 0

        self.stone_sprite = None
        self.stone_amount = 0

        self.car_sprite = None
        self.cloud_sprite = None
        self.street_sprite = None
        
    def setup(self):
        base = constants.get_base()
        self.background = arcade.load_texture(f"{base}/background.png")

        self.player_list = arcade.SpriteList()
        self.stone_list = arcade.SpriteList()
        self.car_list = arcade.SpriteList()
        self.cloud_list = arcade.SpriteList()
        self.street_list = arcade.SpriteList()
        self.score = 0
        self.level = 1
        self.stone_amount = 10

        self.player_sprite = arcade.Sprite(f"{base}/bird.png", constants.PLAYER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 525
        self.player_sprite.change_x = constants.PLAYER_SPEED
        self.player_list.append(self.player_sprite)

        car_coordinate_list = [[200, 70],
                           [700, 90]]

        for coordinate in car_coordinate_list:
            self.car_sprite = arcade.Sprite(f"{base}/car1.png",  constants.CAR_SCALING)
            self.car_sprite.position = coordinate
            self.car_sprite.change_x = constants.CAR_SPEED
            self.car_list.append(self.car_sprite)

        cloud_coordinate_list = [[100, 400],
                           [700, 450]]

        for coordinate in cloud_coordinate_list:
            self.cloud_sprite = arcade.Sprite(f"{base}/cloud.png", constants.CLOUD_SCALING)
            self.cloud_sprite.position = coordinate
            self.cloud_sprite.change_x = constants.CLOUD_SPEED
            self.cloud_list.append(self.cloud_sprite)

        self.street_sprite = arcade.Sprite(f"{base}/street.png", constants.STREET_SCALING)
        self.street_sprite.center_x = 400
        self.street_sprite.center_y = 300
        self.street_list.append(self.street_sprite)

    def on_key_press(self, key, modifiers):
        base = constants.get_base()
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = constants.PLAYER_SPEED
            self.player_sprite.angle = 0
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.PLAYER_SPEED
            self.player_sprite.angle = 180
        elif key == arcade.key.SPACE:
            self.stone_sprite = arcade.Sprite(f"{base}/stone.png", constants.STONE_SCALING)
            self.stone_sprite.center_x = self.player_sprite.center_x
            self.stone_sprite.center_y = self.player_sprite.center_y
            self.stone_sprite.change_y = -constants.STONE_SPEED
            if len(self.stone_list) < 1:
                self.stone_list.append(self.stone_sprite)
                self.stone_amount -= 1

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = constants.PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.PLAYER_SPEED

    def on_update(self, delta_time: float = 1 / 60):
        self.player_list.update()
        self.stone_list.update()
        self.car_list.update()
        self.cloud_list.update()
        self.street_list.update()

        if self.player_sprite.center_x > constants.SCREEN_WIDTH:
            self.player_sprite.change_x = -constants.PLAYER_SPEED
            self.player_sprite.angle = 180
        elif self.player_sprite.center_x < (constants.SCREEN_WIDTH -800):
            self.player_sprite.change_x = constants.PLAYER_SPEED
            self.player_sprite.angle = 0

        self.new_speed = (constants.STONE_SPEED + 3)

        for stone in self.stone_list:
            self.collision_list = arcade.check_for_collision_with_list(stone, self.cloud_list)
            
            if len(self.collision_list) > 0:
                self.stone_sprite.center_y = self.new_speed

        current_speed = (constants.CAR_SPEED + self.level)

        for self.car_sprite in self.car_list:
            if self.car_sprite.center_x > constants.SCREEN_WIDTH:
                self.car_sprite.change_x = -current_speed
            elif self.car_sprite.center_x < (constants.SCREEN_WIDTH -800):
                self.car_sprite.change_x = current_speed

        for self.cloud_sprite in self.cloud_list:
            if self.cloud_sprite.center_x > constants.SCREEN_WIDTH:
                self.cloud_sprite.change_x = constants.CLOUD_SPEED
            elif self.cloud_sprite.center_x < (constants.SCREEN_WIDTH -800):
                self.cloud_sprite.change_x = -constants.CLOUD_SPEED

        for stone in self.stone_list:
            self.collision_list = arcade.check_for_collision_with_list(stone, self.car_list)
            
            if len(self.collision_list) > 0:
                stone.remove_from_sprite_lists()
                self.score += 1
                self.level += 1
                self.stone_amount += 2

        for stone in self.stone_list:
            self.collision_list = arcade.check_for_collision_with_list(stone, self.street_list)
            
            if len(self.collision_list) > 0:
                stone.remove_from_sprite_lists()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        self.street_list.draw()
        self.stone_list.draw()
        self.player_list.draw()
        self.car_list.draw()
        self.cloud_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 25, 560, arcade.color.WHITE, 14)
        output = f"LEVEL {self.level}"
        arcade.draw_text(output, 345, 560, arcade.color.WHITE, 22)
        output = f"Stones: {self.stone_amount}"
        arcade.draw_text(output, 690, 560, arcade.color.WHITE, 14)
        if self.stone_amount <= 0:
            output = "GAME OVER"
            arcade.draw_text(output, 200, 300, arcade.color.RED, 50)