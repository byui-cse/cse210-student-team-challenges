import arcade
from ZeldaGame.abstract_object import MainObjects

class Room(MainObjects):

    def __init__(self, background):
        self.__wall_list = arcade.SpriteList()
        self.__wall_to_remove = arcade.SpriteList()
        self.__list_of_enemies = []
        self.background = arcade.load_texture(f"{background}")
    
    @property
    def sprite_list(self):
        return self.__wall_list

    @property
    def wall_to_remove(self):
        return self.__wall_to_remove
    
    @property
    def list_of_enemies(self):
        return self.__list_of_enemies
    
    def add_sprite(self, sprite_object):
        sprite = sprite_object
        self.__wall_list.append(sprite)
    
    def add_wall_to_remove(self, sprite_object):
        sprite_new = sprite_object
        self.__wall_to_remove.append(sprite_new)

    def remove_walls(self, counter):

        if len(self.__list_of_enemies) == counter:
            for i in self.__wall_to_remove:
                self.__wall_to_remove.remove(i)
        else:
            return