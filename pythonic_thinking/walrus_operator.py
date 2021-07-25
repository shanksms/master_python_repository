fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}


def make_lemonade(count):
    pass


def out_of_stock():
    pass


def slice_bananas(count):
    pass


class OutOfBananas(Exception):
    pass


def make_smoothies(count):
        pass


def make_cider():
    pass

# count = fresh_fruit.get('lemon', 0)
# if count:
#     make_lemonade(count)
# else:
#     out_of_stock()


def example1():
    """
    Though this is only one line shorter,
    it’s a lot more readable because it’s now clear that count is only relevant to the
    first block of the if statement. The assignment expression is first assigning a value to the count variable
    , and then evaluating that value in the context of the if statement to determine how to proceed with
     flow control. This twostep behavior—assign and then evaluate—is the fundamental nature of the walrus operator.
    """

    if count := fresh_fruit.get('lemon', 0):
        make_lemonade(count)
    else:
        out_of_stock()

def example2():

    pieces = 0
    count = fresh_fruit.get('banana', 0)
    if count >= 2:
        pieces = slice_bananas(count)

    try:
        smoothies = make_smoothies(pieces)
    except OutOfBananas:
        out_of_stock()


def example3():
    if (count := fresh_fruit.get('banana', 0)) >= 2:
        pieces = slice_bananas(count)
        to_enjoy = make_smoothies(pieces)
    elif (count := fresh_fruit.get('apple', 0)) >= 4:
        to_enjoy = make_cider(count)
    elif count := fresh_fruit.get('lemon', 0):
        to_enjoy = make_lemonade(count)
    else:
        to_enjoy = 'Nothing'