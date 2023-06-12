from GameComponentLogic import *
from Forest import *
from wolves import *
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
        wolves = Wolves()
        keyboard.press('f11')
        wolf_chance = _game.wolf_chance(4)      # Holds random number for wolves

        print("\n \n \n \n \n \n")
        _game.part_start_game()
        print("\n \n \n \n \n \n")
        _game.play_forest_sentence(forest.start_car(), 1, 0)
        input()
        Clear().cls()
        print("\n \n \n \n \n \n")
        _game.play_forest_sentence(forest.forest6(), 1, 1)
        input()
        Clear().cls()
        print("\n \n \n \n \n \n")
        _game.play_forest_sentence(forest.split_path2(), 1, 2)

        if _game.direction() == 1:
            Clear().cls()
            print("\n \n \n \n \n \n")
            _game.play_forest_sentence(forest.forest5(), 1, 3)
            input()
            Clear().cls()

            if wolf_chance == 2:
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(wolves.paws(), 2, 0)
                input()
                Clear().cls()

            print("\n \n \n \n \n \n")
            _game.play_forest_sentence(forest.stairs_forest1(), 1, 5)
            input()
            Clear().cls()

            if wolf_chance == 2:
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(wolves.wolves_pack(), 2, 1)
                input()
                Clear().cls()

            print("\n \n \n \n \n \n")
            _game.play_forest_sentence(forest.lonely_tree(), 1, 6)

            if _game.direction() == 1:
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.forest_rocks(), 1, 7)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.forest3(), 1, 8)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.muddy_path(), 1, 9)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.lonely_tree(), 1, 10)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.fontain(), 1, 11)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")

                if wolf_chance == 2:
                    """Ends game if wolves were met earlier"""
                    _game.play_forest_sentence(wolves.angry_wolf(), 2, 2)
                    input()
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.game_over()
                    input()
                    exit()

                _game.play_forest_sentence(forest.forest_rocks(), 1, 12)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.cabin2(), 1, 13)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.cabin_door(), 1, 14)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.keys_on_table(), 1, 15)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.login_screen(), 1, 16)
                # Happy end

            else:
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.fontain(), 1, 11)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.forest_rocks(), 1, 12)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.cabin2(), 1, 13)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.cabin_door(), 1, 14)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.keys_on_table(), 1, 15)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.login_screen(), 1, 16)
                # Happy end

        else:
            Clear().cls()
            print("\n \n \n \n \n \n")
            _game.play_forest_sentence(forest.forest7(), 1, 4)
            input()
            Clear().cls()

            if wolf_chance == 2:
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(wolves.paws(), 2, 0)
                input()
                Clear().cls()

            print("\n \n \n \n \n \n")
            _game.play_forest_sentence(forest.forest4(), 1, 17)
            input()
            Clear().cls()
            print("\n \n \n \n \n \n")
            _game.play_forest_sentence(forest.stairs_forest1(), 1, 18)
            input()
            Clear().cls()
            print("\n \n \n \n \n \n")
            _game.play_forest_sentence(forest.fontain(), 1, 19)
            print("\n \n \n \n \n \n")

            if _game.direction() == 1:
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.forest5(), 1, 23)
                input()
                Clear().cls()

                if wolf_chance == 2:
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(wolves.wolves_pack(), 2, 1)
                    input()
                    Clear().cls()

                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.forest_rocks(), 1, 24)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.forest7(), 1, 25)
                print("\n \n \n \n \n \n")

                if _game.direction() == 1:
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(forest.muddy_path(), 1, 26)
                    input()
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(cabin.cabin2(), 1, 13)
                    input()
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(cabin.cabin_door(), 1, 14)
                    input()
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(cabin.keys_on_table(), 1, 15)
                    input()
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(forest.login_screen(), 1, 16)
                    # Happy end
                else:
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(cabin.cabin2(), 1, 13)
                    input()
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(cabin.cabin_door(), 1, 14)
                    input()
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(cabin.keys_on_table(), 1, 15)
                    input()
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(forest.login_screen(), 1, 16)
                    # Happy end

            else:
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.cabin1(), 1, 20)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.cabin_door(), 1, 21)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.cabin_door(), 1, 22)
                # Check ending on this part
                input()
                Clear().cls()
                # added block of code
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.muddy_path(), 1, 24)
                input()
                Clear().cls()

                if wolf_chance == 2:

                    # wolves

                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(wolves.wolves_pack(), 2, 1)
                    input()
                    Clear().cls()

                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.forest_rocks(), 1, 12)
                input()
                Clear().cls()

                if _game.direction() == 1:
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(forest.forest_rocks(), 1, 26)

                elif _game.direction() == 1 and wolf_chance == 2:

                    """Ends game if wolves were met earlier"""

                    print("\n \n \n \n \n \n")
                    _game.play_forest_sentence(wolves.angry_wolf(), 2, 2)
                    input()
                    Clear().cls()
                    print("\n \n \n \n \n \n")
                    _game.game_over()
                    input()
                    exit()

                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.cabin2(), 1, 13)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.cabin_door(), 1, 14)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(cabin.keys_on_table(), 1, 15)
                input()
                Clear().cls()
                print("\n \n \n \n \n \n")
                _game.play_forest_sentence(forest.login_screen(), 1, 16)
                # Happy end

        print("*")
        input()


