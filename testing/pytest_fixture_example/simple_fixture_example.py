import pytest

@pytest.fixture
def name():
    return 'Rick'


def test_something(name):
    assert name == 'Rick'
