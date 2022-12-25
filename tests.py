from cmath import sqrt

from ThermalConductivity.matrices import get_damping_matrix, get_thermal_conductivity_matrix


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


if __name__ == "__main__":
    damping_matrix_test()
    thermal_conductivity_matrix_test()
