from StoryTexts import *
from PicToText import *
from reseter import Clear
from StoryTexts import FileImporter
from SlowTextPrint import *

clear = Clear()
_clr = clear.cls()


class StartLogic:
    """Logic and timelines of a game"""

    def __init__(self):
        self._number_of_line = None
        self._forest = None
        self._file = FileImporter()
        self._pic = PictureInGame()

    def __str__(self):
        return "Logic of a game and logic paths"

    def part_0_game(self):
        tutorial = FileImporter()
        tutorial.tutorial_texts()
        input()
        _clr
        _pregame = self._file.open_story_lines()
        _pregame_pic = self._pic.start_game()
        _pregame_text = self._pic.start_text()
        _pregame
        print(_pregame_pic)
        print(_pregame_text)

    def story_lines(self, number_of_line):
        """enter the number of line from text file"""
        self._number_of_line = number_of_line
        with open("Texts/Story.txt", encoding="utf-8") as file:
            self._sentence = file.readlines()
            print(self._sentence[number_of_line])

    def part_1_game(self):
        """post-screen timeline"""
        self._forest = Forest().start_car()
        print(self._forest)
        self._slowprint = ConsolePrinter(self._sentence[0])
        self._slowprint.slow_print()

    def part_2_game(self):
        """second part of journey"""



# TO write text for each picture
# TO match text to each picture for story
# TO make function for moving into next location via < >


s = StartLogic()
s.part_0_game()
s = StartLogic()
s.story_lines(0)
s.part_1_game()

