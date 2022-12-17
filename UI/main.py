import sys
from PyQt5 import QtWidgets
from UI.ui_main import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = MainPage(MainWindow)
sys.exit(app.exec_())
