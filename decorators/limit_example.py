import time

def once_per_n(n):
    def middle(func):
        last_invoked = 0

        def wrapper(*args, **kwargs):
            nonlocal last_invoked
            if time.time() - last_invoked < n:
                raise Exception('called too often')
            last_invoked = time.time()
            return func(*args, **kwargs)

        return wrapper
    return middle

@once_per_n(4)
def slow_add(a, b):
    time.sleep(2)
    return a + b

if __name__ == '__main__':
    print(slow_add(1, 2))
    print(slow_add(3, 4))

