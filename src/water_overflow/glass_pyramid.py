from .glass import Glass
from .glass_validator import GlassValidator
from .liter_to_ml import liter_to_ml


class GlassPyramid(object):
    def __init__(self, capacity: int, liter: float):
        self._ml = liter_to_ml(liter)
        self._capacity = capacity
        self._pyramid: [(int, int), Glass] = {(0, 0): Glass(capacity)}

    def _add_glass(self, base=0, line=0):
        glass = self.get_glass(base, line)
        position = (glass.base, glass.line)

        if position not in self._pyramid:
            self._pyramid[position] = glass

        return glass

    @property
    def glasses(self) -> [(int, int), Glass]:
        return self._pyramid

    def get_glass(self, base, line) -> Glass:
        GlassValidator.validate(base, line)
        try:
            return self._pyramid[(base, line)]
        except KeyError:
            return Glass(self._capacity, base, line)

    def pour(self, ml: float = None, glass: Glass = None):
        if not ml:
            ml = self._ml
        if not glass:
            glass = self._add_glass()

        overflow = glass.pour(ml)

        if overflow > 0:
            l_glass = self._add_glass(glass.base + 1, glass.line)
            r_glass = self._add_glass(glass.base + 1, glass.line + 1)
            self.pour(overflow / 2, l_glass)
            self.pour(overflow / 2, r_glass)
