from src.errors.water_flow_error import WaterFlowError


class Glass(object):
    def __init__(self, capacity: int, base=0, line=0):
        self.capacity = capacity
        self.base = base
        self.line = line
        self._value = 0

    def pour(self, value: float) -> float:
        if value < 0:
            raise WaterFlowError('water flow should be non-negative')
        self._value += value
        if self.is_full():
            return self._overflow()
        return 0

    def is_full(self) -> bool:
        if self._value >= self.capacity:
            return True
        return False

    def _overflow(self) -> float:
        overflow = self._value - self.capacity
        self._value = self.capacity
        return overflow
