from Forest import *


class PictureInGame:

    """This class puts pictures together with sentences"""

    def __init__(self):
        self._start_text = None
        self._forest = None
        self._game_over = """ 
                              ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
                             ██▒ ▀█ ▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
                            ▒██░▄▄▄ ░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
                            ░▓█  ██▓ ░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
                            ░▒▓███▀▒  ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
                             ░▒   ▒   ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
                              ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
                              ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
                                  ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                                                 ░                   
                              """

        self._start_info = """
                              _____                                         _                _              _             _   
                             |  __  |                                       | |              | |            | |           | |  
                             | |__) | __ ___  ___ ___    __ _ _ __  _   _  | | _____ _   _  | |_ ___    ___| |_ __ _ _ __| |_ 
                             |  ___| '__/ _ \/ __/ __|  / _` | '_ \| | | | | |/ / _ \ | | | | __/ _ \  / __| __/ _` | '__| __|
                             | |   | | |  __/\__ \__ \ | (_| | | | | |_| | |   <  __/ |_| | | || (_) | \__ \ || (_| | |  | |_ 
                             |_|   |_|  \___||___/___/  \__,_|_| |_|\__, | |_|\_\___|\__, |  \__\___/  |___/\__\__,_|_|   \__|
                                                                     __/ |            __/ |                                   
                                                                    |___/            |___/                               
                             """

    def __str__(self):
        return "Pictures with sentences from txt file"

    def start_game(self):
        """Start game picture"""
        _forest = Forest()
        self._forest = _forest.login_screen()
        return self._forest

    def start_text(self):
        """Ascii art start game"""
        return self._start_info

    def game_over(self):
        return self._game_over

