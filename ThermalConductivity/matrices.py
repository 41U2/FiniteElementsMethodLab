from typing import List, Tuple

from SymmetricBandMatrix.matrix import Matrix
from SymmetricBandMatrix.symmetric_band_matrix import SymmetricBandMatrix
from ThermalConductivity.utils import get_triangle_area


def get_source_matrix(
        vertices: List[List[float]],
        triangle_indices:
        List[Tuple[int, int, int]],
        source_function,
        boundary_function,
        is_boundary_vertices: List[bool]) -> Matrix:
    n_vertices = len(vertices)
    source_matrix = Matrix.zeros(n_vertices, 1)

    pass


# Матрица демпфирования
def get_damping_matrix(vertices: List[List[float]],
                       triangle_indices: List[Tuple[int, int, int]]) -> SymmetricBandMatrix:
    vertices_num = len(vertices)
    damping_matrix = SymmetricBandMatrix.zeros(vertices_num, vertices_num)
    for i, j, k in triangle_indices:
        triangle_area = get_triangle_area((vertices[i], vertices[j], vertices[k]))
        triangle_element_damping_matrix = Matrix(3, 3, [
            2, 1, 1,
            1, 2, 1,
            1, 1, 2]) * (triangle_area / 12)

        damping_matrix.set_value(i, i, damping_matrix(i, i) + triangle_element_damping_matrix(0, 0))
        damping_matrix.set_value(i, j, damping_matrix(i, j) + triangle_element_damping_matrix(0, 1))
        damping_matrix.set_value(i, k, damping_matrix(i, k) + triangle_element_damping_matrix(0, 2))

        damping_matrix.set_value(j, i, damping_matrix(j, i) + triangle_element_damping_matrix(1, 0))
        damping_matrix.set_value(j, j, damping_matrix(j, j) + triangle_element_damping_matrix(1, 1))
        damping_matrix.set_value(j, k, damping_matrix(j, k) + triangle_element_damping_matrix(1, 2))

        damping_matrix.set_value(k, i, damping_matrix(k, i) + triangle_element_damping_matrix(2, 0))
        damping_matrix.set_value(k, j, damping_matrix(k, j) + triangle_element_damping_matrix(2, 1))
        damping_matrix.set_value(k, k, damping_matrix(k, k) + triangle_element_damping_matrix(2, 2))

    return damping_matrix


# Матрица теплопроводности
def get_thermal_conductivity_matrix(vertices: List[List[float]],
                                    triangle_indices: List[Tuple[int, int, int]]) -> SymmetricBandMatrix:
    pass


def test():
    vertices = [
        [0, 0],
        [24, 0],
        [24, 24],
        [0, 24]
    ]
    triangle_indices = [
        (0, 1, 3),
        (1, 2, 3)
    ]
    damping_matrix = get_damping_matrix(vertices, triangle_indices)
    print(f'{damping_matrix = }')


if __name__ == "__main__":
    test()
