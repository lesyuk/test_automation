import pytest


def test_1():
    assert 1 == 2
    

class TestClass:

    def test_2(self):
        assert 1 != 2

    def test_3(self):
        with pytest.raises(ZeroDivisionError):
            assert 1 / 1
            pytest.fail('No ZeroDivisionError occured')
