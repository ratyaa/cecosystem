from dataclasses import dataclass

@dataclass
class Coord:
    x: float
    y: float

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)
    __radd__ = __add__
    
    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y);
    __rsub__ = __sub__

    def __mul__(self, factor):
        return Coord(self.x * factor, self.y * factor)
    __rmul__ = __mul__
