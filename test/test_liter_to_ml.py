from pytest import raises, mark
from src.water_overflow.liter_to_ml import liter_to_ml
from src.errors.liters_conversion_error import LitersConversionError


@mark.parametrize('liter,ml', [(1, 1000), (3.3, 3300), (0, 0)])
def test_liter_to_ml(liter, ml):
    assert liter_to_ml(liter) == ml


def test_conversion_fails_on_negative():
    with raises(LitersConversionError):
        liter_to_ml(-3)
