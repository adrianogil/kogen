import types
from kogen import utils


def test_opposite_direction():
    assert utils.opposite_direction('north') == 'south'
    assert utils.opposite_direction('south') == 'north'
    assert utils.opposite_direction('west') == 'east'
    assert utils.opposite_direction('east') == 'west'


def test_capitalize():
    assert utils.capitalize('hello') == 'Hello'
    assert utils.capitalize('a') == 'A'


def test_is_int():
    assert utils.is_int('123')
    assert utils.is_int('-5')
    assert not utils.is_int('3.14')
    assert not utils.is_int('ten')


def test_get_random(monkeypatch):
    # force randint to return the upper bound to test edge behaviour
    monkeypatch.setattr(utils, 'randint', lambda a, b: b)
    data = [1, 2, 3]
    assert utils.get_random(data) == data[-1]
