from ui_main_page import *
from Triangulation.triangulation import *
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
        self.points = 1
        self.step = 0.05
        self.t_values = [0.05, 0.1, 0.15, 0.2, 0.25]

        self.main_page.init_input_params_button_action(lambda: self.init_input_params())
        self.main_page.create_plot_button_action(lambda: self.create_plot(self.points, self.t_values, self.step))

        self.main_window.show()

    def init_input_params(self):
        self.nx = int(self.main_page.nx_input.toPlainText())
        self.ny = int(self.main_page.ny_input.toPlainText())
        self.hx = list(map(int, self.main_page.hx_input.toPlainText().split(',')))
        self.hy = list(map(int, self.main_page.hy_input.toPlainText().split(',')))
        self.x0 = int(self.main_page.x0_input.toPlainText())
        self.y0 = int(self.main_page.y0_input.toPlainText())
        self.f = self.main_page.f_dropdown.currentText()
        self.phi = self.main_page.phi_dropdown.currentText()
        self.psi = self.main_page.psi_dropdown.currentText()
        self.t = self.main_page.t_input.toPlainText()

        print('input params are set')

        self.invoke_calculation()

    def invoke_calculation(self):

        print('calculation processed')

    def create_plot(self, points, t_values, step):
        # t_values - возможные значения t
        # points:
        # [
        #     ([1, 2], 0.12),
        #     ([2, 2], 0.3),
        # ]
        self.plot = Window(points, t_values, step)
        self.plot.window().show()
        print('plot created')


