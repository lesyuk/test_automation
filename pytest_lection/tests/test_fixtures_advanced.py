import os
import random
import pytest


@pytest.fixture(scope='module')
def random_func():
    return random.randint(0, 100)


@pytest.fixture(autouse=True, scope='function')
def new_file(random_func):
    with open(f'test_file_{random_func}', 'w') as f:
        f.write('123123123123213213135142131203534536535413')
        f.flush()
        yield f
    os.remove(f.name)


def test():
    pass


def test1():
    pass


def test2():
    pass
