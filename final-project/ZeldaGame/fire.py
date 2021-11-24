from abc import ABC, abstractmethod

class Fire(ABC):

    @abstractmethod
    def shoot(self):
        pass

class Shooter:

    def __init__(self, weapon):
        self.__weapon = weapon

    def do_shoot(self, player, artillery, artillery_list, all_sprites):
        result = self.__weapon.shoot(player, artillery, artillery_list, all_sprites)
        return result


class ShootUp(Fire):

    def shoot(self, player, artillery, artillery_list, all_sprites):
        artillery.center_x = player.center_x
        artillery.center_y = player.center_y - 5
        artillery.change_y = 500
        artillery.change_angle = 90

        artillery_list.append(artillery)
        all_sprites.append(artillery)

class ShootDown(Fire):

    def shoot(self, player, artillery, artillery_list, all_sprites):
    
        artillery.center_x = player.center_x
        artillery.center_y = player.center_y - 5
        artillery.change_y = -500
        artillery.change_angle = 90

        artillery_list.append(artillery)
        all_sprites.append(artillery)

class ShootLeft(Fire):

    def shoot(self, player, artillery, artillery_list, all_sprites):
        artillery.center_x = player.center_x
        artillery.center_y = player.center_y - 5
        artillery.change_x = -500
        artillery.change_angle = 180

        artillery_list.append(artillery)
        all_sprites.append(artillery)

class ShootRight(Fire):
    
    def shoot(self, player, artillery, artillery_list, all_sprites):
        artillery.center_x = player.center_x
        artillery.center_y = player.center_y - 5
        artillery.velocity = (500, 0)

        artillery_list.append(artillery)
        all_sprites.append(artillery)