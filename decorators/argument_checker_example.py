import functools


# check parameter is decorator factory
def check_parameter(index):
    # this is actual decorator
    def validator(fn):
        @functools.wraps(fn)
        def inner(*args):
            if args[1] < 0:
                raise ValueError('Can not be non negative')
            return fn(*args)
        return inner
    return validator


@check_parameter(1)
def create_list(value, size):
    return [value] * size


if __name__ == '__main__':
    print(create_list('a', 2))
    # below will fail
    #create_list('a', -1)
