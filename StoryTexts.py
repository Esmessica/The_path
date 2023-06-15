from SlowTextPrint import ConsolePrinter
from reseter import *

"""This file takes texts from .txt file for story telling. It takes one line of txt file at time."""


class StoryTexts:
    def __init__(self):
        self._leng = None

    def __str__(self):
        return "Texts before game starts"

    def open_story_lines(self):
        with open("Texts/StoryLines.txt", encoding="utf-8") as file:  # test
            print("\n\n\n\n\n\n")
            count = 0
            sentence = file.readlines()
            self._leng = len(sentence)
            while count <= self._leng - 1:
                variable = sentence[count]
                count += 1
                printer = ConsolePrinter(variable)
                _do = printer.slow_print()
                input()

    def tutorial_texts(self):
        try:
            with open("Texts/Tutorial.txt", encoding="utf-8") as file:
                sentence = file.readlines()
                for i in sentence:
                    printer = ConsolePrinter(i)
                    _do = printer.slow_print()
                print("\n")
                input()
        except FileNotFoundError:
            print("Error in text file")