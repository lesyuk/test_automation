import pytest
import itertools
from homework3 import data


@pytest.fixture(params=data.TEST_LISTS)
def new_list(request):
    return list(request.param)


@pytest.fixture()
def initial_list(new_list):
    return list(new_list)


def test_list_append(new_list, initial_list):
    element_to_add = '1'
    new_list.append(element_to_add)
    assert len(new_list) == len(initial_list) + 1
    assert new_list[-1] == element_to_add


@pytest.mark.parametrize('value', data.TEST_ITERABLE)
def test_list_extend(new_list, initial_list, value):
    value_len = len(value)
    new_list.extend(value)
    assert len(new_list) == len(initial_list) + value_len
    for i in range(value_len):
        assert new_list[i - value_len] == list(value)[i]


def test_list_pop(new_list):
    new_list_slice = new_list[:len(new_list) - 1]
    if not new_list:
        with pytest.raises(IndexError):
            new_list.pop()
    else:
        last_element = new_list[-1]
        popped_element = new_list.pop(-1)
        assert last_element == popped_element
        assert new_list_slice == new_list


class TestListSorting:
    def test_list_sort(self, new_list):
        new_list.sort()
        for t in list(itertools.pairwise(new_list)):
            assert t[0] <= t[1]

    def test_list_sorted(self, new_list, initial_list):
        sorted_list = sorted(new_list)
        for t in list(itertools.pairwise(sorted_list)):
            assert t[0] <= t[1]
        assert new_list == initial_list



