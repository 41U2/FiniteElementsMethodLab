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

        self.main_page.init_input_params_button_action(lambda: self.init_input_params())
        self.main_page.create_plot_button_action(lambda: self.create_plot())

        self.main_window.show()

    def init_input_params(self):
        self.nx = int(self.main_page.nx_input.toPlainText())
        self.ny = int(self.main_page.ny_input.toPlainText())
        self.hx = list(map(int, self.main_page.hx_input.toPlainText().split(',')))
        self.hy = list(map(int, self.main_page.hy_input.toPlainText().split(',')))
        self.x0 = int(self.main_page.x0_input.toPlainText())
        self.y0 = int(self.main_page.y0_input.toPlainText())
        self.f = self.main_page.f_input.toPlainText()
        self.phi = self.main_page.phi_input.toPlainText()
        self.psi = self.main_page.psi_input.toPlainText()
        self.t = self.main_page.t_input.toPlainText()

        print('input params are set')

        self.invoke_triangulation()

    def invoke_triangulation(self):
        triangulation(self.x0, self.y0, self.nx, self.ny, self.hx, self.hy)
        print('triangulation processed')

    def create_plot(self):
        self.plot = Window()
        self.plot.window().show()
        print('plot created')


