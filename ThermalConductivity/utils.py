from copy import deepcopy
from typing import List, Tuple

from SymmetricBandMatrix.matrix import Matrix
from SymmetricBandMatrix.symmetric_band_matrix import SymmetricBandMatrix


def get_triangle_area(vertices: Tuple[List[float], List[float], List[float]]) -> float:
    x = 0
    y = 1
    return 0.5 * abs((vertices[1][x] - vertices[0][x]) * (vertices[2][y] - vertices[0][y]) -
                     (vertices[2][x] - vertices[0][x]) * (vertices[1][y] - vertices[0][y]))


def integrate_by_triangle(
        function,
        triangle_vertices: Tuple[List[float], List[float], List[float]],
        i_vertex_in_triangle: int) -> float:
    assert i_vertex_in_triangle <= 2
    assert i_vertex_in_triangle >= 0
    area = get_triangle_area((triangle_vertices[0], triangle_vertices[1], triangle_vertices[2]))
    neighbours = [1, 2]
    if i_vertex_in_triangle == 1:
        neighbours = [0, 2]
    if i_vertex_in_triangle == 2:
        neighbours = [0, 1]

    middle_point_1 = [
        (triangle_vertices[i_vertex_in_triangle][0] + triangle_vertices[neighbours[0]][0]) / 2.,
        (triangle_vertices[i_vertex_in_triangle][1] + triangle_vertices[neighbours[0]][1]) / 2.,
    ]

    middle_point_2 = [
        (triangle_vertices[i_vertex_in_triangle][0] + triangle_vertices[neighbours[1]][0]) / 2.,
        (triangle_vertices[i_vertex_in_triangle][1] + triangle_vertices[neighbours[1]][1]) / 2.,
    ]

    return area * (function(middle_point_1) + function(middle_point_2)) / 6.


def scattering_procedure(result_matrix_size: int, triangle_indices: List[Tuple[int, int, int]],
                         triangle_elements_matrices: List[Matrix]) -> SymmetricBandMatrix:
    result_matrix = SymmetricBandMatrix.zeros(result_matrix_size, result_matrix_size)

    for matrix_index, single_triangle_indices in enumerate(triangle_indices):
        i, j, k = single_triangle_indices

        result_matrix.set_value(i, i, result_matrix(i, i) + triangle_elements_matrices[matrix_index](0, 0))
        result_matrix.set_value(i, j, result_matrix(i, j) + triangle_elements_matrices[matrix_index](0, 1))
        result_matrix.set_value(i, k, result_matrix(i, k) + triangle_elements_matrices[matrix_index](0, 2))

        result_matrix.set_value(j, i, result_matrix(j, i) + triangle_elements_matrices[matrix_index](1, 0))
        result_matrix.set_value(j, j, result_matrix(j, j) + triangle_elements_matrices[matrix_index](1, 1))
        result_matrix.set_value(j, k, result_matrix(j, k) + triangle_elements_matrices[matrix_index](1, 2))

        result_matrix.set_value(k, i, result_matrix(k, i) + triangle_elements_matrices[matrix_index](2, 0))
        result_matrix.set_value(k, j, result_matrix(k, j) + triangle_elements_matrices[matrix_index](2, 1))
        result_matrix.set_value(k, k, result_matrix(k, k) + triangle_elements_matrices[matrix_index](2, 2))

    return result_matrix


def apply_boundary_conditions(vertices: List[List[float]], thermal_conductivity_matrix: SymmetricBandMatrix,
                              boundary_condition_func, source_vector: Matrix, is_boundary_vertex: List[bool],
                              current_time: float, ) -> Tuple[SymmetricBandMatrix, Matrix]:
    result_matrix = deepcopy(thermal_conductivity_matrix)
    result_vector = deepcopy(source_vector)
    for i_vertex, vertex in enumerate(vertices):
        if not is_boundary_vertex[i_vertex]:
            continue
        x = 0
        y = 1
        # current_time == prev_time + time_step (В соответствии с неявным методом Эйлера предполагаем, что ищем
        # текущие значения {u} на основе предыдущих)
        value_from_boundary_condition = boundary_condition_func(vertex[x], vertex[y], current_time)
        result_matrix.set_value(i_vertex, i_vertex, 1)
        result_vector.set_value(i_vertex, 0, value_from_boundary_condition)

    return result_matrix, result_vector
