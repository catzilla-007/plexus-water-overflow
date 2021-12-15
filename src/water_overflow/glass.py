from src.errors.glass_initialization_error import GlassInitializationError


class Glass(object):
    def __init__(self, capacity: int, base=0, line=0):
        self.capacity = capacity
        self.base = base
        self.line = line
        self._value = 0
        self._validate_glass()

    def _validate_glass(self):
        if self.base < 0:
            raise GlassInitializationError('base glass should be non-negative')
        if self.capacity < 0:
            raise GlassInitializationError('glass capacity should be non-negative')
        if self.line < 0:
            raise GlassInitializationError('glass line should be non-negative')
        if self.line > self.base:
            raise GlassInitializationError('glass line should be less than the base')

