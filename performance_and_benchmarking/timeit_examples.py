from timeit import timeit
setup = 'from datetime import datetime'
statement = 'datetime.now()'
result = timeit(setup=setup, stmt=statement)
print(f'Took an average of {result}ms')