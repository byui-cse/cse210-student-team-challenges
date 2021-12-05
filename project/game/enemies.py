import arcade
from game import K

class Enemies(arcade.Sprite):
    UP = True      
    def update(self):
        super().update()
        
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > K.SCREEN_HEIGHT - 1:
            self.top = K.SCREEN_HEIGHT - 1


        