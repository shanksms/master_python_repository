import time

def fancy_repr(self):
    return f'i am a {type(self)} with {vars(self)}'


def object_birthday(c):
    # add a method to the class
    c.__repr__ = fancy_repr
    def wrapper(*args, **kwargs):
        o = c(*args, **kwargs)
        # add an attribute to an instance
        o._created_at = time.time()
        return o

    return wrapper

@object_birthday
class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    a = Foo(1, [1, 2, 3])
    print(a)
    print(a._created_at)


