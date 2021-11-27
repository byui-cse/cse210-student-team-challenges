import arcade
from ZeldaGame.scaling import SCREEN_WIDTH

class Enemy(arcade.Sprite):
    
    def __init__(self, filename, sprite_scaling):
    
        super().__init__(filename, sprite_scaling)
        self.moving_left = True
        self.moving_right = False
        self.health = 2

    def position_enemy(self, left, bottom):
        self.left = left
        self.bottom = bottom

    def update(self, factor, collide_at):

        if self.center_x > collide_at and self.moving_left == True:
            self.moving_right = False
            self.center_x -= factor

        if self.center_x < collide_at:
            self.moving_right = True
        
        if self.moving_right:
            self.moving_left = False
            self.center_x += factor

        if self.center_x > SCREEN_WIDTH - collide_at:
            self.moving_left = True
            self.moving_right = False
            self.center_x -= factor