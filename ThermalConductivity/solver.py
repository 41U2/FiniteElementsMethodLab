from copy import deepcopy
from typing import List, Tuple

from SymmetricBandMatrix.symmetric_band_matrix import SymmetricBandMatrix
from SymmetricBandMatrix.matrix import Matrix
from SymmetricBandMatrix.lu_decomposition import LUDecomposition
from matrices import get_source_vector


class ThermalConductivitySolver:

    def __init__(
            self,
            thermal_conductivity_matrix: SymmetricBandMatrix,
            damping_matrix: SymmetricBandMatrix,
            vertices: List[List[float]],
            triangle_vertex_indices: List[Tuple[int, int, int]]):
        self.thermal_conductivity_matrix = deepcopy(thermal_conductivity_matrix)
        self.damping_matrix = deepcopy(damping_matrix)
        self.vertices = deepcopy(vertices)
        self.triangle_vertex_indices = deepcopy(triangle_vertex_indices)

    @staticmethod
    def __euler_step__(
            vertices: List[List[float]],
            triangle_vertex_indices: List[Tuple[int, int, int]],
            current_values: Matrix,
            thermal_conductivity_matrix: SymmetricBandMatrix,
            damping_matrix: SymmetricBandMatrix,
            boundary_function,
            source_function,
            current_time: float,
            dt: float
    ) -> Matrix:
        left_side_matrix = damping_matrix + thermal_conductivity_matrix * dt
        source_vector = get_source_vector(vertices, triangle_vertex_indices, source_function)
        right_side_vector = SymmetricBandMatrix.mtimes(damping_matrix, current_values) + source_vector * dt
        decomposition = LUDecomposition.lu_decompose_sbm(left_side_matrix)
        return decomposition.solve(right_side_vector)

    def solve(
            self,
            initial_function,
            boundary_function,
            source_function,
            time: float,
            dt: float
    ):
        n_vertices = len(self.vertices)
        current_values = Matrix.zeros(n_vertices, 1)
        for i_vertex in range(n_vertices):
            value = initial_function(self.vertices[i_vertex])
            current_values.set_value(i_vertex, 0, value)

        current_time = 0
        while current_time - dt < time:
            kek = 1


