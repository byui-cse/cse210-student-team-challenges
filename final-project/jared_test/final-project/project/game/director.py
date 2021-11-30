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
        #Get screen dimensions and title
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        
        #Initialize sprite lists
        self.player_list = None
        self.bomb_list = None
        self.meteor_list = None
        self.saucer_list = None
        self.saucer2_list = None
        self.surface_list = None
        self.surfArt_list = None
        self.star_list = None
        self.start_game = False
        self.game_over = False
        self.new_highscore = False
        self.saucer_struck = False
        self.saucer2_struck = False

        #Music and sound effects
        self.background_music = arcade.Sound(":resources:music/funkyrobot.mp3")
        self.drop_bomb_sound = arcade.Sound(":resources:sounds/lose4.wav")
        self.hit_meteor_sound = arcade.Sound(":resources:sounds/hit1.wav")
        self.hit_saucer_sound = arcade.Sound(":resources:sounds/explosion2.wav")
        self.hit_surface_sound = arcade.Sound(":resources:sounds/hurt1.wav")
        self.begin_game_sound = arcade.Sound(":resources:sounds/upgrade4.wav")
        self.game_over_sound = arcade.Sound(":resources:sounds/gameover3.wav")
        self.new_highscore_sound = arcade.Sound(":resources:sounds/upgrade5.wav")

        #Initialize sprites
        self.player_sprite = None
        self.score = None
        self.highscore = None
        self.level = None
        self.bomb_sprite = None
        self.bomb_amount = None
        self.meteor_sprite = None
        self.saucer_sprite = None
        self.saucer2_sprite = None
        self.surface_sprite = None
        self.surfArt_sprite = None
        self.star_sprite = None


    def setup(self):
        #Setup ambiance
        self.background = arcade.set_background_color(arcade.csscolor.BLACK)
        self.background_music.play()

        #Prepare lists to work with arcade
        self.player_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.saucer_list = arcade.SpriteList()
        self.saucer2_list = arcade.SpriteList()
        self.surface_list = arcade.SpriteList()
        self.surfArt_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        #Prepare global storage variables
        self.score = 0
        self.highscore = 120
        self.level = 1
        self.restart_timer = 0
        self.struck_timer = 0
        self.struck2_timer = 0
        self.bomb_amount = 10

        #Place player character
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip2_orange.png", constants.PLAYER_SCALING)
        self.player_sprite.angle = 270
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 490
        self.player_sprite.change_x = constants.PLAYER_SPEED
        self.player_list.append(self.player_sprite)

        #Place meteors
        meteor_coordinate_list = [[100, 310],
                           [700, 400]]
        for coordinate in meteor_coordinate_list:
            self.meteor_sprite = arcade.Sprite(":resources:images/space_shooter/meteorGrey_big3.png", constants.METEOR_SCALING)
            self.meteor_sprite.position = coordinate
            self.meteor_sprite.change_x = constants.METEOR_SPEED
            self.meteor_list.append(self.meteor_sprite)

        #Place saucer 1
        self.saucer_sprite = arcade.Sprite(":resources:images/tiles/switchRed.png",  constants.SAUCER_SCALING)
        self.saucer_sprite.position = [200, 60]
        self.saucer_sprite.change_x = constants.SAUCER_SPEED
        self.saucer_list.append(self.saucer_sprite)

        #Place saucer 2
        self.saucer2_sprite = arcade.Sprite(":resources:images/tiles/switchGreen.png",  constants.SAUCER_SCALING)
        self.saucer2_sprite.position = [700, 100]
        self.saucer2_sprite.change_x = constants.SAUCER_SPEED
        self.saucer2_list.append(self.saucer2_sprite)

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
        #While gameplay is active
        if self.start_game == True:
            if self.game_over == False:
                if key == arcade.key.RIGHT:
                    self.player_sprite.change_x = constants.PLAYER_SPEED
                elif key == arcade.key.LEFT:
                    self.player_sprite.change_x = -constants.PLAYER_SPEED


    def on_update(self, delta_time: float = 1 / 60):
        #Check and update changes to sprite lists every frame
        self.player_list.update()
        self.bomb_list.update()
        self.meteor_list.update()
        self.saucer_list.update()
        self.saucer2_list.update()
        self.surface_list.update()
        self.surfArt_list.update()
        self.star_list.update()

        #Player sprite changes direction based on screen-edge collisions
        if self.player_sprite.center_x > constants.SCREEN_WIDTH:
            self.player_sprite.change_x = -constants.PLAYER_SPEED
            self.player_sprite.angle = 90
        elif self.player_sprite.center_x < (constants.SCREEN_WIDTH -800):
            self.player_sprite.change_x = constants.PLAYER_SPEED
            self.player_sprite.angle = 270

        #When bomb hits a meteor
        for bomb in self.bomb_list:
            self.meteor_collision_list = arcade.check_for_collision_with_list(bomb, self.meteor_list)
            if len(self.meteor_collision_list) > 0:
                bomb.remove_from_sprite_lists()
                self.hit_meteor_sound.play()
                if self.bomb_amount == 0:
                    self.game_over = True
                    if self.score > self.highscore:
                        self.new_highscore = True
                        self.highscore = self.score
                        self.new_highscore_sound.play()
                    elif self.score <= self.highscore:
                        self.new_highscore = False
                        self.game_over_sound.play()
        
            #When bomb hits saucers
            #Saucer 1
            self.saucer_collision_list = arcade.check_for_collision_with_list(bomb, self.saucer_list)
            if len(self.saucer_collision_list) > 0:
                bomb.remove_from_sprite_lists()
                self.saucer_struck = True
                self.hit_saucer_sound.play()
                self.score += 10
                self.level += 1
                self.bomb_amount += 2

            #Saucer 2
            self.saucer_collision_list = arcade.check_for_collision_with_list(bomb, self.saucer2_list)
            if len(self.saucer_collision_list) > 0:
                bomb.remove_from_sprite_lists()
                self.saucer2_struck = True
                self.hit_saucer_sound.play()
                self.score += 10
                self.level += 1
                self.bomb_amount += 2

            #When bomb hits the planet surface
            self.surface_collision_list = arcade.check_for_collision_with_list(bomb, self.surface_list)
            if len(self.surface_collision_list) > 0:
                bomb.remove_from_sprite_lists()
                self.hit_surface_sound.play()
                if self.bomb_amount == 0:
                    self.game_over = True
                    if self.score > self.highscore:
                        self.new_highscore = True
                        self.highscore = self.score
                        self.new_highscore_sound.play()
                    elif self.score <= self.highscore:
                        self.new_highscore = False
                        self.game_over_sound.play()

        #Meteors change direction based on screen_edge collisions
        for self.meteor_sprite in self.meteor_list:
            if self.meteor_sprite.center_x > constants.SCREEN_WIDTH:
                self.meteor_sprite.change_x = constants.METEOR_SPEED
            elif self.meteor_sprite.center_x < (constants.SCREEN_WIDTH -800):
                self.meteor_sprite.change_x = -constants.METEOR_SPEED

        #Saucers change direction based on screen-edge collisions
        #Saucer 1
        self.current_speed = (constants.SAUCER_SPEED + self.level)
        for self.saucer_sprite in self.saucer_list:
            if self.saucer_sprite.center_x > constants.SCREEN_WIDTH:
                self.saucer_sprite.change_x = -self.current_speed
                self.current_direction = 2
            elif self.saucer_sprite.center_x < (constants.SCREEN_WIDTH -800):
                self.saucer_sprite.change_x = self.current_speed
                self.current_direction = 1

        #Saucer 2
        self.current_speed = (constants.SAUCER_SPEED + self.level)
        for self.saucer2_sprite in self.saucer2_list:
            if self.saucer2_sprite.center_x > constants.SCREEN_WIDTH:
                self.saucer2_sprite.change_x = -self.current_speed
                self.current_direction2 = 2
            elif self.saucer2_sprite.center_x < (constants.SCREEN_WIDTH -800):
                self.saucer2_sprite.change_x = self.current_speed
                self.current_direction2 = 1


        if self.game_over == True:
            self.restart_timer +=1


        if self.saucer_struck == True:
            self.struck_timer += 1


        if self.saucer2_struck == True:
            self.struck2_timer += 1


    def on_draw(self):
        #Draw sprite list changes every frame
        arcade.start_render()
        self.star_list.draw()
        self.surface_list.draw()
        self.surfArt_list.draw()
        self.bomb_list.draw()
        self.player_list.draw()
        self.saucer2_list.draw()
        self.saucer_list.draw()
        self.meteor_list.draw()

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

        #Show score or highscore when applicable
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
            elif self.restart_timer >= 240:
                self.score = 0
                self.level = 1
                self.bomb_amount = 10
                self.restart_timer = 0
                self.game_over = False
                self.new_highscore = False
                self.start_game = False

        #Draw saucer struck animations based on direction
        #Saucer 1
        if self.saucer_struck == True:
            if self.struck_timer < 10:
                if self.current_direction == 1:
                    self.saucer_sprite.angle = -10
                elif self.current_direction == 2:
                    self.saucer_sprite.angle = 10
            elif self.struck_timer >= 10 and self.struck_timer < 20:
                if self.current_direction == 1:
                    self.saucer_sprite.angle = 10
                elif self.current_direction == 2:
                    self.saucer_sprite.angle = -10
            elif self.struck_timer >= 20:
                self.saucer_sprite.angle = 0
                self.struck_timer = 0
                self.saucer_struck = False

        #Saucer 2
        if self.saucer2_struck == True:
            if self.struck2_timer < 10:
                if self.current_direction2 == 1:
                    self.saucer2_sprite.angle = -10
                elif self.current_direction2 == 2:
                    self.saucer2_sprite.angle = 10
            elif self.struck2_timer >= 10 and self.struck2_timer < 20:
                if self.current_direction2 == 1:
                    self.saucer2_sprite.angle = 10
                elif self.current_direction2 == 2:
                    self.saucer2_sprite.angle = -10
            elif self.struck2_timer >= 20:
                self.saucer2_sprite.angle = 0
                self.struck2_timer = 0
                self.saucer2_struck = False