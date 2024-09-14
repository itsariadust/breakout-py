import arcade
from arcade.color import WHITE

from constants import *
from block import BlockSprite


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.player_list = None
        self.block_list = None
        
        self.block_textures = None
        
        self.game_state = PLAY_GAME
        
        self.player_sprite = None
        self.score = 0
        self.lives = 3
        self.death_pause = 0
        
        self.window.set_mouse_visible(False)

        arcade.set_viewport(0, 640, 0, 480)

        arcade.set_background_color(arcade.color.BLACK)
        
    def level_one(self):
        block_columns = 18
        block_rows = 7
        x_viewport_offset = 40
        y_viewport_offset = 400
        
        for column in range(block_columns):
            x = x_viewport_offset + (column * 40) + 20
            for row in range(block_rows):
                y = y_viewport_offset + ((block_rows - 1 - row) * 16) + 8

                score = 0

                if row == 0:
                    sprite_texture = arcade.load_texture("assets/block_red.png")
                    score = 1
                elif row == 1:
                    sprite_texture = arcade.load_texture("assets/block_orange.png")
                    score = 2
                elif row == 2:
                    sprite_texture = arcade.load_texture("assets/block_yellow.png")
                    score = 3
                elif row == 3:
                    sprite_texture = arcade.load_texture("assets/block_green.png")
                    score = 4
                elif row == 4:
                    sprite_texture = arcade.load_texture("assets/block_blue.png")
                    score = 5
                elif row == 5:
                    sprite_texture = arcade.load_texture("assets/block_indigo.png")
                    score = 6
                else:
                    sprite_texture = arcade.load_texture("assets/block_violet.png")
                    score = 7

                block = BlockSprite(sprite_texture)
                block.scale = 1
                block.score = score

                block.center_x = x
                block.center_y = y

                self.block_list.append(block)

    def setup(self):
        self.game_state = PLAY_GAME

        # Sprite List
        self.player_list = arcade.SpriteList()
        self.block_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("assets/player.png", 1)
        self.player_sprite.center_x = 320
        self.player_sprite.center_y = 40 + (self.player_sprite.height / 2)
        self.player_sprite.color = WHITE
        self.player_list.append(self.player_sprite)

        self.level_one()

    def on_show_view(self):
        self.setup()
        
    def draw(self):
        self.block_list.draw()
        self.player_list.draw()

    def on_draw(self):
        self.window.use()
        self.window.clear()
        self.draw()

    def on_update(self, delta_time):
        """All the logic to move, and the game logic goes here."""
        self.physics_engine.update()
        self.player_list.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass