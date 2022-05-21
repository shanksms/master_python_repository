
def chunk(_list, batch_size):
    for i in range(0, len(_list), batch_size):
        yield _list[i:i+batch_size]

for i in chunk(list(range(10)), 3):
    print(i)

