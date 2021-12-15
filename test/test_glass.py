from pytest import mark, raises

from src.errors.water_flow_error import WaterFlowError
from src.water_overflow.glass import Glass


def test_first_glass_should_initiate():
    glass = Glass(250)
    assert glass.capacity == 250
    assert glass.base == 0
    assert glass.line == 0


def test_n_glass_should_initiate():
    glass = Glass(200, 10, 3)
    assert glass.capacity == 200
    assert glass.base == 10
    assert glass.line == 3


@mark.parametrize('pour,is_full', [(100, True), (50, False), (130, True), (0, False)])
def test_glass_is_full(pour, is_full):
    glass = Glass(100)
    glass.pour(pour)
    assert glass.is_full() is is_full


def test_glass_is_full_fails():
    glass = Glass(100)
    with raises(WaterFlowError):
        glass.pour(-1)


def test_glass_pour_overflow():
    glass = Glass(10)
    overflow = glass.pour(14)
    assert overflow == 4


def test_glass_get_value():
    glass = Glass(10)
    glass.pour(4)
    assert glass.value == 4
