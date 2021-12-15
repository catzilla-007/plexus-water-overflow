from pytest import mark, raises

from src.water_overflow.glass_validator import GlassValidator
from src.errors.glass_validation_error import GlassValidationError

valid_glass = [
    (0, 0),
    (1, 1),
    (3, 2),
    (4, 0)
]


@mark.parametrize('base,line', valid_glass)
def test_valid_glass(base, line):
    GlassValidator.validate(base, line)


invalid_glass = [
    (-1, 1),
    (1, -1),
    (1, 2),
]


@mark.parametrize('base,line', invalid_glass)
def test_invalid_glasses_should_raise(base, line):
    with raises(GlassValidationError):
        GlassValidator.validate(base, line)
