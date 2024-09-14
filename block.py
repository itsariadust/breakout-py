import arcade

from constants import *

class BlockSprite(arcade.Sprite):
    def __init__(self, texture):
        super().__init__()
        self.texture = texture
        self.score = 0
        self.broken = False
        
    def on_update(self):
        if self.broken:
            self.remove_from_sprite_lists
            return