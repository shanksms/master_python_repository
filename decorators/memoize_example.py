import pickle


def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        t = (pickle.dumps(args), pickle.dumps(kwargs))
        if t in cache:
            print('exists in cache')
            return cache[t]
        else:
            ret = func(*args, **kwargs)
            cache[t] = ret
            return ret
    return wrapper
@memoize
def add(a, b):
    return a + b

@memoize
def mul(a, b):
    return a * b

if __name__ == '__main__':
    print(add(3, 2))
    print(mul(3, 2))
    print(add(3, 2))
    print(mul(3, 2))

