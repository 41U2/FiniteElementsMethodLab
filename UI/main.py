import sys
import traceback
from UI.ui_controller import *


# касмтомные ерроры для вывода в консоль
def except_hook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Всё пошло по пизде, давай по новой !:", tb)


sys.excepthook = except_hook


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = MainPage(MainWindow)
sys.exit(app.exec_())
