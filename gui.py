#!/usr/bin/python3
import sys

from PyQt5 import QtGui, QtCore, QtWidgets

import ZeltInit as Z
from lib import attack_gui, decisive_gui, main_window, new_character_ui, join_battle_gui, character_picker_ui, \
    Modification_Window


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setup_buttons()
        self.actionLoad_Players.triggered.connect(self.show_file_dialog)

        self.statusBar()
        # self.Withering_btn.
        character_list = Z.character_list
        Z.sort_table()
        self.model = QtGui.QStandardItemModel(len(character_list), 5, self)
        self.setup_model()
        self.window2 = None

    def setup_buttons(self):
        self.Withering_btn.clicked.connect(self.open_attack_window)
        self.Decisive_btn.clicked.connect(self.open_decisive_window)
        self.join_battle_btn.clicked.connect(self.join_battle)
        self.add_npc_btn.clicked.connect(self.open_new_character_window)
        self.modify_init_btn.clicked.connect(self.modify_character)

    def modify_character(self):
        if len(Z.character_list) == 0:
            return
        window2 = CharacterPickerWindow(self.model)
        character_index = window2.exec()
        print("Return Successful")
        window3 = ModifyCharacterWindow(character_index)
        values = window3.exec()

    def join_battle(self):
        c_list = Z.character_list

        if len(c_list) == 0:
            return

        for character in c_list:
            if character.join_battle_pool == 0:
                # Ask for Initiative
                self.window2 = JoinBattleWindow(character.name)

                values = self.window2.exec()
                if values:
                    character.initiative = values
                else:
                    break

            else:
                character.join_battle()

        self.setup_model()

    def open_attack_window(self):
        if len(Z.character_list) == 0:
            print('\a')
            return

        self.window2 = AttackWindow(self.model)
        values = self.window2.exec()

        if values:
            Z.handle_withering(*values)
            Z.sort_table()
            self.setup_model()

    def open_decisive_window(self):
        if len(Z.character_list) == 0:
            return
        self.window2 = DecisiveWindow(self.model)
        values = self.window2.exec()

        if values:
            if len(values) == 3:
                Z.handle_decisive(*values)

            else:
                Z.handle_gambits(*values)
            Z.sort_table()
            self.setup_model()

    def open_new_character_window(self):

        self.window2 = AddCharacterWindow(self.model)
        values = self.window2.exec()

        if values:
            Z.add_npc(*values)
            Z.sort_table()
            self.setup_model()

    def show_file_dialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', )

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
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Shift Target")

        self.table = self.tableView
        self.tableView.setModel(self.model)
        character_list = Z.character_list

        Z.sort_table()

        row = 0

        for character in character_list:
            self.model.setHeaderData(row, QtCore.Qt.Vertical, row)
            self.model.setData(self.model.index(row, 0, QtCore.QModelIndex()), character.name)
            self.model.setData(self.model.index(row, 1, QtCore.QModelIndex()), character.initiative)
            self.model.setData(self.model.index(row, 2, QtCore.QModelIndex()), character.crash_state)
            self.model.setData(self.model.index(row, 3, QtCore.QModelIndex()), character.has_gone)
            # if character.shift_target:
            #     self.model.setData(self.model.index(row, 4, QtCore.QModelIndex()), character.shift_target.name)
            row += 1

        self.tableView.resizeColumnsToContents()


class JoinBattleWindow(QtWidgets.QDialog, join_battle_gui.Ui_Dialog):
    def __init__(self, name, parent=None, ):
        super().__init__()
        self.setupUi(self)
        self.groupBox.setTitle(name)

    def exec(self):

        super().exec()

        if self.result():
            return self.get_values()
        else:
            return None

    def get_values(self):
        join_battle = self.spinBox.value()

        return join_battle


class AttackWindow(QtWidgets.QDialog, attack_gui.Ui_Dialog):
    def __init__(self, model, parent=None, ):
        super().__init__()
        self.model = model
        self.setupUi(self)

        self.attacker_box = self.attacker_combo
        self.attacker_box.setModel(self.model)

        self.defender_box = self.defender_combobox
        self.defender_box.setModel(self.model)
        self.defender_box.setCurrentIndex(1)

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
        damage = self.damage_spinbox.value()
        rout = self.spinBox.value()

        if attacker_trick != 0 or defender_trick != 0:
            tricks = True
        else:
            tricks = False

        trick = (tricks, attacker_trick, defender_trick)

        values = (attacker, defender), damage, trick, rout
        return values


class DecisiveWindow(QtWidgets.QDialog, decisive_gui.Ui_Dialog):
    def __init__(self, model, parent=None, ):
        super().__init__()
        self.model = model
        self.setupUi(self)

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

        self.gambit_combo.activated.connect(self.set_cost_text)
        self.set_cost_text()

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
            # prepare for handle_gambit
            values = ((attacker, defender), success, gambit_type, trick)

        return values

    def set_cost_text(self):
        gambit = self.gambit_combo.currentText()

        if gambit != "Standard Decisive":
            cost = Z.gambit_dict[gambit]
            text = str(cost) + " initiative"
        else:
            text = ""
        self.init_cost_label.setText(text)


class AddCharacterWindow(QtWidgets.QDialog, new_character_ui.Ui_Dialog):
    def __init__(self, parent=None, ):
        super().__init__()
        self.setupUi(self)

    def exec(self):

        super().exec()

        if self.result():
            return self.get_values()
        else:
            return None

    def get_values(self):
        name = self.name_edit.text()
        inert_init = self.checkBox.isChecked()
        join_battle = self.Join_battle_box.value()
        values = name, inert_init, join_battle
        return values


class CharacterPickerWindow(QtWidgets.QDialog, character_picker_ui.Ui_Dialog):
    def __init__(self, model, parent=None, ):
        super().__init__()
        self.model = model
        self.setupUi(self)
        self.comboBox.setModel(self.model)

    def exec(self):
        super().exec()

        if self.result():
            return self.get_values()
        else:
            return None

    def get_values(self):
        return self.comboBox.currentIndex()


class ModifyCharacterWindow(QtWidgets.QDialog, Modification_Window.Ui_Dialog):
    def __init__(self, character_index):

        super().__init__()
        self.setupUi(self)
        print("Init!")
        self.character = Z.character_list[character_index]

    def exec(self):
        super().exec()

        if self.result():
            return self.get_values()
        else:
            return None

    def get_values(self):
        pass


app = QtWidgets.QApplication(sys.argv)
# Z.set_up_test()

window = MainWindow()

window.show()
sys.exit(app.exec_())
