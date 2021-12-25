from itertools import chain

'''
This is how itertools.chain work.
it takes multiple iterators and iterate them as if they are part of same iterator
'''
from itertools import chain

for one_item in chain('abc', [1, 2, 3], {'a': 1, 'b': 2}):
    print(one_item)

# lets implement our own version of chain

def mychain(*args):
    for arg in args:
        for element in arg:
            yield element

print('#' * 80)
for e in mychain('abc', [1, 2, 3], {'a': 1, 'b': 2}):
    print(e)

# lets implement a simple iterator class