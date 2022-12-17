import PyQt5
from ui_main_page import *


class MainPage:

    def __init__(self, main_page_input):
        self.main_window = main_page_input
        self.main_page = UIMainPage(self.main_window)

        self.main_window.show()
