from GameComponentLogic import *
from Forest import *
from StoryTexts import  *


class Game():

    """This file manages the game flow"""

    def __init__(self):
        pass

    def __str__(self):
        return "Mistic forest game"

    def ingame(self):
        _game = GameComponentLogic()
        forest = Forest()
        _before_game = StoryTexts()
        _before_game.tutorial_texts()
        _before_game.open_story_lines()
        # print(game.part_start_game())
        _game.play_forest_sentence(forest.start_car(), 0)
        input()
        Clear().cls()
        _game.play_forest_sentence(forest.forest6(), 1)
        input()
        Clear().cls()
        _game.play_forest_sentence(forest.split_path2(), 2)
        if _game.direction() == 1:
            _game.play_forest_sentence(forest.forest5(), 3)
            input()
            Clear().cls()

        else:
            _game.play_forest_sentence(forest.forest7(), 4)
            input()
            Clear().cls()

        print("konec testu")
        input()


g = Game()
g.ingame()