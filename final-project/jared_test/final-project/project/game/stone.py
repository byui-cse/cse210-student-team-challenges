import arcade
from game import constants

class Director(arcade.Window):

    def __init__(self):
        self.stone_list = None
        self.stone_sprite = None
        self.stone_amount = 0
        
    def setup(self):
        self.stone_list = arcade.SpriteList()
        self.stone_amount = 10

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.stone_sprite = arcade.Sprite("cse210-student-team-challenges/final-project/jared_test/final-project/project/game/assets/sprites/stone.png", constants.STONE_SCALING)
            self.stone_sprite.center_x = self.player_sprite.center_x
            self.stone_sprite.center_y = self.player_sprite.center_y
            self.stone_sprite.change_y = -constants.STONE_SPEED
            if len(self.stone_list) < 1:
                self.stone_list.append(self.stone_sprite)
                self.stone_amount -= 1

    def on_update(self, delta_time):
        self.stone_list.update()

        for stone in self.stone_list:
            self.collision_list = arcade.check_for_collision_with_list(stone, self.car_list)
            
            if len(self.collision_list) > 0:
                stone.remove_from_sprite_lists()
                self.score += 1

        for stone in self.stone_list:
            self.collision_list = arcade.check_for_collision_with_list(stone, self.street_list)
            
            if len(self.collision_list) > 0:
                stone.remove_from_sprite_lists()

    def on_draw(self):
        arcade.start_render()
        self.stone_list.draw()