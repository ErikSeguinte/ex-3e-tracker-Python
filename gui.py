import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import ZeltInit as Z
import main_window
import attack_gui


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.Withering_btn.clicked.connect(self.open_attack_window)
        self.actionLoad_Players.triggered.connect(self.open_attack_window)
        self.statusBar()
        # self.Withering_btn.
        self.setup_model()
        self.window2 = None


        # self.model.setData(QtCore.QModelIndex(0,0),1)

    def open_attack_window(self):
        if self.window2 == None:
            self.window2 = attack_window(self.model)
        self.window2.show()

    def print_stuff(self):
        print("OMG")

    def show_file_dialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', )

        print(fname[0])

        if fname[0]:
            Z.add_players(fname[0])

        self.setup_model()

    def setup_model(self):
        Z.set_up_test()
        character_list = Z.character_list
        self.model = QtGui.QStandardItemModel(len(character_list), 5, self)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Initiative")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Crash")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Has Gone")

        self.table = self.tableView
        self.tableView.setModel(self.model)
        character_list = Z.character_list
        print(character_list)

        Z.sort_table()

        self.model.setData(self.model.index(0, 0, QtCore.QModelIndex()), "1")

        row = 0

        for character in character_list:
            self.model.setData(self.model.index(row, 4, QtCore.QModelIndex()), row)
            self.model.setData(self.model.index(row, 0, QtCore.QModelIndex()), character.name)
            self.model.setData(self.model.index(row, 1, QtCore.QModelIndex()), character.initiative)
            self.model.setData(self.model.index(row, 2, QtCore.QModelIndex()), character.crash_state)
            self.model.setData(self.model.index(row, 3, QtCore.QModelIndex()), character.has_gone)
            row += 1


class attack_window(QtWidgets.QDialog, attack_gui.Ui_Dialog):
    def __init__(self, model, parent=None, ):
        super().__init__()
        self.model = model
        self.setupUi(self)

        attacker_box = self.attacker_combo
        attacker_box.setModel(self.model)







app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()
sys.exit(app.exec_())
