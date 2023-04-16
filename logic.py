from Forest import *
from Cabin import *
from TextAscii import *


class Game:

    """This class puts pictures together with sentences"""

    def __init__(self):
        self._forest = Forest.login_screen()

    def __str__(self):
        return "Pictures with sentences from txt file"

    def start_game(self):
        print(self._forest)



