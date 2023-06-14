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
                                      _____                     ______       _              _                          _   _                  
                                     |  __ \                   |  ____|     | |            | |                        | | (_)                 
                                     | |__) | __ ___  ___ ___  | |__   _ __ | |_ ___ _ __  | |_ ___     ___ ___  _ __ | |_ _ _ __  _   _  ___ 
                                     |  ___/ '__/ _ \/ __/ __| |  __| | '_ \| __/ _ \ '__| | __/ _ \   / __/ _ \| '_ \| __| | '_ \| | | |/ _ \
                                     | |   | | |  __/\__ \__ \ | |____| | | | ||  __/ |    | || (_) | | (_| (_) | | | | |_| | | | | |_| |  __/
                                     |_|   |_|  \___||___/___/ |______|_| |_|\__\___|_|     \__\___/   \___\___/|_| |_|\__|_|_| |_|\__,_|\___|                                                                                                                             
                             """

    def __str__(self):
        return "Pictures with sentences from txt file"

    def start_game(self):
        """Start game picture"""
        print("\n \n \n \n \n \n")
        _forest = Forest()
        self._forest = _forest.login_screen()
        return self._forest

    def start_text(self):
        """Ascii art start game"""
        return self._start_info

    def game_over(self):
        return self._game_over

