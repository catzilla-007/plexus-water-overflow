from src.errors.glass_validation_error import GlassValidationError


class GlassValidator(object):

    @staticmethod
    def validate(base: int, line: int):
        if base < 0:
            raise GlassValidationError(f'glass base {base} should be non-negative')
        if line < 0:
            raise GlassValidationError(f'glass line {line} should be non-negative')
        if line > base:
            raise GlassValidationError(f'glass line {line} should be less than the base')
