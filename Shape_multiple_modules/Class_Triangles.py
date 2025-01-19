import math
from . import Class_line, Class_point, Class_shape


# Clase Triangle
class Triangle(Class_shape.Shape):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(is_regular=self.is_equilateral(vertices))
        self._vertices = vertices

    def vertices(self) -> list[Class_point.Point]:
        return self._vertices

    def edges(self) -> list[Class_line.Line]:
        return [Class_line.Line(self._vertices[i], self._vertices[(i + 1) % 3]) for i in range(3)]

    def compute_area(self) -> float:
        a, b, c = (edge.length for edge in self.edges())
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def compute_inner_angles(self) -> list[float]:
        a, b, c = (edge.length for edge in self.edges())
        angles = [
            math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c))),
            math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))),
            math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        ]
        return angles

    @staticmethod
    def is_equilateral(vertices: list[Class_point.Point]) -> bool:
        edges = [Class_line.Line(vertices[i], vertices[(i + 1) % 3]) for i in range(3)]
        return all(math.isclose(edges[0].length, edge.length) for edge in edges)

# Subclases de Triangle
class Isosceles(Triangle):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(vertices)
        if not self.is_isosceles():
            raise ValueError("Los vértices no forman un triángulo isósceles.")

    def is_isosceles(self) -> bool:
        a, b, c = (edge.length for edge in self.edges())
        return math.isclose(a, b) or math.isclose(a, c) or math.isclose(b, c)

class Equilateral(Triangle):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(vertices)
        if not self.is_equilateral(vertices):
            raise ValueError("Los vértices no forman un triángulo equilátero.")

class Scalene(Triangle):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(vertices)
        if not self.is_scalene():
            raise ValueError("Los vértices no forman un triángulo escaleno.")

    def is_scalene(self) -> bool:
        a, b, c = (edge.length for edge in self.edges())
        return not (math.isclose(a, b) or math.isclose(a, c) or math.isclose(b, c))

class Trirectangle(Triangle):
    def __init__(self, vertices: list[Class_point.Point]):
        super().__init__(vertices)
        if not self.is_right_triangle():
            raise ValueError("Los vértices no forman un triángulo rectángulo.")

    def is_right_triangle(self) -> bool:
        a, b, c = sorted(edge.length for edge in self.edges())
        return math.isclose(a**2 + b**2, c**2)