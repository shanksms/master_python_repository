for tup in zip('abc', [1, 2, 3]):
    print(tup)


# lets implement myzip
def myzip(*args):
    length_of_shortest = min([len(arg) for arg in args])
    for i in range(length_of_shortest):
        ret_list = []
        for arg in args:
            ret_list.append(arg[i])
        yield tuple(ret_list)


print('#' * 80)
for tup in myzip('abc', [1, 2, 3]):
    print(tup)