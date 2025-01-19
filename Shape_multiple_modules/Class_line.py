from . import Class_point

# Clase Line
class Line:
    def __init__(self, start_point: Class_point.Point, end_point: Class_point.Point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.start_point.compute_distance(self.end_point)