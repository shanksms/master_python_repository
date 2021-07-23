def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')


# Create the generator, notice no output appears
c = countdown(3)
c


# Run to first yield and emit a value
print(next(c))


# Run to the next yield
print(next(c))


# Run to next yield
print(next(c))


# Run to next yield (iteration stops)
print(next(c))