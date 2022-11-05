import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # noqa:

from game.game import Game

if __name__ == '__main__':
    Game()
