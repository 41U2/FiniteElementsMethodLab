from copy import deepcopy
from typing import List, Tuple

from SymmetricBandMatrix.symmetric_band_matrix import SymmetricBandMatrix
from SymmetricBandMatrix.matrix import Matrix
from SymmetricBandMatrix.lu_decomposition import LUDecomposition
from .matrices import get_source_vector, get_thermal_conductivity_matrix, get_damping_matrix
from .utils import apply_boundary_conditions


class ThermalConductivitySolver:

    def __init__(
            self,
            thermal_conductivity_matrix: SymmetricBandMatrix,
            damping_matrix: SymmetricBandMatrix,
            vertices: List[List[float]],
            triangle_vertex_indices: List[Tuple[int, int, int]],
            is_boundary_vertex: List[bool]
    ):
        self.thermal_conductivity_matrix = deepcopy(thermal_conductivity_matrix)
        self.damping_matrix = deepcopy(damping_matrix)
        self.vertices = deepcopy(vertices)
        self.triangle_vertex_indices = deepcopy(triangle_vertex_indices)
        self.is_boundary_vertex = deepcopy(is_boundary_vertex)

    # пока что не используем ширину ленты
    @staticmethod
    def thermal_conductivity_solver(
            vertices: List[List[float]],
            triangle_vertex_indices: List[Tuple[int, int, int]],
            is_boundary_vertex: List[bool],
            band_width: int
    ):
        thermal_conductivity_matrix = get_thermal_conductivity_matrix(vertices, triangle_vertex_indices)
        damping_matrix = get_damping_matrix(vertices, triangle_vertex_indices)
        return ThermalConductivitySolver(
            thermal_conductivity_matrix,
            damping_matrix,
            vertices,
            triangle_vertex_indices,
            is_boundary_vertex
        )

    @staticmethod
    def __euler_step__(
            vertices: List[List[float]],
            triangle_vertex_indices: List[Tuple[int, int, int]],
            is_boundary_vertex: List[bool],
            current_values: Matrix,
            thermal_conductivity_matrix: SymmetricBandMatrix,
            damping_matrix: SymmetricBandMatrix,
            boundary_function,
            source_function,
            current_time: float,
            dt: float
    ) -> Matrix:
        left_side_matrix = damping_matrix + thermal_conductivity_matrix * dt
        source_vector = get_source_vector(vertices, triangle_vertex_indices, source_function, current_time)
        right_side_vector = SymmetricBandMatrix.mtimes(damping_matrix, current_values) + source_vector * dt

        left_side_with_boundary_function, right_side_with_boundary_function = apply_boundary_conditions(
            vertices, left_side_matrix, boundary_function, right_side_vector, is_boundary_vertex,
            current_time
        )
        decomposition = LUDecomposition.lu_decompose_sbm(left_side_with_boundary_function)
        return decomposition.solve(right_side_with_boundary_function)

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

        current_time = dt
        print(f"Current time: 0", "\nCurrent_values =\n", current_values)
        while current_time + dt < time:
            current_values = self.__euler_step__(
                self.vertices,
                self.triangle_vertex_indices,
                self.is_boundary_vertex,
                current_values,
                self.thermal_conductivity_matrix,
                self.damping_matrix,
                boundary_function,
                source_function,
                current_time,
                dt
            )
            print(f"Current time: {current_time}", "\nCurrent_values =\n", current_values)
            current_time += dt

        last_dt = time - current_time
        current_values = self.__euler_step__(
            self.vertices,
            self.triangle_vertex_indices,
            self.is_boundary_vertex,
            current_values,
            self.thermal_conductivity_matrix,
            self.damping_matrix,
            boundary_function,
            source_function,
            time,
            last_dt
        )
        print(f"Current time: {time}", "\nCurrent_values =\n", current_values)
        return current_values
