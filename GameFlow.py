from GameComponentLogic import *
from Forest import *
from StoryTexts import *
import keyboard
from Cabin import Cabins


class Game:

    """This file manages the game flow"""

    def __init__(self):
        pass

    def __str__(self):
        return "Mistic forest game"

    def ingame(self):
        _game = GameComponentLogic()
        forest = Forest()
        cabin = Cabins()
        keyboard.press('f11')

        # _before_game = StoryTexts()
        # _before_game.tutorial_texts()
        # _before_game.open_story_lines()
        _game.part_start_game()
        _game.play_forest_sentence(forest.start_car(), 0)
        input()
        Clear().cls()
        _game.play_forest_sentence(forest.forest6(), 1)
        input()
        Clear().cls()
        _game.play_forest_sentence(forest.split_path2(), 2)
        if _game.direction() == 1:
            Clear().cls()
            _game.play_forest_sentence(forest.forest5(), 3)
            input()
            Clear().cls()
            _game.play_forest_sentence(forest.stairs_forest1(), 5)
            input()
            Clear().cls()
            _game.play_forest_sentence(forest.lonely_tree(), 6)
            if _game.direction() == 1:
                Clear().cls()
                _game.play_forest_sentence(forest.forest_rocks(), 7)
                input()
                Clear().cls()
                _game.play_forest_sentence(forest.forest3(), 8)
                input()
                Clear().cls()
                _game.play_forest_sentence(forest.muddy_path(), 9)
                input()
                Clear().cls()
                _game.play_forest_sentence(forest.lonely_tree(), 10)
                input()
                Clear().cls()
                _game.play_forest_sentence(forest.fontain(), 11)
                input()
                Clear().cls()
                _game.play_forest_sentence(forest.forest_rocks(), 12)
                input()
                Clear().cls()
                _game.play_forest_sentence(cabin.cabin2(), 13)
                input()
                Clear().cls()
                _game.play_forest_sentence(cabin.cabin_door(), 14)
                input()
                Clear().cls()
                _game.play_forest_sentence(cabin.keys_on_table(), 15)
                input()
                Clear().cls()
                _game.play_forest_sentence(forest.login_screen(), 16)
                # Happy end
            else:

                _game.play_forest_sentence(forest.fontain(), 11)
                input()
                Clear().cls()
                _game.play_forest_sentence(forest.forest_rocks(), 12)
                input()
                Clear().cls()
                _game.play_forest_sentence(cabin.cabin2(), 13)
                input()
                Clear().cls()
                _game.play_forest_sentence(cabin.cabin_door(), 14)
                input()
                Clear().cls()
                _game.play_forest_sentence(cabin.keys_on_table(), 15)
                input()
                Clear().cls()
                _game.play_forest_sentence(forest.login_screen(), 16)
                # Happy end

        else:
            _game.play_forest_sentence(forest.forest7(), 4)
            input()
            Clear().cls()
            _game.play_forest_sentence(forest.forest4(), 17)
            input()
            Clear().cls()
            _game.play_forest_sentence(forest.stairs_forest1(), 18)
            input()
            Clear().cls()
            _game.play_forest_sentence(forest.fontain(), 19)

            if _game.direction() == 1:
                Clear().cls()
                _game.play_forest_sentence(forest.forest5(), 23)
                input()
                Clear().cls()
                _game.play_forest_sentence(forest.forest_rocks(), 24)
                input()
                Clear().cls()
                _game.play_forest_sentence(forest.forest7(), 25)

                if _game.direction() == 1:
                    Clear().cls()
                    _game.play_forest_sentence(forest.muddy_path(), 26)
                    input()
                    Clear().cls()
                    _game.play_forest_sentence(cabin.cabin2(), 13)
                    input()
                    Clear().cls()
                    _game.play_forest_sentence(cabin.cabin_door(), 14)
                    input()
                    Clear().cls()
                    _game.play_forest_sentence(cabin.keys_on_table(), 15)
                    input()
                    Clear().cls()
                    _game.play_forest_sentence(forest.login_screen(), 16)
                    # Happy end
                else:
                    _game.play_forest_sentence(cabin.cabin2(), 13)
                    input()
                    Clear().cls()
                    _game.play_forest_sentence(cabin.cabin_door(), 14)
                    input()
                    Clear().cls()
                    _game.play_forest_sentence(cabin.keys_on_table(), 15)
                    input()
                    Clear().cls()
                    _game.play_forest_sentence(forest.login_screen(), 16)
                    # Happy end

            else:
                _game.play_forest_sentence(cabin.cabin1(), 20)
                input()
                Clear().cls()
                _game.play_forest_sentence(cabin.cabin_door(), 21)
                input()
                Clear().cls()
                _game.play_forest_sentence(cabin.cabin_door(), 22)
                input()
                Clear().cls()

        print("konec testu")
        input()


g = Game()
g.ingame()