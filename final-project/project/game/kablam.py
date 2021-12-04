import arcade
from game import constants
from game.ship import Ship
from game.meteor import Meteor
from game.saucer import Saucer


class KablamGame(arcade.Window):
    """A code template for the game. The responsibility of 
    this class of objects is to control the sequence of play.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (KablamGame): an instance of KablamGame.
        """
        #Get screen dimensions and title
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        
        #Initialize sprite lists
        self.ship_list = None
        self.meteor_list = None
        self.saucer_list = None
        self.bomb_list = None
        self.surface_list = None
        self.star_list = None
        self.start_game = False
        self.game_over = False
        self.new_highscore = False
        self.saucer_struck = False

        #Music and sound effects
        self.background_music = arcade.Sound(":resources:music/funkyrobot.mp3")
        self.meteor_hit_sound = arcade.Sound(":resources:sounds/hit1.wav")
        self.saucer_hit_sound = arcade.Sound(":resources:sounds/explosion2.wav")
        self.surface_hit_sound = arcade.Sound(":resources:sounds/hurt1.wav")
        self.begin_game_sound = arcade.Sound(":resources:sounds/upgrade4.wav")
        self.game_over_sound = arcade.Sound(":resources:sounds/gameover3.wav")
        self.new_highscore_sound = arcade.Sound(":resources:sounds/upgrade5.wav")

        #Initialize sprites
        self.score = None
        self.highscore = None
        self.bomb_amount = None


    def setup(self):
        #Setup ambiance
        self.background = arcade.set_background_color(arcade.csscolor.BLACK)
        self.background_music.play()

        #Prepare lists to work with arcade
        self.ship_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.saucer_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.surface_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        #Prepare storage variables
        self.score = 0
        self.highscore = 80
        self.restart_timer = 0
        self.struck_timer = 0
        self.music_replay_timer = 0
        self.bomb_amount = 10

        #Place ship
        self.ship = Ship(64, 490, 270, constants.SHIP_SPEED)
        self.ship_list.append(self.ship.sprite)

        #Place meteors
        #Meteor 1
        self.meteor1 = Meteor(100, 310, constants.METEOR_SPEED)
        self.meteor_list.append(self.meteor1.sprite)
        #Meteor2
        self.meteor2 = Meteor(600, 400, constants.METEOR_SPEED)
        self.meteor_list.append(self.meteor2.sprite)

        #Place saucer
        self.saucer = Saucer(799, 100, 0, 3)
        self.saucer_list.append(self.saucer.sprite)

        #Place surface
        for x in range(0, 820, 20):
            self.surface_sprite = arcade.Sprite(":resources:images/tiles/sandCenter_rounded.png", constants.SURFACE_SCALING)
            self.surface_sprite.center_x = x
            self.surface_sprite.center_y = 20
            self.surface_list.append(self.surface_sprite)

        #Place stars in background
        for x in range(25, 800, 250):
                    for y in range(0, 600, 130):
                        self.star_sprite = arcade.Sprite(":resources:onscreen_controls/shaded_light/unchecked.png", constants.STAR_SCALING)
                        self.star_sprite.center_x = x
                        self.star_sprite.center_y = y
                        self.star_list.append(self.star_sprite)      
        for x in range(43, 800, 173):
                    for y in range(0, 600, 178):
                        self.star_sprite = arcade.Sprite(":resources:onscreen_controls/shaded_light/unchecked.png", constants.STAR_SCALING)
                        self.star_sprite.center_x = x
                        self.star_sprite.center_y = y
                        self.star_list.append(self.star_sprite)


    def on_key_press(self, key, modifiers):
        #While main screen is active
        if self.start_game == False:
            if key == arcade.key.RETURN:
                self.start_game = True
                self.begin_game_sound.play()

        #While gameplay is active
        if self.start_game == True:
            if self.game_over == False:
                if key == arcade.key.RIGHT:
                    self.ship.move_right()
                elif key == arcade.key.LEFT:
                    self.ship.move_left()
                elif key == arcade.key.SPACE:
                    if len(self.bomb_list) < 1:
                        self.ship.drop_bomb()
                        self.bomb_list.append(self.ship.bomb)
                        self.bomb_amount -= 1


    def on_key_release(self, key, modifiers):
        #While gameplay is active
        if self.start_game == True:
            if self.game_over == False:
                if key == arcade.key.RIGHT:
                    self.ship.move_right()
                elif key == arcade.key.LEFT:
                    self.ship.move_left()


    def on_update(self, delta_time: float = 1 / 60):
        #Check and update changes to sprite lists every frame
        self.ship_list.update()
        self.meteor_list.update()
        self.saucer_list.update()
        self.bomb_list.update()
        self.surface_list.update()
        self.star_list.update()

        #Ship wraps screen
        self.ship.wraps_screen()

        #Meteors wrap screen
        self.meteor1.wraps_screen()
        self.meteor2.wraps_screen()

        #Saucer wraps screen
        self.saucer.wraps_screen()

        #When bomb hits the meteor
        for bomb in self.bomb_list:
            self.meteor_collision_list = arcade.check_for_collision_with_list(bomb, self.meteor_list)
            if len(self.meteor_collision_list) > 0:
                bomb.remove_from_sprite_lists()
                self.meteor_hit_sound.play()
                if self.bomb_amount == 0:
                    self.game_over = True
                    if self.score > self.highscore:
                        self.new_highscore = True
                        self.highscore = self.score
                        self.new_highscore_sound.play()
                    elif self.score <= self.highscore:
                        self.new_highscore = False
                        self.game_over_sound.play()
        
            #When bomb hits the saucer
            self.new_speed = self.saucer.sprite.change_x
            self.saucer_collision_list = arcade.check_for_collision_with_list(bomb, self.saucer_list)
            if len(self.saucer_collision_list) > 0:
                bomb.remove_from_sprite_lists()
                self.saucer_struck = True
                self.saucer_hit_sound.play()
                self.score += 10
                self.new_speed = (self.saucer.sprite.change_x + 1)
                self.bomb_amount += 2

            #When bomb hits the planet surface
            self.surface_collision_list = arcade.check_for_collision_with_list(bomb, self.surface_list)
            if len(self.surface_collision_list) > 0:
                bomb.remove_from_sprite_lists()
                self.surface_hit_sound.play()
                if self.bomb_amount == 0:
                    self.game_over = True
                    if self.score > self.highscore:
                        self.new_highscore = True
                        self.highscore = self.score
                        self.new_highscore_sound.play()
                    elif self.score <= self.highscore:
                        self.new_highscore = False
                        self.game_over_sound.play()


        if self.game_over == True:
            self.restart_timer +=1


        if self.saucer_struck == True:
            self.struck_timer += 1

        #Loop background music
        self.music_replay_timer += 1
        if self.music_replay_timer == 12600:
            self.background_music.play()
            self.music_replay_timer = 0


    def on_draw(self):
        #Draw sprite list changes every frame
        arcade.start_render()

        self.star_list.draw()
        self.surface_list.draw()
        self.bomb_list.draw()
        self.ship_list.draw()
        self.saucer_list.draw()
        self.meteor_list.draw()

        #Draw saucer struck animation
        if self.saucer_struck == True:
            if self.struck_timer < 10:
                self.saucer.sprite.angle = -10
            elif self.struck_timer >= 10 and self.struck_timer < 20:
                self.saucer.sprite.angle = 10
            elif self.struck_timer >= 20:
                self.saucer.sprite.change_x = self.new_speed
                self.saucer.sprite.angle = 0
                self.struck_timer = 0
                self.saucer_struck = False

        #Draw information sprites near the top of the screen
        output = "Arrow Keys to Switch Direction -- Spacebar to Drop Bombs"
        arcade.draw_text(output, 160, 577, arcade.color.WHITE, 14)


        output = f"Score: {self.score}"
        arcade.draw_text(output, 25, 545, arcade.color.WHITE, 14)


        output = f"Bombs: {self.bomb_amount}"
        arcade.draw_text(output, 690, 545, arcade.color.WHITE, 14)

        #Start screen
        if self.start_game == False:
            output = "KABLAM!"
            arcade.draw_text(output, 110, 400, arcade.color.BLUE, 100)
            output = "Pess RETURN to Play"
            arcade.draw_text(output, 125, 240, arcade.color.YELLOW, 40)
            output = f"HIGHSCORE: {self.highscore}"
            arcade.draw_text(output, 290, 75, arcade.color.WHITE, 22)

        #Show score or new highscore when applicable
        if self.game_over == True:
            if self.restart_timer < 240:
                output = "GAME OVER"
                arcade.draw_text(output, 200, 350, arcade.color.RED, 50)
                if self.new_highscore == True:
                    output = f"NEW HIGHSCORE: {self.score}"
                    arcade.draw_text(output, 280, 150, arcade.color.GREEN, 22)
                elif self.new_highscore == False:
                    output = f"SCORE: {self.score}"
                    arcade.draw_text(output, 340, 150, arcade.color.WHITE, 22)
            #Reset back to beginning defaults
            elif self.restart_timer >= 240:
                self.score = 0
                self.bomb_amount = 10
                self.restart_timer = 0
                self.saucer.sprite.change_x = 3
                self.game_over = False
                self.new_highscore = False
                self.start_game = False