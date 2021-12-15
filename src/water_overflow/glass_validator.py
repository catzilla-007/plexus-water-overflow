from src.errors.glass_validation_error import GlassValidationError
from .glass import Glass


class GlassValidator(object):

    @staticmethod
    def validate(glass: Glass):
        if glass.base < 0:
            raise GlassValidationError(f'glass base {glass.base} should be non-negative')
        if glass.capacity < 0:
            raise GlassValidationError(f'glass capacity {glass.capacity} should be non-negative')
        if glass.line < 0:
            raise GlassValidationError(f'glass line {glass.line} should be non-negative')
        if glass.line > glass.base:
            raise GlassValidationError(f'glass line {glass.line} should be less than the base')
