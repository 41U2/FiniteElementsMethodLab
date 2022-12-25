from copy import deepcopy
from typing import List, Tuple

from SymmetricBandMatrix.symmetric_band_matrix import SymmetricBandMatrix


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
