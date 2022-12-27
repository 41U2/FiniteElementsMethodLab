import numpy as np
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QSlider, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

from test_data_for_plot import *
from PyQt5.QtCore import Qt
import math


class Window(QDialog):

    # constructor
    def __init__(self, t_values, step, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.min_temperature = -10
        self.max_temperature = 10

        # self.button.clicked.connect(lambda: self.plot(self.points, self.t_values))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout

        # t_values = [0.05, 0.1, 0.15, 0.2, 0.25]
        # step = 0.05

        tmp_t_values = []
        for t_value in t_values:
            # print(10**(abs(str(t_value).find('.') - len(str(t_value))) - 1))
            # t_value *= 10**(abs(str(t_value).find('.') - len(str(t_value))) - 1)
            t_value = math.trunc(t_value * 10000)
            t_value = int(t_value)
            # print(t_value)
            tmp_t_values.append(t_value)

        t_values = tmp_t_values

        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setRange(tmp_t_values[0], tmp_t_values[-1])
        print(tmp_t_values[0], tmp_t_values[-1])
        self.slider.setValue(tmp_t_values[0])

        self.step = math.trunc(step * 10000)
        self.slider.setSingleStep(step * 10000)
        self.slider.setTickInterval(step * 10000)
        self.slider.setPageStep(step * 10000)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)

        print('STEP', self.step)

        self.slider.valueChanged.connect(self.update_slider)

        self.result_label = QLabel('', self)

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.result_label.setFont(font)

        layout.addWidget(self.slider)
        layout.addWidget(self.result_label)

        # layout.addRow(slider)
        # layout.addRow(self.result_label)

        self.result_label.setText(f'Значение t: {tmp_t_values[0] / 10000}')

        # setting layout to the main window
        self.setLayout(layout)

        # self.slider.senderSignalIndex()

    def update_slider(self):
        self.result_label.setText(f'Значение t: {self.slider.value() / 10000}')

    def plot(self, points, temperature: float):
        self.figure.clear()

        # test_data = TestDataForPlot()

        self.figure.clear()

        ax = self.figure.add_subplot()

        x_data = [point[0] for point in points]
        y_data = [point[1] for point in points]
        # rgb = [
        #     [
        #         (element - min(0, self.min_temperature)) / (self.max_temperature - min(0, self.min_temperature)),
        #         1 - (element - min(0, self.min_temperature)) / (self.max_temperature - min(0, self.min_temperature)),
        #         0
        #     ] for element in temperature
        # ]
        rgb = [
            [
                element / self.max_temperature,
                1 - element / self.max_temperature,
                0
            ] for element in temperature
        ]
        rgb_final = []
        for elem in rgb:
            if elem[0] < 0:
                elem[0] = 0
            if elem[0] > 1:
                elem[0] = 1
            if elem[1] < 0:
                elem[1] = 0
            if elem[1] > 1:
                elem[1] = 1
            rgb_final.append(elem)

        ax.scatter(x_data, y_data, s=750, c=rgb_final, edgecolors='black', linewidths=1)
        ax.grid(True)

        self.canvas.draw()
