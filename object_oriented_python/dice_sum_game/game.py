from object_oriented_python.dice_sum_game.player import Player


class Game:
    counter = 0

    def __init__(self, num_players, target_score = 100):
        self.players = [Player(i + 1) for i in range(num_players)]
        Game.counter += 1
        self.game_num = Game.counter
        self.target_score = target_score

    def run_game(self):
        print(f"{self} started")
        while True:
            for player in self.players:
                player.take_turn()
            if self.game_over():
                winners = self.get_winners()
                if len(winners) == 1:
                    print(f'{winners[0]} wins')
                else:
                    print(f'{winners} win')
                print(f"{self} ended")

                return


    def game_over(self):
        for player in self.players:
            if player.score >= self.target_score:
                return True
        return False


    def get_winners(self):
        return [str(player) for player in self.players if player.score >= self.target_score]

    def __str__(self):
        return f'Game {self.game_num}'