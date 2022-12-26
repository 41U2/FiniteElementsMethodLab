from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QSlider, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
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

        self.button = QPushButton('Построить график')

        # self.button.clicked.connect(lambda: self.plot(self.points, self.t_values))


        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button.setAutoFillBackground(False)
        self.button.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(100, 100, 100, 166), stop:1 rgba(255, 255, 255, 255));\n"
            "border-with: 10px;\n"
            "border-radius:10px;\n"
            "border-color: rgb(0, 0, 0);")
        self.button.setIconSize(QtCore.QSize(12, 12))

        self.button.setFont(font)
        self.button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button.setAutoFillBackground(False)
        self.button.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(100, 100, 100, 166), stop:1 rgba(255, 255, 255, 255));\n"
            "border-with: 10px;\n"
            "border-radius:10px;\n"
            "border-color: rgb(0, 0, 0);")
        self.button.setIconSize(QtCore.QSize(12, 12))

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.button)

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
        self.slider.setTickInterval(step* 10000)
        self.slider.setPageStep(step* 10000)
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

    def update_slider(self):
        self.result_label.setText(f'Значение t: {self.slider.value() / 10000}')

    def plot(self, points):

        # [
        #     ([1, 2], 0.12),
        #     ([2, 2], 0.3),
        # ]

        # tобщ
        # t1, t2 ... tобщ

        points = [
            ([1, 1], 34),
            ([2, 1], 43),
            ([3, 1], 11),
            ([1, 2], 89),
            ([2, 2], 19),
            ([3, 2], 67),
        ]

        self.figure.clear()

        test_data = TestDataForPlot()

        self.figure.clear()

        ax = self.figure.add_subplot()

        x_data = [point[0][0] for point in points]
        y_data = [point[0][1] for point in points]
        c_values = [point[1] for point in points]

        ax.scatter(x_data, y_data, s=300, c=c_values, cmap='OrRd', edgecolors='black', linewidths=1,
                   norm=plt.Normalize(vmin=min(c_values), vmax=max(c_values)))
        ax.grid(True)

        # refresh canvas
        self.canvas.draw()

