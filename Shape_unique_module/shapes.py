import math

# Clase Point
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def compute_distance(self, other_point: "Point") -> float:
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Clase Line
class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.start_point.compute_distance(self.end_point)

# Clase Shape
class Shape:
    def __init__(self, is_regular: bool):
        self.is_regular = is_regular

    def vertices(self) -> list[Point]:
        """Devuelve los vértices de la figura."""
        raise NotImplementedError("Este método debe implementarse en las subclases.")

    def edges(self) -> list[Line]:
        """Devuelve los lados de la figura."""
        raise NotImplementedError("Este método debe implementarse en las subclases.")

    def inner_angles(self) -> list[float]:
        """Devuelve los ángulos internos de la figura."""
        return self.compute_inner_angles()

    def compute_area(self) -> float:
        """Calcula el área de la figura."""
        raise NotImplementedError("Este método debe implementarse en las subclases.")

    def compute_perimeter(self) -> float:
        """Calcula el perímetro de la figura."""
        return sum(edge.length for edge in self.edges())

    def compute_inner_angles(self) -> list[float]:
        """Calcula los ángulos internos de la figura."""
        raise NotImplementedError("Este método debe implementarse en las subclases.")

# Clase Triangle
class Triangle(Shape):
    def __init__(self, vertices: list[Point]):
        super().__init__(is_regular=self.is_equilateral(vertices))
        self._vertices = vertices

    def vertices(self) -> list[Point]:
        return self._vertices

    def edges(self) -> list[Line]:
        return [Line(self._vertices[i], self._vertices[(i + 1) % 3]) for i in range(3)]

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
    def is_equilateral(vertices: list[Point]) -> bool:
        edges = [Line(vertices[i], vertices[(i + 1) % 3]) for i in range(3)]
        return all(math.isclose(edges[0].length, edge.length) for edge in edges)

# Subclases de Triangle
class Isosceles(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        if not self.is_isosceles():
            raise ValueError("Los vértices no forman un triángulo isósceles.")

    def is_isosceles(self) -> bool:
        a, b, c = (edge.length for edge in self.edges())
        return math.isclose(a, b) or math.isclose(a, c) or math.isclose(b, c)

class Equilateral(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        if not self.is_equilateral(vertices):
            raise ValueError("Los vértices no forman un triángulo equilátero.")

class Scalene(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        if not self.is_scalene():
            raise ValueError("Los vértices no forman un triángulo escaleno.")

    def is_scalene(self) -> bool:
        a, b, c = (edge.length for edge in self.edges())
        return not (math.isclose(a, b) or math.isclose(a, c) or math.isclose(b, c))

class Trirectangle(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        if not self.is_right_triangle():
            raise ValueError("Los vértices no forman un triángulo rectángulo.")

    def is_right_triangle(self) -> bool:
        a, b, c = sorted(edge.length for edge in self.edges())
        return math.isclose(a**2 + b**2, c**2)

class Rectangle(Shape):
    def __init__(self, vertices: list[Point]):
        super().__init__(is_regular=self.is_square(vertices))
        self._vertices = vertices

    def vertices(self) -> list[Point]:
        return self._vertices

    def edges(self) -> list[Line]:
        return [Line(self._vertices[i], self._vertices[(i + 1) % 4]) for i in range(4)]

    def compute_area(self) -> float:
        edges = self.edges()
        return edges[0].length * edges[1].length

    def compute_inner_angles(self) -> list[float]:
        return [90.0, 90.0, 90.0, 90.0]

    @staticmethod
    def is_square(vertices: list[Point]) -> bool:
        edges = [Line(vertices[i], vertices[(i + 1) % 4]) for i in range(4)]
        lengths = [edge.length for edge in edges]
        return all(math.isclose(length, lengths[0]) for length in lengths)

# Subclase de Rectangle
class Square(Rectangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        if not self.is_square(vertices):
            raise ValueError("Los vértices no forman un cuadrado.")


#Ejemplo de uso
def main():
    # Triángulo equilátero
    vertices_equilateral = [Point(0, 0), Point(3, 0), Point(1.5, math.sqrt(6.75))]
    equilateral_triangle = Equilateral(vertices_equilateral)
    print("\nTriángulo Equilátero:")
    print("Vértices:", [(v.x, v.y) for v in equilateral_triangle.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in equilateral_triangle.edges()])
    print("Ángulos internos:", equilateral_triangle.inner_angles())
    print("Área:", equilateral_triangle.compute_area())
    print("Perímetro:", equilateral_triangle.compute_perimeter())
    print("Es regular:", equilateral_triangle.is_regular)

    # Triángulo isósceles
    vertices_isosceles = [Point(0, 0), Point(4, 0), Point(2, 3)]
    isosceles_triangle = Isosceles(vertices_isosceles)
    print("\nTriángulo Isósceles:")
    print("Vértices:", [(v.x, v.y) for v in isosceles_triangle.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in isosceles_triangle.edges()])
    print("Ángulos internos:", isosceles_triangle.inner_angles())
    print("Área:", isosceles_triangle.compute_area())
    print("Perímetro:", isosceles_triangle.compute_perimeter())
    print("Es regular:", isosceles_triangle.is_regular)

    # Triángulo escaleno
    vertices_scalene = [Point(0, 0), Point(4, 0), Point(3, 2)]
    scalene_triangle = Scalene(vertices_scalene)
    print("\nTriángulo Escaleno:")
    print("Vértices:", [(v.x, v.y) for v in scalene_triangle.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in scalene_triangle.edges()])
    print("Ángulos internos:", scalene_triangle.inner_angles())
    print("Área:", scalene_triangle.compute_area())
    print("Perímetro:", scalene_triangle.compute_perimeter())
    print("Es regular:", scalene_triangle.is_regular)

    # Triángulo rectángulo
    vertices_trirectangle = [Point(0, 0), Point(3, 0), Point(0, 4)]
    trirectangle_triangle = Trirectangle(vertices_trirectangle)
    print("\nTriángulo Rectángulo:")
    print("Vértices:", [(v.x, v.y) for v in trirectangle_triangle.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in trirectangle_triangle.edges()])
    print("Ángulos internos:", trirectangle_triangle.inner_angles())
    print("Área:", trirectangle_triangle.compute_area())
    print("Perímetro:", trirectangle_triangle.compute_perimeter())
    print("Es regular:", trirectangle_triangle.is_regular)

    # Rectángulo
    vertices_rectangle = [Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3)]
    rectangle = Rectangle(vertices_rectangle)
    print("\nRectángulo:")
    print("Vértices:", [(v.x, v.y) for v in rectangle.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in rectangle.edges()])
    print("Ángulos internos:", rectangle.inner_angles())
    print("Área:", rectangle.compute_area())
    print("Perímetro:", rectangle.compute_perimeter())
    print("Es regular:", rectangle.is_regular)

    # Cuadrado
    vertices_square = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
    square = Square(vertices_square)
    print("\nCuadrado:")
    print("Vértices:", [(v.x, v.y) for v in square.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in square.edges()])
    print("Ángulos internos:", square.inner_angles())
    print("Área:", square.compute_area())
    print("Perímetro:", square.compute_perimeter())
    print("Es regular:", square.is_regular)

if __name__ == "__main__":
    main()