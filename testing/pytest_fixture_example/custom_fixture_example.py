import pytest
import sqlite3


@pytest.fixture(params=[':memory:'])
def connection(request):
    '''
    First we have the connection() fixture, which uses the special parameter params. Instead of using the :memory:
    database in sqlite3, we can use a different database name or multiple names as well.
    That is why params is a list; the test will be executed for each value in params.
    '''
    return sqlite3.connect(request.param)


@pytest.fixture
def transaction(connection):
    '''
    The transaction() fixture uses the connection() to open the database connection, yield it to the user of that fixture,
    and take care of the cleanup after. This could easily have been omitted and done in transation() immediately, but it saves an indentation
    level and it allows you to further customize the connection at a single location if needed.
    '''
    with connection:
        yield connection


def test_insert(transaction):
    transaction.execute('create table test (id integer)')
    transaction.execute('insert into test values (1), (2), (3)')
