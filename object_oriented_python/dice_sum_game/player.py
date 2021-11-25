import random

class Player:
    def __init__(self, player_num):
        self._score = 0
        self.player_num = player_num

    def take_turn(self):
        player_roll = random.randint(1, 6)
        self._score += player_roll
        print(f'{self} score is {self._score}. rolled dice {player_roll}')

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f'Player {self.player_num}'

    def __repr__(self):
        return f'Player({self.player_num})'
