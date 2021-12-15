from .glass import Glass


class GlassPyramid(object):
    def __init__(self):
        self._pyramid: [(int, int), Glass] = {(0,0): Glass(250)}

    def pour(self, liters: int):
        pass
