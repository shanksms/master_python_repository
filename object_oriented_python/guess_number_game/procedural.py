guess = 1

while True:
    try:
        num = int(input('Enter a number between 1-100'))
    except:
        print('invalid number. please guess again')

    if num > 45:
        print('your number is over')
    elif num < 45:
        print('your number is under')
    else:
        break

    guess += 1

print(f'you guess in {guess} attempts')
