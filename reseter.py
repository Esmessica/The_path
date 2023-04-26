import os


class Clear:

    def cls(self):
        """reseting console"""
        return os.system('cls' if os.name == 'nt' else 'clear')