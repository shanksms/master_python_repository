import time


def logtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        print(f'time taken is {time.time() - start_time}')
        return ret
    return wrapper

@logtime
def slow_add(a, b):
    time.sleep(2)
    return a + b

if __name__ == '__main__':
    print(slow_add(2, 5))