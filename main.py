import math
from Shape_multiple_modules import Class_point, Class_Triangles, Class_quadrilaterals

#Ejemplo de uso
def main():
    # Triángulo equilátero
    vertices_equilateral = [Class_point.Point(0, 0), Class_point.Point(3, 0), Class_point.Point(1.5, math.sqrt(6.75))]
    equilateral_triangle = Class_Triangles.Equilateral(vertices_equilateral)
    print("\nTriángulo Equilátero:")
    print("Vértices:", [(v.x, v.y) for v in equilateral_triangle.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in equilateral_triangle.edges()])
    print("Ángulos internos:", equilateral_triangle.inner_angles())
    print("Área:", equilateral_triangle.compute_area())
    print("Perímetro:", equilateral_triangle.compute_perimeter())
    print("Es regular:", equilateral_triangle.is_regular)

    # Triángulo isósceles
    vertices_isosceles = [Class_point.Point(0, 0), Class_point.Point(4, 0), Class_point.Point(2, 3)]
    isosceles_triangle = Class_Triangles.Isosceles(vertices_isosceles)
    print("\nTriángulo Isósceles:")
    print("Vértices:", [(v.x, v.y) for v in isosceles_triangle.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in isosceles_triangle.edges()])
    print("Ángulos internos:", isosceles_triangle.inner_angles())
    print("Área:", isosceles_triangle.compute_area())
    print("Perímetro:", isosceles_triangle.compute_perimeter())
    print("Es regular:", isosceles_triangle.is_regular)

    # Triángulo escaleno
    vertices_scalene = [Class_point.Point(0, 0), Class_point.Point(4, 0), Class_point.Point(3, 2)]
    scalene_triangle = Class_Triangles.Scalene(vertices_scalene)
    print("\nTriángulo Escaleno:")
    print("Vértices:", [(v.x, v.y) for v in scalene_triangle.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in scalene_triangle.edges()])
    print("Ángulos internos:", scalene_triangle.inner_angles())
    print("Área:", scalene_triangle.compute_area())
    print("Perímetro:", scalene_triangle.compute_perimeter())
    print("Es regular:", scalene_triangle.is_regular)

    # Triángulo rectángulo
    vertices_trirectangle = [Class_point.Point(0, 0), Class_point.Point(3, 0), Class_point.Point(0, 4)]
    trirectangle_triangle = Class_Triangles.Trirectangle(vertices_trirectangle)
    print("\nTriángulo Rectángulo:")
    print("Vértices:", [(v.x, v.y) for v in trirectangle_triangle.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in trirectangle_triangle.edges()])
    print("Ángulos internos:", trirectangle_triangle.inner_angles())
    print("Área:", trirectangle_triangle.compute_area())
    print("Perímetro:", trirectangle_triangle.compute_perimeter())
    print("Es regular:", trirectangle_triangle.is_regular)

    # Rectángulo
    vertices_rectangle = [Class_point.Point(0, 0), Class_point.Point(4, 0), Class_point.Point(4, 3), Class_point.Point(0, 3)]
    rectangle = Class_quadrilaterals.Rectangle(vertices_rectangle)
    print("\nRectángulo:")
    print("Vértices:", [(v.x, v.y) for v in rectangle.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in rectangle.edges()])
    print("Ángulos internos:", rectangle.inner_angles())
    print("Área:", rectangle.compute_area())
    print("Perímetro:", rectangle.compute_perimeter())
    print("Es regular:", rectangle.is_regular)

    # Cuadrado
    vertices_square = [Class_point.Point(0, 0), Class_point.Point(2, 0), Class_point.Point(2, 2), Class_point.Point(0, 2)]
    square = Class_quadrilaterals.Square(vertices_square)
    print("\nCuadrado:")
    print("Vértices:", [(v.x, v.y) for v in square.vertices()])
    print("Longitudes de aristas:", [edge.length for edge in square.edges()])
    print("Ángulos internos:", square.inner_angles())
    print("Área:", square.compute_area())
    print("Perímetro:", square.compute_perimeter())
    print("Es regular:", square.is_regular)

if __name__ == "__main__":
    main()