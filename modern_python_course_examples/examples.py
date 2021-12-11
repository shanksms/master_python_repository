from random import choice, choices, sample, shuffle
from collections import Counter

outcomes = ['win', 'lose', 'draw', 'play again', 'double win']
print(choice(outcomes))
print(choices(outcomes, k=10))
print(Counter(choices(outcomes, k=10)))
# choices are uniformly distributed
print(Counter(choices(outcomes, k=10000)))
# choices duplicates
print(choices(outcomes, k=5))
# if you want to choose without replacement
print(sample(outcomes, k=4))
print(sample(outcomes, k=4))
# sample can be used to choose lottery winners
print(sorted(sample(range(1, 57), k=6)))