from typing import List, Tuple

from SymmetricBandMatrix.matrix import Matrix
from SymmetricBandMatrix.symmetric_band_matrix import SymmetricBandMatrix
from ThermalConductivity.utils import get_triangle_area, partition_procedure

from .utils import integrate_by_triangle


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
            value = integrate_by_triangle(source_function, triangle_vertices, i_vertex)
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
    triangle_elements_damping_matrices = []

    for i, j, k in triangle_indices:
        triangle_area = get_triangle_area((vertices[i], vertices[j], vertices[k]))
        triangle_element_damping_matrix = Matrix(3, 3, [
            2, 1, 1,
            1, 2, 1,
            1, 1, 2]) * (triangle_area / 12)
        triangle_elements_damping_matrices.append(triangle_element_damping_matrix)

    damping_matrix = partition_procedure(vertices_num, triangle_indices, triangle_elements_damping_matrices)
    return damping_matrix


# Матрица теплопроводности
def get_thermal_conductivity_matrix(vertices: List[List[float]],
                                    triangle_indices: List[Tuple[int, int, int]]) -> SymmetricBandMatrix:
    pass
