import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import ZeltInit
import main_window


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.Withering_btn.clicked.connect(self.print_stuff)
        self.actionLoad_Players.triggered.connect(self.show_file_dialog)
        self.statusBar()
        # self.Withering_btn.

    def print_stuff(self):
        print("OMG")

    def show_file_dialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', )

        print(fname[0])

        if fname[0]:
            ZeltInit.add_players(fname[0])


class InitView(QtWidgets.QAbstractItemView):
    def __init__(self, parent=None):
        super().__init__()






app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()
sys.exit(app.exec_())
