from pytest import mark, raises

from src.water_overflow.glass import Glass
from src.water_overflow.glass_validator import GlassValidator
from src.errors.glass_validation_error import GlassValidationError

valid_glass = [
    (250, 0, 0),
    (200, 1, 1),
    (100, 3, 2),
    (50, 4, 0)
]


@mark.parametrize('capacity,base,line', valid_glass)
def test_valid_glass(capacity, base, line):
    glass = Glass(capacity, base, line)
    GlassValidator.validate(glass)


invalid_glass = [
    (-1, 1, 1),
    (1, -1, 1),
    (1, 1, -1),
    (1, 1, 2),
]


@mark.parametrize('capacity,base,line', invalid_glass)
def test_invalid_glasses_should_raise(capacity, base, line):
    with raises(GlassValidationError):
        glass = Glass(capacity, base, line)
        GlassValidator.validate(glass)
