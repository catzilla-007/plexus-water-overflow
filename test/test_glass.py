from pytest import raises, mark
from src.errors.glass_initialization_error import GlassInitializationError

from src.water_overflow.glass import Glass


def test_first_glass_should_initiate():
    glass = Glass(250)
    assert glass.capacity == 250
    assert glass.base == 0
    assert glass.line == 0


valid_glass = [
    (250, 0, 0),
    (200, 1, 1),
    (100, 3, 2),
    (50, 4, 0)
]


@mark.parametrize('capacity,base,line', valid_glass)
def test_glass_should_initiate(capacity, base, line):
    glass = Glass(capacity, base, line)
    assert glass.capacity == capacity
    assert glass.base == base
    assert glass.line == line


invalid_glass = [
    (-1, 1, 1),
    (1, -1, 1),
    (1, 1, -1),
    (1, 1, 2),
]


@mark.parametrize('capacity,base,line', invalid_glass)
def test_invalid_glass_should_raise(capacity, base, line):
    with raises(GlassInitializationError):
        Glass(capacity, base, line)