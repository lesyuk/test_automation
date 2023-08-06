import pytest
import random
from homework3 import data


@pytest.fixture(params=data.TEST_SETS)
def new_set(request):
    return set(request.param)


@pytest.fixture()
def initial_set(new_set):
    return set(new_set)


def test_set_access_by_index(new_set):
    if new_set:
        with pytest.raises(TypeError):
            assert new_set[1]


def test_set_remove_value(new_set):
    if new_set:
        random_element = random.choice(tuple(new_set))
        new_set.remove(random_element)
        assert random_element not in new_set


@pytest.mark.parametrize('value', data.TEST_ITERABLE)
def test_set_update(new_set, value):
    new_set.update(value)
    assert set(value).issubset(new_set)


class TestSetAdding:

    @pytest.mark.parametrize('value', data.TEST_HASHABLE_VALUES)
    def test_set_add_hashable_value(self, new_set, initial_set, value):
        new_set.add(value)
        assert new_set != initial_set
        assert value in new_set

    @pytest.mark.parametrize('value', data.TEST_UNHASHABLE_VALUES)
    def test_set_add_unhashable_value(self, new_set, value):
        with pytest.raises(TypeError):
            new_set.add(value)
