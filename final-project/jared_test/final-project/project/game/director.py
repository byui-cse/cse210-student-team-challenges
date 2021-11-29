import arcade
from game import constants

class Director(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        self.player_list = None
        self.bomb_list = None
        self.meteor_list = None
        self.saucer_list = None
        self.surface_list = None
        self.surfArt_list = None
        self.star_list = None
        self.game_over = False


        self.background_music = arcade.Sound(":resources:music/funkyrobot.mp3")
        self.drop_bomb_sound = arcade.Sound(":resources:sounds/lose4.wav")
        self.hit_meteor_sound = arcade.Sound(":resources:sounds/hurt1.wav")
        self.hit_saucer_sound = arcade.Sound(":resources:sounds/hit1.wav")
        self.hit_surface_sound = arcade.Sound(":resources:sounds/hurt1.wav")
        self.game_over_sound = arcade.Sound(":resources:sounds/gameover3.wav")


        self.player_sprite = None
        self.score = 0
        self.level = 0


        self.bomb_sprite = None
        self.bomb_amount = 0


        self.meteor_sprite = None
        self.saucer_sprite = None
        self.surface_sprite = None
        self.surfArt_sprite = None
        self.star_sprite = None


    def setup(self):
        self.background = arcade.set_background_color(arcade.csscolor.BLACK)
        self.background_music.play()
        self.player_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.saucer_list = arcade.SpriteList()
        self.surface_list = arcade.SpriteList()
        self.surfArt_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.score = 0
        self.level = 1
        self.bomb_amount = 10


        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip2_orange.png", constants.PLAYER_SCALING)
        self.player_sprite.angle = 270
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 500
        self.player_sprite.change_x = constants.PLAYER_SPEED
        self.player_list.append(self.player_sprite)

        
        meteor_coordinate_list = [[100, 310],
                           [700, 400]]
        for coordinate in meteor_coordinate_list:
            self.meteor_sprite = arcade.Sprite(":resources:images/space_shooter/meteorGrey_big3.png", constants.METEOR_SCALING)
            self.meteor_sprite.position = coordinate
            self.meteor_sprite.change_x = constants.METEOR_SPEED
            self.meteor_list.append(self.meteor_sprite)

        
        saucer_coordinate_list = [[200, 60],
                           [700, 105]]
        for coordinate in saucer_coordinate_list:
            self.saucer_sprite = arcade.Sprite(":resources:images/tiles/switchGreen.png",  constants.SAUCER_SCALING)
            self.saucer_sprite.position = coordinate
            self.saucer_sprite.change_x = constants.SAUCER_SPEED
            self.saucer_list.append(self.saucer_sprite)

        #Place surface art only
        for x in range(0, 820, 20):
            self.surfArt_sprite = arcade.Sprite(":resources:images/tiles/sandCenter_rounded.png", constants.SURFACE_SCALING)
            self.surfArt_sprite.center_x = x
            self.surfArt_sprite.center_y = 20
            self.surfArt_list.append(self.surfArt_sprite)

        #Place real collidable surface
        for x in range(0, 820, 20):
            self.surface_sprite = arcade.Sprite(":resources:images/tiles/sandCenter_rounded.png", constants.SURFACE_SCALING)
            self.surface_sprite.center_x = x
            self.surface_sprite.center_y = 0
            self.surface_list.append(self.surface_sprite)


        for x in range(25, 800, 250):
                    for y in range(0, 600, 130):
                        self.star_sprite = arcade.Sprite(":resources:onscreen_controls/shaded_light/unchecked.png", constants.STAR_SCALING)
                        self.star_sprite.center_x = x
                        self.star_sprite.center_y = y
                        self.star_list.append(self.star_sprite)


    def on_key_press(self, key, modifiers):
        if self.game_over == False:
            if key == arcade.key.RIGHT:
                self.player_sprite.change_x = constants.PLAYER_SPEED
                self.player_sprite.angle = 270
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -constants.PLAYER_SPEED
                self.player_sprite.angle = 90
            elif key == arcade.key.SPACE:
                self.bomb_sprite = arcade.Sprite(":resources:images/topdown_tanks/tankRed_barrel1_outline.png", constants.BOMB_SCALING)
                self.bomb_sprite.center_x = self.player_sprite.center_x
                self.bomb_sprite.center_y = self.player_sprite.center_y
                self.bomb_sprite.change_y = -constants.BOMB_SPEED
                if len(self.bomb_list) < 1:
                    self.bomb_list.append(self.bomb_sprite)
                    self.drop_bomb_sound.play()
                    self.bomb_amount -= 1


    def on_key_release(self, key, modifiers):
        if self.game_over == False:
            if key == arcade.key.RIGHT:
                self.player_sprite.change_x = constants.PLAYER_SPEED
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -constants.PLAYER_SPEED


    def on_update(self, delta_time: float = 1 / 60):
        self.player_list.update()
        self.bomb_list.update()
        self.meteor_list.update()
        self.saucer_list.update()
        self.surface_list.update()
        self.surfArt_list.update()
        self.star_list.update()


        if self.player_sprite.center_x > constants.SCREEN_WIDTH:
            self.player_sprite.change_x = -constants.PLAYER_SPEED
            self.player_sprite.angle = 90
        elif self.player_sprite.center_x < (constants.SCREEN_WIDTH -800):
            self.player_sprite.change_x = constants.PLAYER_SPEED
            self.player_sprite.angle = 270


        for bomb in self.bomb_list:
            self.meteor_collision_list = arcade.check_for_collision_with_list(bomb, self.meteor_list)
            if len(self.meteor_collision_list) > 0:
                bomb.remove_from_sprite_lists()
                self.hit_meteor_sound.play()
                if self.bomb_amount == 0:
                    self.game_over = True
                    self.game_over_sound.play()


            self.surface_collision_list = arcade.check_for_collision_with_list(bomb, self.surface_list)
            if len(self.surface_collision_list) > 0:
                bomb.remove_from_sprite_lists()
                self.hit_surface_sound.play()
                if self.bomb_amount == 0:
                    self.game_over = True
                    self.game_over_sound.play()
        

            self.saucer_collision_list = arcade.check_for_collision_with_list(bomb, self.saucer_list)
            if len(self.saucer_collision_list) > 0:
                bomb.remove_from_sprite_lists()
                self.hit_saucer_sound.play()
                self.score += 1
                self.level += 1
                self.bomb_amount += 2


        for self.meteor_sprite in self.meteor_list:
            if self.meteor_sprite.center_x > constants.SCREEN_WIDTH:
                self.meteor_sprite.change_x = constants.METEOR_SPEED
            elif self.meteor_sprite.center_x < (constants.SCREEN_WIDTH -800):
                self.meteor_sprite.change_x = -constants.METEOR_SPEED


        current_speed = (constants.SAUCER_SPEED + self.level)
        for self.saucer_sprite in self.saucer_list:
            if self.saucer_sprite.center_x > constants.SCREEN_WIDTH:
                self.saucer_sprite.change_x = -current_speed
            elif self.saucer_sprite.center_x < (constants.SCREEN_WIDTH -800):
                self.saucer_sprite.change_x = current_speed


    def on_draw(self):
        arcade.start_render()
        self.star_list.draw()
        self.surface_list.draw()
        self.surfArt_list.draw()
        self.bomb_list.draw()
        self.player_list.draw()
        self.saucer_list.draw()
        self.meteor_list.draw()


        output = f"Score: {self.score}"
        arcade.draw_text(output, 25, 560, arcade.color.WHITE, 14)
        output = f"LEVEL {self.level}"
        arcade.draw_text(output, 345, 560, arcade.color.WHITE, 22)
        output = f"Stones: {self.bomb_amount}"
        arcade.draw_text(output, 690, 560, arcade.color.WHITE, 14)
        if self.game_over == True:
            output = "GAME OVER"
            arcade.draw_text(output, 200, 300, arcade.color.RED, 50)