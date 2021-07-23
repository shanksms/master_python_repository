items = [1, 2, 3]
# Get the iterator
it = iter(items)     # Invokes items.__iter__()
# Run the iterator
next(it)             # Invokes it.__next__()
next(it)
next(it)
next(it)  # Generates an error