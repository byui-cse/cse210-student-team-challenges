import arcade
from game import constants

class Director(arcade.Window):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.stone_sprite = None
        
    def setup(self):
        self.score = 0

    def on_update(self, delta_time):

        for stone in self.stone_list:
            self.collision_list = arcade.check_for_collision_with_list(stone, self.car_list)
            
            if len(self.collision_list) > 0:
                stone.remove_from_sprite_lists()
                self.score += 1

    def on_draw(self):
        arcade.start_render()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 25, 570, arcade.color.WHITE, 14)