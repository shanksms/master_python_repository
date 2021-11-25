"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from object_oriented_python.dice_sum_game.game import Game

if __name__ == '__main__':
    game1 = Game(4)
    game1.run_game()
    #game2 = Game(4, target_score=50)
    #game2.run_game()