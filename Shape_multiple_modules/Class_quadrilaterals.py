import math
from . import Class_line, Class_point, Class_shape

class Rectangle(Class_shape.Shape):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(is_regular=self.is_square(vertices))
        self._vertices = vertices

    def vertices(self) -> list[Class_point.Point]:
        return self._vertices

    def edges(self) -> list[Class_line.Line]:
        return [Class_line.Line(self._vertices[i], self._vertices[(i + 1) % 4]) for i in range(4)]

    def compute_area(self) -> float:
        edges = self.edges()
        return edges[0].length * edges[1].length

    def compute_inner_angles(self) -> list[float]:
        return [90.0, 90.0, 90.0, 90.0]

    @staticmethod
    def is_square(vertices: list[Class_point.Point]) -> bool:
        edges = [Class_line.Line(vertices[i], vertices[(i + 1) % 4]) for i in range(4)]
        lengths = [edge.length for edge in edges]
        return all(math.isclose(length, lengths[0]) for length in lengths)

# Subclase de Rectangle
class Square(Rectangle):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(vertices)
        if not self.is_square(vertices):
            raise ValueError("Los vértices no forman un cuadrado.")