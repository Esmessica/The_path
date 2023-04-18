from StoryTexts import *
from PicToText import *
from reseter import Clear

clear = Clear()
_clr = clear.cls()


class GameLogic:

    """Logic and timelines of a game"""


    def __init__(self):
        pass

    def __str__(self):
        return "Logic of a game and logic paths"

    def part1(self):
        _file = FileImporter()
        _pregame = _file.open_story_lines()
        return _pregame


g = GameLogic()
g.part1()
_clr