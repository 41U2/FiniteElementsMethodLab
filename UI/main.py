import sys
from UI.ui_controller import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = MainPage(MainWindow)
sys.exit(app.exec_())
