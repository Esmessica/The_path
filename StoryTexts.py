from SlowTextPrint import ConsolePrinter

"""This file takes texts from .txt file for story telling. It takes one line of txt file at time."""


class FileImporter:
    def __init__(self):
        self._leng = None

    def __str__(self):
        pass
    def open_story_lines(self):
        with open("Texts/StoryLines.txt", encoding="utf-8") as file:  # test
            count = 0
            sentence = file.readlines()
            self._leng = len(sentence)
            while count <= self._leng - 1:
                variable = sentence[count]
                count += 1
                printer = ConsolePrinter(variable)
                _do = printer.slow_print()
                input()
            return True

    def tutorial_texts(self):
        with open("Texts/Tutorial.txt", encoding="utf-8") as file:
            sentence = file.readlines()
            for i in sentence:
                printer = ConsolePrinter(i)
                _do = printer.slow_print()
            input()
        return True


# f = FileImporter()
# f.tutorial_texts()



