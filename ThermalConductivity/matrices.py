from typing import List, Tuple

from SymmetricBandMatrix.matrix import Matrix
from SymmetricBandMatrix.symmetric_band_matrix import SymmetricBandMatrix
from ThermalConductivity.utils import get_triangle_area

from .utils import intergrate_by_triangle


def get_source_matrix(
        vertices: List[List[float]],
        triangle_indices: List[Tuple[int, int, int]],
        source_function,
        boundary_function,
        is_boundary_vertices: List[bool]) -> Matrix:
    n_vertices = len(vertices)
    n_triangles = len(triangle_indices)
    source_matrix = Matrix.zeros(n_vertices, 1)
    for i_triangle in range(n_triangles):
        triangle_vertices = (
            vertices[triangle_indices[i_triangle][0]],
            vertices[triangle_indices[i_triangle][1]],
            vertices[triangle_indices[i_triangle][2]]
        )
        for i_vertex in range(3):
            value = intergrate_by_triangle(source_function, triangle_vertices, i_vertex)
            current_value = source_matrix(triangle_indices[i_triangle][i_vertex], 0)
            source_matrix.set_value(triangle_indices[i_triangle][i_vertex], 0, current_value + value)

    for i_vertex in range(n_vertices):
        if not is_boundary_vertices[i_vertex]:
            continue
        source_matrix.set_value(i_vertex, 0, boundary_function(vertices[i_vertex]))

    return source_matrix


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
