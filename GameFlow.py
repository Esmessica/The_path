from GameComponentLogic import *
from Forest import *
from reseter import *


game = GameComponentLogic()
forest = Forest()


# print(game.part_start_game())
game.play_forest_sentence(forest.start_car(), 0)
input()
Clear().cls()
game.play_forest_sentence(forest.forest6(), 1)
input()
Clear().cls()
game.play_forest_sentence(forest.split_path2(), 2)
if game.direction() == 1:
    game.play_forest_sentence(forest.forest5(), 3)
    input()
    Clear().cls()

else:
    game.play_forest_sentence(forest.forest7(), 4)
    input()
    Clear().cls()

print("konec testu")
input()