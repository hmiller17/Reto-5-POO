from . import Class_point, Class_line

# Clase Shape
class Shape:
    def __init__(self, is_regular: bool):
        self.is_regular = is_regular

    def vertices(self) -> list[Class_point.Point]:
        """Devuelve los vértices de la figura."""
        raise NotImplementedError("Este método debe implementarse en las subclases.")

    def edges(self) -> list[Class_line.Line]:
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