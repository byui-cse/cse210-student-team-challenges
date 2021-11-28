import arcade
from game import constants

class Bird(arcade.Sprite):

    def __init__(self):

        super().__init__()

        self.player_list = None
        self.player_sprite = None
     
    def setup(self):
        self.player_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("cse210-student-team-challenges/final-project/jared_test/final-project/project/game/assets/sprites/bird.png", constants.PLAYER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 525
        self.player_sprite.change_x = constants.PLAYER_SPEED
        self.player_list.append(self.player_sprite)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = constants.PLAYER_SPEED
            self.player_sprite.angle = 0
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.PLAYER_SPEED
            self.player_sprite.angle = 180

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = constants.PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.PLAYER_SPEED

    def on_update(self, delta_time):
        self.player_list.update()

        if self.player_sprite.center_x > constants.SCREEN_WIDTH:
            self.player_sprite.change_x = -constants.PLAYER_SPEED
            self.player_sprite.angle = 180
        elif self.player_sprite.center_x < (constants.SCREEN_WIDTH -800):
            self.player_sprite.change_x = constants.PLAYER_SPEED
            self.player_sprite.angle = 0

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()