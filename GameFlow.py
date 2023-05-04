from GameComponentLogic import *
from Forest import *

game = GameComponentLogic()
forest = Forest()

print(game.part_start_game())
print(game.play_forest_sentence(forest.start_car(), 0))