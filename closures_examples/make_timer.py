"""
make_timer() function returns a new function. Each time you call this new function,
it returns the elapsed time since the last time you called it. Here’s how it looks:
"""
import time
def make_timer():
    last_time_called = None
    def inner():
        nonlocal last_time_called
        if not last_time_called:
            last_time_called = time.time()
            return None
        return time.time() - last_time_called
    return inner
if __name__ == '__main__':
    inner_fn = make_timer()
    print(inner_fn())
    time.sleep(2)
    print(inner_fn())
    time.sleep(2)
    print(inner_fn())
