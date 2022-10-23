
def frange(start, end, step):
    while start < end:
        yield start
        start += step


for i in frange(1, 10, 0.5):
    print(i)


