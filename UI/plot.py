from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from test_data_for_plot import *


class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.plot()

        layout = QVBoxLayout()

        layout.addWidget(self.toolbar)

        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def plot(self):

        test_data = TestDataForPlot()

        self.figure.clear()

        ax = self.figure.add_subplot()

        rgb = [[value_data.value, 0, 0] for value_data in test_data.test_data]

        ax.scatter([x_data.x for x_data in test_data.test_data],
                   [y_data.y for y_data in test_data.test_data], s=300,
                   c=rgb, edgecolors='black', linewidths=1)
        ax.grid(True)

        # refresh canvas
        self.canvas.draw()
