import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import ZeltInit
import main_window

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
ui = main_window.Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
