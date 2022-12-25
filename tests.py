from cmath import sqrt

from SymmetricBandMatrix.matrix import Matrix
from ThermalConductivity.matrices import get_damping_matrix


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
    print(f'{damping_matrix = }')
    m = Matrix.zeros(2, 2)
    print(m)


if __name__ == "__main__":
    damping_matrix_test()
