import random
from uuid import uuid4
import random_dict


def generate_random_string():
    return str(uuid4().hex)


TEST_LISTS = [
    [],
    [random.randrange(11)],
    [random.uniform(0, 100.1) for i in range(11)],
    [generate_random_string() for i in range(101)],
    [random.choice([True, False]) for i in range(1001)],
    [{1: '1'}],
    [[random.randint(1, 65535)] for i in range(11)],
    # [{i} for i in range(101)],
    list(zip(list(range(1001)), list(range(1001))))
]

TEST_SETS = [
    set(),
    {random.randrange(2, 11)}
]

TEST_DICTS = [
    {},
    random_dict.random_int_dict(1, random.randrange(11)),
    random_dict.random_float_dict(1, random.randrange(101)),
    random_dict.random_string_dict(1, random.randrange(1001)),
    random_dict.random_bool_dict(1, random.randrange(11)),
    random_dict.random_dict(1, random.randrange(11))
]

TEST_HASHABLE_VALUES = [
    random.choice([random.uniform(0, 100.1),
                   random.randrange(12, 65535),
                   generate_random_string(),
                   ('1', '2'),
                   frozenset(['a', 'a', 'e', 'e', 'i', 'o', 'u'])])
]

TEST_UNHASHABLE_VALUES = [
    random.choice([{'1': ' 2'},
                   [1, 2, 3],
                   {'a', 'b', 'c'}])
]

TEST_ITERABLE = [
    random.choice([{'1': ' 2'},
                   [1, 2, 3],
                   {'a', 'b', 'c'},
                   ('1', '2'),
                   'zxc',
                   frozenset(['!', '.', '~'])])
]

TEST_DICT_KEYS_AND_VALUES = [
    (('a', 'b', 'c'), None),
    ((None, True, False), generate_random_string()),
    ((1, 2, 3), random.randrange(11)),
    ((0.0, 10.1, 100.1), 1000.1),
    ((('a', 'b'), (True, False), (1, 2)), (None, None)),

]

TEST_DICT_UNHASHABLE_KEYS = [
    ((TEST_UNHASHABLE_VALUES[0]), None),
    print(((TEST_UNHASHABLE_VALUES[0]), None))
]
