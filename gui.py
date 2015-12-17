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

        # Model View stuff
        self.model = QtGui.QStandardItemModel(4, 3, self)
        table = self.tableView

        table.setModel(self.model)
        # self.model.insertRow(self,1,QtCore.QModelIndex)

        character_list = self.get_character_list()

        self.model.setData(self.model.index(1, 0), "Name", )



    def print_stuff(self):
        print("OMG")

    def show_file_dialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', )

        print(fname[0])

        if fname[0]:
            ZeltInit.add_players(fname[0])

    def get_character_list(self):
        return ZeltInit.character_list







app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()
sys.exit(app.exec_())
