from StoryTexts import *
from PicToText import *
from reseter import Clear
from StoryTexts import FileImporter

clear = Clear()
_clr = clear.cls()


class StartLogic:

    """Logic and timelines of a game"""

    def __init__(self):
        self._file = FileImporter()
        self._pic = PictureInGame()

    def __str__(self):
        return "Logic of a game and logic paths"

    def part1_game(self):
        tutorial = FileImporter()
        tutorial.tutorial_texts()
        _clr
        _pregame = self._file.open_story_lines()
        _pregame_pic = self._pic.start_game()
        _pregame_text = self._pic.start_text()
        _pregame
        print(_pregame_pic)
        print(_pregame_text)


s = StartLogic()
s.part1_game()
input()