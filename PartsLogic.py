from PicToText import *
from reseter import Clear
from StoryTexts import FileImporter
from SlowTextPrint import *
from wolves import *


class GameComponentLogic:
    """Logic of a game components, start, end + decision method for controling game flow"""

    def __init__(self):
        self._question = None
        self._slowprint = None
        self._number_of_line = None
        self._forest = None
        self._file = FileImporter()
        self._pic = PictureInGame()
        self._sentence = None

    def __str__(self):
        return "Logic of a game and logic paths"

    def part_start_game(self):
        """Method for starting game screen"""
        tutorial = FileImporter()
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
        input()

    def press_direction(self):
        """direction decider left = True, right = False"""
        _questioning_cycle = 1
        while _questioning_cycle:
            self._question = input("\t\tWhich way should I go?\t < \t >\n\t\t")

            if self._question == "<":
                _questioning_cycle = 0
                return True
            elif self._question == ">":
                _questioning_cycle = 0
                return False
            else:
                _e = "I need left or right arrow to continue!"
                try:
                    raise ValueError(_e)
                except ValueError as exp:
                    print("Error", exp)

    def play_afterstart_game(self, forest, sentence_index):
        """Method for choosing line of text code and picture from py file"""
        self._forest = forest
        print(self._forest)
        with open("Texts/Story.txt", encoding="utf-8") as file:
            self._sentence = file.readlines()
        self._slowprint = ConsolePrinter(self._sentence[sentence_index])
        self._slowprint.slow_print()


# TO write text for each picture CHECK
# TO match text to each picture for story
# TO make function for moving into next location via < >


# # testing
# s = StartLogic()
# # s.part_start_game()
# # s.play_afterstart_game(Forest().start_car(), 0)
# # input()
# # s.play_afterstart_game(Forest().forest6(), 1)
# s.play_afterstart_game(Forest().forest6(), 2)
# s.press_direction()