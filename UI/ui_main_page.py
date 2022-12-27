from PyQt5 import QtWidgets, QtCore, QtGui


class UIMainPage:

    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 470, 664, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.init_input_params_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.init_input_params_button.sizePolicy().hasHeightForWidth())
        self.init_input_params_button.setSizePolicy(sizePolicy)
        self.init_input_params_button.setMinimumSize(QtCore.QSize(200, 60))
        self.init_input_params_button.setMaximumSize(QtCore.QSize(200, 60))
        self.init_input_params_button.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.init_input_params_button.setFont(font)
        self.init_input_params_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.init_input_params_button.setAutoFillBackground(False)
        self.init_input_params_button.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(100, 100, 100, 166), stop:1 rgba(255, 255, 255, 255));\n"
            "border-with: 10px;\n"
            "border-radius:10px;\n"
            "border-color: rgb(0, 0, 0);")
        self.init_input_params_button.setIconSize(QtCore.QSize(12, 12))
        self.init_input_params_button.setObjectName("init_input_params_button")
        self.gridLayout.addWidget(self.init_input_params_button, 0, 0, 1, 1)
        self.create_plot_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_plot_button.sizePolicy().hasHeightForWidth())
        self.create_plot_button.setSizePolicy(sizePolicy)
        self.create_plot_button.setMinimumSize(QtCore.QSize(200, 60))
        self.create_plot_button.setMaximumSize(QtCore.QSize(200, 60))
        self.create_plot_button.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.create_plot_button.setFont(font)
        self.create_plot_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_plot_button.setAutoFillBackground(False)
        self.create_plot_button.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(100, 100, 100, 166), stop:1 rgba(255, 255, 255, 255));\n"
            "border-with: 10px;\n"
            "border-radius:10px;\n"
            "border-color: rgb(0, 0, 0);")
        self.create_plot_button.setIconSize(QtCore.QSize(12, 12))
        self.create_plot_button.setObjectName("create_plot_button")
        self.gridLayout.addWidget(self.create_plot_button, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 30, 558, 183))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ny_input = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ny_input.sizePolicy().hasHeightForWidth())
        self.ny_input.setSizePolicy(sizePolicy)
        self.ny_input.setMinimumSize(QtCore.QSize(50, 30))
        self.ny_input.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ny_input.setFont(font)
        self.ny_input.setObjectName("ny_input")
        self.gridLayout_4.addWidget(self.ny_input, 1, 2, 1, 1)
        self.ny_text = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ny_text.sizePolicy().hasHeightForWidth())
        self.ny_text.setSizePolicy(sizePolicy)
        self.ny_text.setMinimumSize(QtCore.QSize(50, 0))
        self.ny_text.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ny_text.setFont(font)
        self.ny_text.setObjectName("ny_text")
        self.gridLayout_4.addWidget(self.ny_text, 1, 1, 1, 1)
        self.hy_input = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hy_input.sizePolicy().hasHeightForWidth())
        self.hy_input.setSizePolicy(sizePolicy)
        self.hy_input.setMinimumSize(QtCore.QSize(250, 30))
        self.hy_input.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hy_input.setFont(font)
        self.hy_input.setObjectName("hy_input")
        self.gridLayout_4.addWidget(self.hy_input, 1, 5, 1, 1)
        self.x0_text = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x0_text.sizePolicy().hasHeightForWidth())
        self.x0_text.setSizePolicy(sizePolicy)
        self.x0_text.setMinimumSize(QtCore.QSize(50, 0))
        self.x0_text.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.x0_text.setFont(font)
        self.x0_text.setObjectName("x0_text")
        self.gridLayout_4.addWidget(self.x0_text, 2, 1, 1, 1)
        self.t_input = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_input.sizePolicy().hasHeightForWidth())
        self.t_input.setSizePolicy(sizePolicy)
        self.t_input.setMinimumSize(QtCore.QSize(50, 30))
        self.t_input.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.t_input.setFont(font)
        self.t_input.setObjectName("t_input")
        self.gridLayout_4.addWidget(self.t_input, 2, 5, 1, 1)
        self.hy_text = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hy_text.sizePolicy().hasHeightForWidth())
        self.hy_text.setSizePolicy(sizePolicy)
        self.hy_text.setMinimumSize(QtCore.QSize(50, 0))
        self.hy_text.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.hy_text.setFont(font)
        self.hy_text.setObjectName("hy_text")
        self.gridLayout_4.addWidget(self.hy_text, 1, 4, 1, 1)
        self.nx_input = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nx_input.sizePolicy().hasHeightForWidth())
        self.nx_input.setSizePolicy(sizePolicy)
        self.nx_input.setMinimumSize(QtCore.QSize(50, 30))
        self.nx_input.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nx_input.setFont(font)
        self.nx_input.setObjectName("nx_input")
        self.gridLayout_4.addWidget(self.nx_input, 0, 2, 1, 1)
        self.hx_input = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hx_input.sizePolicy().hasHeightForWidth())
        self.hx_input.setSizePolicy(sizePolicy)
        self.hx_input.setMinimumSize(QtCore.QSize(250, 30))
        self.hx_input.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hx_input.setFont(font)
        self.hx_input.setObjectName("hx_input")
        self.gridLayout_4.addWidget(self.hx_input, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 3, 1, 1)
        self.y0_input = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y0_input.sizePolicy().hasHeightForWidth())
        self.y0_input.setSizePolicy(sizePolicy)
        self.y0_input.setMinimumSize(QtCore.QSize(50, 30))
        self.y0_input.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.y0_input.setFont(font)
        self.y0_input.setObjectName("y0_input")
        self.gridLayout_4.addWidget(self.y0_input, 3, 2, 1, 1)
        self.nx_text = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nx_text.sizePolicy().hasHeightForWidth())
        self.nx_text.setSizePolicy(sizePolicy)
        self.nx_text.setMinimumSize(QtCore.QSize(50, 0))
        self.nx_text.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nx_text.setFont(font)
        self.nx_text.setObjectName("nx_text")
        self.gridLayout_4.addWidget(self.nx_text, 0, 1, 1, 1)
        self.y0_text = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y0_text.sizePolicy().hasHeightForWidth())
        self.y0_text.setSizePolicy(sizePolicy)
        self.y0_text.setMinimumSize(QtCore.QSize(50, 0))
        self.y0_text.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.y0_text.setFont(font)
        self.y0_text.setObjectName("y0_text")
        self.gridLayout_4.addWidget(self.y0_text, 3, 1, 1, 1)
        self.x0_input = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x0_input.sizePolicy().hasHeightForWidth())
        self.x0_input.setSizePolicy(sizePolicy)
        self.x0_input.setMinimumSize(QtCore.QSize(50, 30))
        self.x0_input.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x0_input.setFont(font)
        self.x0_input.setObjectName("x0_input")
        self.gridLayout_4.addWidget(self.x0_input, 2, 2, 1, 1)
        self.t_text = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_text.sizePolicy().hasHeightForWidth())
        self.t_text.setSizePolicy(sizePolicy)
        self.t_text.setMinimumSize(QtCore.QSize(50, 0))
        self.t_text.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.t_text.setFont(font)
        self.t_text.setObjectName("t_text")
        self.gridLayout_4.addWidget(self.t_text, 2, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 6, 1, 1)
        self.hx_text = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hx_text.sizePolicy().hasHeightForWidth())
        self.hx_text.setSizePolicy(sizePolicy)
        self.hx_text.setMinimumSize(QtCore.QSize(50, 0))
        self.hx_text.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.hx_text.setFont(font)
        self.hx_text.setObjectName("hx_text")
        self.gridLayout_4.addWidget(self.hx_text, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 230, 455, 226))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 4, 1, 1)
        self.f_text = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_text.sizePolicy().hasHeightForWidth())
        self.f_text.setSizePolicy(sizePolicy)
        self.f_text.setMinimumSize(QtCore.QSize(100, 0))
        self.f_text.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.f_text.setFont(font)
        self.f_text.setObjectName("f_text")
        self.gridLayout_3.addWidget(self.f_text, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(35, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_3.addItem(spacerItem6, 5, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_3.addItem(spacerItem7, 1, 3, 1, 1)
        self.f_dropdown = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_dropdown.sizePolicy().hasHeightForWidth())
        self.f_dropdown.setSizePolicy(sizePolicy)
        self.f_dropdown.setMinimumSize(QtCore.QSize(250, 30))
        self.f_dropdown.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.f_dropdown.setFont(font)
        self.f_dropdown.setObjectName("f_dropdown")
        self.gridLayout_3.addWidget(self.f_dropdown, 2, 3, 1, 1)
        self.phi_text = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phi_text.sizePolicy().hasHeightForWidth())
        self.phi_text.setSizePolicy(sizePolicy)
        self.phi_text.setMinimumSize(QtCore.QSize(100, 0))
        self.phi_text.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.phi_text.setFont(font)
        self.phi_text.setObjectName("phi_text")
        self.gridLayout_3.addWidget(self.phi_text, 3, 1, 1, 1)
        self.psi_text = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.psi_text.sizePolicy().hasHeightForWidth())
        self.psi_text.setSizePolicy(sizePolicy)
        self.psi_text.setMinimumSize(QtCore.QSize(100, 0))
        self.psi_text.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.psi_text.setFont(font)
        self.psi_text.setObjectName("psi_text")
        self.gridLayout_3.addWidget(self.psi_text, 4, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 1, 2, 1, 1)
        self.phi_dropdown = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phi_dropdown.sizePolicy().hasHeightForWidth())
        self.phi_dropdown.setSizePolicy(sizePolicy)
        self.phi_dropdown.setMinimumSize(QtCore.QSize(250, 30))
        self.phi_dropdown.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phi_dropdown.setFont(font)
        self.phi_dropdown.setObjectName("phi_dropdown")
        self.gridLayout_3.addWidget(self.phi_dropdown, 3, 3, 1, 1)
        self.psi_dropdown = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.psi_dropdown.sizePolicy().hasHeightForWidth())
        self.psi_dropdown.setSizePolicy(sizePolicy)
        self.psi_dropdown.setMinimumSize(QtCore.QSize(250, 30))
        self.psi_dropdown.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.psi_dropdown.setFont(font)
        self.psi_dropdown.setObjectName("psi_dropdown")
        self.gridLayout_3.addWidget(self.psi_dropdown, 4, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.set_dropdown_list_values()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.init_input_params_button.setText(_translate("MainWindow", "Ввести значения"))
        self.create_plot_button.setText(_translate("MainWindow", "Построить график"))
        self.ny_text.setText(_translate("MainWindow", "Ny"))
        self.x0_text.setText(_translate("MainWindow", "x0"))
        self.hy_text.setText(_translate("MainWindow", "hy"))
        self.nx_text.setText(_translate("MainWindow", "Nx"))
        self.y0_text.setText(_translate("MainWindow", "y0"))
        self.t_text.setText(_translate("MainWindow", "t"))
        self.hx_text.setText(_translate("MainWindow", "hx"))
        self.f_text.setText(_translate("MainWindow", "f(x,y,t)"))
        self.phi_text.setText(_translate("MainWindow", "φ(x,y)"))
        self.psi_text.setText(_translate("MainWindow", "ψ(x,y,t)"))

    def set_dropdown_list_values(self):
        self.f_dropdown.addItem("значение f1")
        self.f_dropdown.addItem("значение f2")

        self.phi_dropdown.addItem("значение phi1")
        self.phi_dropdown.addItem("значение phi2")

        self.psi_dropdown.addItem("значение psi1")
        self.psi_dropdown.addItem("значение psi2")
        self.psi_dropdown.addItem("значение psi3")

    def init_input_params_button_action(self, lambda_expression):
        self.init_input_params_button.clicked.connect(lambda_expression)

    def create_plot_button_action(self, labmda_expression):
        self.create_plot_button.clicked.connect(labmda_expression)
