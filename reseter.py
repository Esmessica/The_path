import os


class Clear:

    def cls(self):
        """reseting console"""
        input()
        return os.system('cls' if os.name == 'nt' else 'clear')