from cmath import sqrt
from typing import List

from ThermalConductivity.matrices import \
    get_damping_matrix, \
    get_thermal_conductivity_matrix, \
    get_source_vector
from ThermalConductivity.utils import apply_boundary_conditions
from ThermalConductivity.solver import ThermalConductivitySolver


def damping_matrix_test():
    vertices = [
        [0, 0],
        [sqrt(24), 0],
        [sqrt(24), sqrt(24)],
        [0, sqrt(24)]
    ]
    triangle_indices = [
        (0, 1, 3),
        (1, 2, 3)
    ]
    damping_matrix = get_damping_matrix(vertices, triangle_indices)
    print(f'damping_matrix = \n{damping_matrix}')


def thermal_conductivity_matrix_test():
    vertices = [
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1]
    ]
    triangle_indices = [
        (0, 1, 3),
        (1, 2, 3)
    ]
    thermal_conductivity_matrix = get_thermal_conductivity_matrix(vertices, triangle_indices)
    print(f'thermal_conductivity_matrix = \n{thermal_conductivity_matrix}')
    return thermal_conductivity_matrix


def source_matrix_function(vertex: List[float]) -> float:
    return 2 * vertex[0] + vertex[1] + 1


def source_vector_test():
    vertices = [
        [0, 1],
        [1, 1],
        [1, 0],
        [0, 0]
    ]
    triangle_vertex_indices = [
        (0, 2, 3),
        (2, 0, 1)
    ]
    result = get_source_vector(vertices, triangle_vertex_indices, source_matrix_function)
    print("Source vector: \n", result)
    return result


def boundary_condition_function(x, y, t):
    return x + y + t


def applying_boundary_conditions_test():
    vertices = [
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1]
    ]
    thermal_conductivity_matrix = thermal_conductivity_matrix_test()
    source_vector = source_vector_test()

    prev_time = 0
    time_step = 1
    result_matrix, result_vector = apply_boundary_conditions(vertices, thermal_conductivity_matrix,
                                                             boundary_condition_function, source_vector,
                                                             # is_boundary_vertex=[False, False, True, True],
                                                             is_boundary_vertex=[True, False, False, True],
                                                             current_time=prev_time + time_step)
    print('original_matrix:\n', thermal_conductivity_matrix)
    print('original_vector:\n', source_vector)
    print('result_matrix:\n', result_matrix)
    print('result_vector:\n', result_vector)


def source_function_1(vertex: List[float], t: float) -> float:
    return 0


def initial_function_1(vertex: List[float]) -> float:
    if vertex[0] != 0 or vertex[1] != 0:
         return 2
    return -2


def initial_function_2(vertex: List[float]) -> float:
    if vertex[0] != 0 and vertex[1] != 0:
         return 2
    return -2


def initial_function_3(vertex: List[float]) -> float:
    if vertex[0] == -1 and vertex[1] == -1:
         return 2
    return -2


def boundary_function_1(vertex: List[float], t: float) -> float:
    return initial_function_1(vertex) + t


def boundary_function_2(vertex: List[float], t: float) -> float:
    return initial_function_1(vertex)


def boundary_function_3(vertex: List[float], t: float) -> float:
    return initial_function_1(vertex)


def thermal_conductivity_solver_test():
    vertices = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 0],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]
    triangle_vertex_indices = [
        (0, 1, 3),
        (3, 1, 4),
        (1, 2, 4),
        (4, 2, 5),
        (3, 4, 6),
        (6, 4, 7),
        (4, 5, 7),
        (7, 5, 8)
    ]
    is_boundary_vertex = [
        True,
        True,
        True,
        True,
        False,
        True,
        True,
        True,
        True
    ]
    n_vertices = len(vertices)
    solver = ThermalConductivitySolver.thermal_conductivity_solver(
        vertices,
        triangle_vertex_indices,
        is_boundary_vertex,
        n_vertices)
    result = solver.solve(
        initial_function_1,
        boundary_function_1,
        source_function_1,
        0.5,
        0.1
    )
    kek = 3



if __name__ == "__main__":
    # damping_matrix_test()
    # thermal_conductivity_matrix_test()
    # source_vector_test()
    # applying_boundary_conditions_test()
    thermal_conductivity_solver_test()
