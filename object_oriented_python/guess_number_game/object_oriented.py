
class GuessGame:
    def __init__(self, number, min=0, max=100):
        self.number = number
        self.min = min
        self.max = max
        self.guess_number = 1

    def get_user_guess(self):
        try:
            num = int(input('Enter a number between 1-100'))
        except:
            print('invalid number. please guess again')
        return num
    def play(self):
        while True:
            num = self.get_user_guess()
            if num > self.number:
                print('your number is over')
            elif num < self.number:
                print('your number is under')
            else:
                break
            self.guess_number += 1
        print(f'you guessed in {self.guess_number} attempts')


if __name__ == '__main__':
    game = GuessGame(45)
    game.play()