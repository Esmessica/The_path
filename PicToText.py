from Forest import *
from Cabin import *
from TextAscii import *


class PictureInGame:

    """This class puts pictures together with sentences"""

    def __init__(self):
        self._start_text = None
        self._forest = None

    def __str__(self):
        return "Pictures with sentences from txt file"

    def start_game(self):
        """Start game picture"""
        _forest = Forest()
        self._forest = _forest.login_screen()
        return self._forest

    def start_text(self):
        """Ascii art start game"""
        _text1 = AsciiText()
        self._start_text = _text1.start_info()
        return self._start_text


# TODO make ending screen + game over

# testing
# g = Game()
# print(g.start_game())
# print(g.start_text())
# input()


