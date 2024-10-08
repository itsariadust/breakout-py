import arcade

from constants import *
from game_view import GameView

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, RESIZEABLE)
    start_view = GameView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()