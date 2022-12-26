from copy import deepcopy

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
        return 0

    @staticmethod
    def initial_function(vertex: List[float]) -> float:
        # return abs(vertex[0]) + abs(vertex[1])
       if vertex[0] != 0 or vertex[1] != 0:
           return 2
       return -2

    @staticmethod
    def boundary_function(vertex: List[float], t: float) -> float:
        return MainPage.initial_function(vertex) # - min(t, 1)

    def compute(self):
        vertices_tuple, adjacency_matrix, triangle_indices, is_boundary_vertex_tuple = triangulation(
            self.x0, self.y0, self.nx, self.ny, self.hx, self.hy
        )
        n_vertices = len(vertices_tuple)
        vertices = [elem[1] for elem in vertices_tuple]
        is_boundary_vertex = [elem[1] for elem in is_boundary_vertex_tuple]
        band_width = band_width_from_triangle_vertex_indices(triangle_indices)
        solver = ThermalConductivitySolver.thermal_conductivity_solver(
            vertices, triangle_indices, is_boundary_vertex, band_width
        )
        # [[t, [u1, u2, u3, u4...]]] - температура в вершинах для определённого t
        self.output = deepcopy(solver.solve(
            MainPage.initial_function,
            MainPage.boundary_function,
            MainPage.source_function,
            self.t,
            self.dt
        ))
        # [[x, y], [x, y]]
        self.vertices = deepcopy(vertices)
        print('triangulation processed')

    def create_plot(self):
        print([elem[0] for elem in self.output])
        self.plot = Window([elem[0] for elem in self.output], self.dt)
        self.refresh_plot()
        self.plot.button.clicked.connect(lambda: self.refresh_plot())
        self.plot.window().show()
        print('plot created')

    def refresh_plot(self):
        current_t = self.plot.slider.value()
        for element in self.output:
            if math.trunc(element[0] * 10000) / 10000 == current_t / 10000:
                self.plot.plot(self.vertices, element[1])
                break


