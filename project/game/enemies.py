import arcade
import K

class Enemies():
    pass
    def __init__(self):
        self.enemies_list = arcade.SpriteList()
    def setup(self):
        enemy = ":resources:images/enemies/mouse.png"
        enemy.center_x = 64
        enemy.center_y = 150
        self.enemies_list.append(enemy)
        arcade.start_render()
        self.enemies_list.draw()
        self.enemies_list.draw()