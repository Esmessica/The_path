import time


class ConsolePrinter:

    """Text slow printing"""

    def __init__(self, text):
        self._text = text

    def __str__(self):
        return f"Printing : {self._text}"

    def slow_print(self):
        print("\t \t", end="")
        for character in self._text:
            print(character, end="", flush=True)
            time.sleep(0.03)


c = ConsolePrinter(input("input"))
c.slow_print()




