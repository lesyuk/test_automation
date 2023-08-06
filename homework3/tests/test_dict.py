import pytest
import random
from homework3 import data


@pytest.fixture(params=data.TEST_DICTS)
def new_dict(request):
    return dict(request.param)


@pytest.fixture()
def initial_dict(new_dict):
    return dict(new_dict)


# def test_dict_clear(new_dict):
#     new_dict.clear()
#     print(new_dict)
#     assert not new_dict
#
#
# def test_dict_copy(new_dict, initial_dict):
#     copied_dict = new_dict.copy()
#     assert copied_dict == new_dict == initial_dict
#     assert id(copied_dict) != id(new_dict)
#
#
@pytest.mark.parametrize('keys,value', data.TEST_DICT_KEYS_AND_VALUES)
def test_dict_fromkeys(keys, value):
    new_dict_from_keys = dict.fromkeys(keys, value)
    new_dict_keys = list(new_dict_from_keys)
    print(new_dict_from_keys)
    for i in range(len(keys)):
        assert new_dict_keys[i] == keys[i]
        assert new_dict_from_keys[new_dict_keys[i]] == value


# @pytest.mark.parametrize('keys,value', data.TEST_DICT_UNHASHABLE_KEYS)
# def test_dict_fromkeys(keys, value):
#     with pytest.raises(TypeError):
#         dict.fromkeys(keys, value)