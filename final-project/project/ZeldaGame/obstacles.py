import arcade

class Obstacle(arcade.Sprite):
    
    def __init__(self, filename, sprite_scaling):
    
        super().__init__(filename, sprite_scaling)
        self.moving_left = True
        self.moving_right = False

    def position_obstacle(self, left, bottom):
        self.left = left
        self.bottom = bottom