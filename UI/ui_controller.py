from copy import deepcopy

from CuthillMcKee.CuthillMcKee import CuthillMcKee
from CuthillMcKee.ReNum import apply_new_indices
from ui_main_page import *
from Triangulation.triangulation import *
from ThermalConductivity.solver import ThermalConductivitySolver
from plot import *


class MainPage:

    def __init__(self, main_page_input):
        self.main_window = main_page_input
        self.main_page = UIMainPage(self.main_window)
        self.nx = None
        self.ny = None
        self.hx = None
        self.hy = None
        self.x0 = None
        self.y0 = None
        self.f = None
        self.phi = None
        self.psi = None
        self.t = None
        self.plot = None
        self.output = None
        self.dt = 0.05
        self.vertices = None

        self.main_page.init_input_params_button_action(lambda: self.init_input_params())
        self.main_page.create_plot_button_action(lambda: self.create_plot())

        self.main_window.show()

    def init_input_params(self):
        self.nx = int(self.main_page.nx_input.toPlainText())
        self.ny = int(self.main_page.ny_input.toPlainText())
        self.hx = list(map(float, self.main_page.hx_input.toPlainText().split(',')))
        self.hy = list(map(float, self.main_page.hy_input.toPlainText().split(',')))
        self.x0 = float(self.main_page.x0_input.toPlainText())
        self.y0 = float(self.main_page.y0_input.toPlainText())
        self.f = self.main_page.f_dropdown.currentText()
        self.phi = self.main_page.phi_dropdown.currentText()
        self.psi = self.main_page.psi_dropdown.currentText()
        self.t = float(self.main_page.t_input.toPlainText())

        print('input params are set')

        self.compute()

    @staticmethod
    def source_function(vertex: List[float], t: float) -> float:
        return t**2

    @staticmethod
    def initial_function_1(vertex: List[float]) -> float:
       return pow(vertex[0], 2) + pow(vertex[1], 2)

    @staticmethod
    def boundary_function(vertex: List[float], t: float) -> float:
        return MainPage.initial_function_1(vertex)

    def compute(self):
        vertices_tuple, adjacency_matrix, triangle_indices, is_boundary_vertex_tuple = triangulation(
            self.x0, self.y0, self.nx, self.ny, self.hx, self.hy
        )
        old_to_new_indices = CuthillMcKee(adjacency_matrix)
        new_vertices, new_triangle_indices, new_is_boundary_vertex = apply_new_indices(
            old_to_new_indices,
            vertices_tuple,
            triangle_indices,
            is_boundary_vertex_tuple)
        band_width = band_width_from_triangle_vertex_indices(new_triangle_indices)
        solver = ThermalConductivitySolver.thermal_conductivity_solver(
            new_vertices, new_triangle_indices, new_is_boundary_vertex, band_width
        )
        # [[t, [u1, u2, u3, u4...]]] - температура в вершинах для определённого t
        self.output = deepcopy(solver.solve(
            MainPage.initial_function_1,
            MainPage.boundary_function,
            MainPage.source_function,
            self.t,
            self.dt
        ))
        # [[x, y], [x, y]]
        self.vertices = deepcopy(new_vertices)
        print('triangulation processed')

    def create_plot(self):
        print([elem[0] for elem in self.output])
        self.plot = Window([elem[0] for elem in self.output], self.dt)
        self.refresh_plot()
        self.plot.window().show()
        self.plot.slider.valueChanged.connect(self.refresh_plot)

        max_values = []
        for elem in self.output:
            max_values.append(max(elem[1]))
        self.plot.max_temperature = max(max_values)

        min_values = []
        for elem in self.output:
            min_values.append(min(elem[1]))
        self.plot.min_temperature = min(min_values)

        print('plot created')

    def refresh_plot(self):
        current_t = self.plot.slider.value() / 10000
        for element in self.output:
            element_time = math.trunc(element[0] * 10000) / 10000
            if element_time < current_t:
                continue
            self.plot.plot(self.vertices, element[1])
            break


