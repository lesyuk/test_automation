import random
import pytest


@pytest.fixture()
def random_value():
    print('Entering! Before test')
    res = random.randint(0, 100)
    yield res
    print('Exiting! After test')


def test1(random_value):
    print('Inside test 1')
    assert random_value > 50


def test2(random_value):
    print('Inside test 2')
    assert random_value > 50
