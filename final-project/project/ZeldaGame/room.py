import arcade
from abstract_object import MainObjects

class Room(MainObjects):

    def __init__(self, background):
        self.__wall_list = arcade.SpriteList()
        self.background = arcade.load_texture(f"{background}")
    
    @property
    def sprite_list(self):
        return self.__wall_list
    
    def add_sprite(self, sprite_object):
        sprite = sprite_object
        self.__wall_list.append(sprite)