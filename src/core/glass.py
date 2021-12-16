from src.errors.water_flow_error import WaterFlowError


class Glass(object):
    def __init__(self, capacity: int, base=0, line=0):
        self.capacity = capacity
        self.base = base
        self.line = line
        self.content = 0

    def fill(self, value: float) -> float:
        if value < 0:
            raise WaterFlowError('water flow should be non-negative')
        self.content += value
        if self.is_full():
            return self._overflow()
        return 0

    def is_full(self) -> bool:
        if self.content >= self.capacity:
            return True
        return False

    def _overflow(self) -> float:
        overflow = self.content - self.capacity
        self.content = self.capacity
        return overflow
