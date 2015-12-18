#!/usr/bin/python3
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import ZeltInit as Z
import main_window
import attack_gui,decisive_gui


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.Withering_btn.clicked.connect(self.open_attack_window)
        self.actionLoad_Players.triggered.connect(self.show_file_dialog)
        self.Decisive_btn.clicked.connect(self.open_decisive_window)
        self.statusBar()
        # self.Withering_btn.
        character_list = Z.character_list
        Z.sort_table()
        self.model = QtGui.QStandardItemModel(len(character_list), 5, self)
        self.setup_model()
        self.window2 = None






        # self.model.setData(QtCore.QModelIndex(0,0),1)

    def open_attack_window(self):

        self.window2 = attack_window(self.model)
        values = self.window2.exec()

        if values:
            Z.handle_withering(*values)
            Z.sort_table()
            self.setup_model()

    def open_decisive_window(self):

            self.window2 = decisive_window(self.model)
            values = self.window2.exec()

            if values:
                if len(values) == 3:
                    Z.handle_decisive(*values)

                else:
                    Z.handle_gambits(*values)
                Z.sort_table()
                self.setup_model()

    def print_stuff(self):
        print("OMG")

    def show_file_dialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', )

        print(fname[0])

        if fname[0]:
            Z.add_players(fname[0])

        self.setup_model()

    def setup_model(self):

        character_list = Z.character_list
        Z.sort_table()
        self.model = QtGui.QStandardItemModel(len(character_list), 5, self)

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "name")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Initiative")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Crash")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Has Gone")

        self.table = self.tableView
        self.tableView.setModel(self.model)
        character_list = Z.character_list
        print(character_list)

        Z.sort_table()

        row = 0

        for character in character_list:
            self.model.setHeaderData(row, QtCore.Qt.Vertical, row)
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
        print("Setup!")

        self.attacker_box = self.attacker_combo
        self.attacker_box.setModel(self.model)

        self.defender_box = self.defender_combobox
        self.defender_box.setModel(self.model)
        self.defender_box.setCurrentIndex(1)

    def exec(self):

        super().exec()
        print(self.result())

        if self.result():
            return self.get_values()
        else:
            return None

    def get_values(self):
        attacker = self.attacker_box.currentIndex()
        defender = self.defender_box.currentIndex()
        attacker_trick = self.a_spinBox.value()
        defender_trick = self.d_spinbox.value()
        damage = self.damage_spinbox.value()

        if attacker_trick != 0 or defender_trick != 0:
            tricks = True
        else:
            tricks = False

        trick = (tricks, attacker_trick, defender_trick)

        values = ((attacker, defender), damage, trick)
        return values


class decisive_window(QtWidgets.QDialog, decisive_gui.Ui_Dialog):
    def __init__(self, model, parent=None, ):
        super().__init__()
        self.model = model
        self.setupUi(self)
        print("Setup!")

        self.attacker_box = self.attacker_combo
        self.attacker_box.setModel(self.model)

        self.defender_box = self.defender_combobox
        self.defender_box.setModel(self.model)
        self.defender_box.setCurrentIndex(1)

        gambit_list = []
        gambit_list.append("Standard Decisive")
        for gambit in Z.GAMBITS:
            gambit_list.append(gambit[0])

        self.gambit_combo.addItems(gambit_list)

    def exec(self):

        super().exec()

        if self.result():
            return self.get_values()
        else:
            return None

    def get_values(self):
        attacker = self.attacker_box.currentIndex()
        defender = self.defender_box.currentIndex()
        attacker_trick = self.a_spinBox.value()
        defender_trick = self.d_spinbox.value()
        gambit_type = self.gambit_combo.currentText()
        success = self.success_radio.isChecked()

        if attacker_trick != 0 or defender_trick != 0:
            tricks = True
        else:
            tricks = False
        trick = (tricks, attacker_trick, defender_trick)

        if gambit_type == "Standard Decisive":
            # prepare for handle_decisive
            values = ((attacker, defender), success, trick)
        else:
            values = ((attacker, defender), success, gambit_type, trick)






        return values

app = QtWidgets.QApplication(sys.argv)
Z.set_up_test()

window = MainWindow()

window.show()
sys.exit(app.exec_())
