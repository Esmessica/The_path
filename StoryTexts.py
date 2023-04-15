from SlowTextPrint import ConsolePrinter

"""This file takes texts from .txt file for story telling. It takes one line of txt file at time."""


with open("StoryLines.txt", encoding="utf-8") as file:               # test
    count = 0
    sentence = file.readlines()
    while count <= 2:
        variable = sentence[count]
        count += 1
        printer = ConsolePrinter(variable)
        do = printer.slow_print()
