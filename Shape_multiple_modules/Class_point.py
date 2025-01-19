import math

# Clase Point
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def compute_distance(self, other_point: "Point") -> float:
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)