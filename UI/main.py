import sys
from PyQt5 import QtWidgets
from UI.ui_main import *
import traceback


def except_hook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Всё пошло по пизде, давай по новой !:", tb)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = MainPage(MainWindow)
sys.exit(app.exec_())
