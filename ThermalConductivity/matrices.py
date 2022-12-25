# Матрица демпфирования
from typing import List, Tuple

from SymmetricBandMatrix.matrix import Matrix
from SymmetricBandMatrix.symmetric_band_matrix import SymmetricBandMatrix


def get_source_matrix(vertices: List[List[float]], triangle_indices: List[Tuple[int, int, int]],
                      source_function, is_boundary_vertices: List[bool]) -> Matrix:
    pass


# Матрица демпфирования
def get_damping_matrix(vertices: List[List[float]],
                       triangle_indices: List[Tuple[int, int, int]]) -> SymmetricBandMatrix:
    pass


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


if __name__ == "__main__":
    test()
