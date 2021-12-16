from pytest import raises, fixture

from src.core.glass_pyramid import GlassPyramid
from src.errors.glass_validation_error import GlassValidationError


@fixture()
def pyramid():
    yield GlassPyramid(250, 1)


def test_glass_pyramid_initialises(pyramid):
    glass = pyramid.get_glass(0, 0)
    assert glass.capacity == 250


def test_glass_pyramid_invalid_glass(pyramid):

    with raises(GlassValidationError):
        pyramid.get_glass(2, 3)
        pyramid.get_glass(-1, 0)


def test_pour_water_in_pyramid(pyramid):
    pyramid.pour()

    glass = pyramid.get_glass(0, 0)
    glass2 = pyramid.get_glass(2, 2)
    assert glass.content == 250
    assert glass2.content == 62.5
