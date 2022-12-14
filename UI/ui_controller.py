from copy import deepcopy
from math import sin, sqrt

from CuthillMcKee.CuthillMcKee import CuthillMcKee
from CuthillMcKee.ReNum import apply_new_indices
from ui_main_page import *
from Triangulation.triangulation import *
from ThermalConductivity.solver import ThermalConductivitySolver
from plot import *


class MainPage:

    @staticmethod
    def source_function_0(vertex: List[float], t: float) -> float:
        return 0

    @staticmethod
    def source_function_1(vertex: List[float], t: float) -> float:
        return t ** 2

    @staticmethod
    def source_function_2(vertex: List[float], t: float) -> float:
        return -t ** 2

    @staticmethod
    def source_function_3(vertex: List[float], t: float) -> float:
        return 3 * sin(2 * t)

    @staticmethod
    def source_function_4(vertex: List[float], t: float) -> float:
        return sqrt(vertex[0] ** 2 + vertex[1] ** 2) * t

    @staticmethod
    def source_function_5(vertex: List[float], t: float) -> float:
        return -sqrt(vertex[0] ** 2 + vertex[1] ** 2) * t

    @staticmethod
    def initial_function_0(vertex: List[float]):
        return 0

    @staticmethod
    def initial_function_1(vertex: List[float]):
        return vertex[0]**2 + vertex[1]**2

    @staticmethod
    def initial_function_2(vertex: List[float]):
        return abs(vertex[0]) + abs(vertex[1])

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
        self.added_to_psi_function = None

        # self.main_page.init_input_params_button_action(lambda: self.init_input_params())
        self.main_page.create_plot_button_action(lambda: self.create_plot())

        self.main_window.show()

    @staticmethod
    def added_to_psi_function_0(vertex: List[float], t: float):
        return 0

    @staticmethod
    def added_to_psi_function_1(vertex: List[float], t: float):
        return 2 * t

    @staticmethod
    def added_to_psi_function_2(vertex: List[float], t: float):
        return -2 * t

    @staticmethod
    def added_to_psi_function_3(vertex: List[float], t: float):
        return sqrt(vertex[0] ** 2 + vertex[1] ** 2) * t

    @staticmethod
    def added_to_psi_function_4(vertex: List[float], t: float):
        return -sqrt(vertex[0]**2 + vertex[1]**2) * t

    def border_function(self, vertex: List[float], t: float):
        return self.phi(vertex) + self.added_to_psi_function(vertex, t)

    def init_input_params(self):

        source_functions = [
            self.source_function_0,
            self.source_function_1,
            self.source_function_2,
            self.source_function_3,
            self.source_function_4,
            self.source_function_5
        ]

        initial_functions = [
            self.initial_function_0,
            self.initial_function_1,
            self.initial_function_2
        ]

        added_functions = [
            self.added_to_psi_function_0,
            self.added_to_psi_function_1,
            self.added_to_psi_function_2,
            self.added_to_psi_function_3,
            self.added_to_psi_function_4
        ]

        self.nx = int(self.main_page.nx_input.toPlainText())
        self.ny = int(self.main_page.ny_input.toPlainText())
        self.hx = list(map(float, self.main_page.hx_input.toPlainText().split(',')))
        self.hy = list(map(float, self.main_page.hy_input.toPlainText().split(',')))
        self.x0 = float(self.main_page.x0_input.toPlainText())
        self.y0 = float(self.main_page.y0_input.toPlainText())
        self.f = source_functions[self.main_page.f_dropdown.currentIndex()]
        self.phi = initial_functions[self.main_page.phi_dropdown.currentIndex()]
        self.added_to_psi_function = added_functions[self.main_page.psi_dropdown.currentIndex()]
        self.t = float(self.main_page.t_input.toPlainText())

        print('input params are set')
        #self.compute()

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
        # [[t, [u1, u2, u3, u4...]]] - ?????????????????????? ?? ???????????????? ?????? ?????????????????????????? t
        self.output = deepcopy(solver.solve(
            self.phi,
            self.border_function,
            self.f,
            self.t,
            self.dt
        ))
        # [[x, y], [x, y]]
        self.vertices = deepcopy(new_vertices)
        print('triangulation processed')

    def create_plot(self):
        self.init_input_params()
        self.compute()
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
        self.refresh_plot()
        print('plot created')

    def refresh_plot(self):
        current_t = self.plot.slider.value() / 10000
        for element in self.output:
            element_time = math.trunc(element[0] * 10000) / 10000
            if element_time < current_t:
                continue
            self.plot.plot(self.vertices, element[1])
            break


