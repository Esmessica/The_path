from SlowTextPrint import ConsolePrinter

"""This file takes texts from .txt file for story telling. It takes one line of txt file at time."""


class FileImporter:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def open_story_lines(self):
        with open("StoryLines.txt", encoding="utf-8") as file:  # test
            count = 0
            sentence = file.readlines()
            leng = len(sentence)
            while count <= leng - 1:
                variable = sentence[count]
                count += 1
                printer = ConsolePrinter(variable)
                _do = printer.slow_print()
                input()

            return True


