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
        self._slowprint = None
        self._number_of_line = None
        self._forest = None
        self._file = FileImporter()
        self._pic = PictureInGame()
        self._sentence = None

    def __str__(self):
        return "Logic of a game and logic paths"

    def part_start_game(self):
        tutorial = FileImporter()
        tutorial.tutorial_texts()
        _clr
        _pregame = self._file.open_story_lines()
        _pregame_pic = self._pic.start_game()
        _pregame_text = self._pic.start_text()
        _pregame
        print(_pregame_pic)
        print(_pregame_text)

    def play_afterstart_game(self, forest, sentence_index):
        self._forest = forest
        print(self._forest)
        with open("Texts/Story.txt", encoding="utf-8") as file:
            self._sentence = file.readlines()
        self._slowprint = ConsolePrinter(self._sentence[sentence_index])
        self._slowprint.slow_print()


# TO write text for each picture
# TO match text to each picture for story
# TO make function for moving into next location via < >

s = StartLogic()
s.part_start_game()