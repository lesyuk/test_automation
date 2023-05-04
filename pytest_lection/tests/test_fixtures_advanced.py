import os
import random
import pytest


@pytest.fixture()
def random_func():
    return random.randint(0, 100)


# If we want to use some value in a fixture from another fixture, we need to pass the fixture to the fixture
@pytest.fixture(autouse=True)
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


# If we want to use a value from autouse fixture, we need to explicitly pass fixture to a test
def test2(new_file):
    print(new_file.write('000000'))
    pass
