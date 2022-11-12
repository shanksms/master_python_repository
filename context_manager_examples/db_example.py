"""
1. Create a table Point which has two columns x and y
2. Insert three rows
3. Delete the table
4. Creation and deletion should happen as part of context manager
"""

from sqlite3 import connect
from contextlib import contextmanager


@contextmanager
def temp_table(cursor):
    cursor.execute('create table Point (x int, y int)')
    yield
    cursor.execute('drop table Point')


with connect('test.db') as conn:
    cursor = conn.cursor()
    with temp_table(cursor):
        cursor.execute('insert into Point values (1, 1)')
        cursor.execute('insert into Point values (2, 2)')
        cursor.execute('insert into Point values (3, 3)')
        for x, y in cursor.execute('select x, y from Point'):
            print(x, y)




