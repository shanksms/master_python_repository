from itertools import permutations
from itertools import combinations

def permutations_example():
    items = ['a', 'b', 'c']
    for p in permutations(items):
        print(p)


def combinations_example():
    items = ['a', 'b', 'c']
    for p in combinations(items, 2):
        print(p)


if __name__ == '__main__':
    combinations_example()
