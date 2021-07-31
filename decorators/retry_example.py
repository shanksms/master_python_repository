import random
from retrying import retry


@retry
def pick_one():
    if random.randint(0, 10) != 1:
        print('1 was not picked')
        raise Exception('1 was not picked')
    print('1 was picked')


@retry(wait_exponential_multiplier=10, wait_exponential_max=1000, stop_max_delay=3000)
def wait_exponential_1000_stop():
    print("Wait 2^x * 10 milliseconds between each retry, up to 1 seconds, ")
    raise Exception('retry')


@retry(wait_exponential_multiplier=10, wait_exponential_max=10000)
def wait_exponential_1000():
    print ("Wait 2^x * 10 milliseconds between each retry, up to 10 seconds, then 10 seconds afterwards")
    raise Exception("Retry!")




if __name__ == '__main__':
    pick_one()
    #wait_exponential_1000()
    wait_exponential_1000_stop()