from PicToText import *
from reseter import Clear
from StoryTexts import StoryTexts
from SlowTextPrint import *
from wolves import *
import random


class GameComponentLogic:
    """Logic of a game components, start, end + decision method for controling game flow"""

    def __init__(self):
        self._question = None
        self._slowprint = None
        self._number_of_line = None
        self._forest = None
        self._file = StoryTexts()
        self._pic = PictureInGame()
        self._sentence = None

    def __str__(self):
        return "Logic of a game and logic paths"

    def part_start_game(self):
        """Method for starting game screen"""
        tutorial = StoryTexts()
        tutorial.tutorial_texts()
        Clear().cls()
        _pregame = self._file.open_story_lines()
        _pregame_pic = self._pic.start_game()
        _pregame_text = self._pic.start_text()
        Clear().cls()
        print(_pregame_pic)
        print(_pregame_text)
        input()
        Clear().cls()

    def game_over(self):
        """Method for game over screen  -  without text"""
        Clear().cls()
        _wolf = Wolves()
        print(_wolf.angry_wolf())
        _game_over = self._pic.game_over()
        print(_game_over)

    def direction(self):
        """direction decider left = True, right = False"""
        _questioning_cycle = 1
        while _questioning_cycle:
            self._question = input("\n\n\t\tWhich way should I go?\t < \t >\n\t\t")

            if self._question == "<":
                _questioning_cycle = 0
                return 1
            elif self._question == ">":
                _questioning_cycle = 0
                return 0
            else:
                _e = "I need left or right arrow to continue!"
                try:
                    raise ValueError(_e)
                except ValueError as exp:
                    print("Error", exp)

    def play_forest_sentence(self, forest, file_option: int,  sentence_index):
        """Method for choosing line of text code and picture from py file"""
        if file_option == 1:
            """Path for Story lines without wolves"""
            self._forest = forest
            print(self._forest)
            with open("Texts/Story.txt", encoding="utf-8") as file:
                self._sentence = file.readlines()
            self._slowprint = ConsolePrinter(self._sentence[sentence_index])
            self._slowprint.slow_print()

        elif file_option == 2:
            """Path for Story lines with wolves"""
            self._forest = forest
            print(self._forest)
            with open("Texts/Wolves.txt", encoding="utf-8") as file:
                self._sentence = file.readlines()
            self._slowprint = ConsolePrinter(self._sentence[sentence_index])
            self._slowprint.slow_print()

    def wolf_chance(self, rand_ground_chance_number):
        self._chance = random.randint(1, rand_ground_chance_number)
        return self._chance


# wolves = Wolves()
# g = GameComponentLogic()
# test_w = g.wolf_chance(2)
# print(test_w)
# if test_w == 1:
#     g.play_forest_sentence(wolves.paws(), 2, 0)
#
# else:
#     print("Je to dva")

# TO write text for each picture CHECK
# TO match text to each picture for story
# TO make function for moving into next location via < >