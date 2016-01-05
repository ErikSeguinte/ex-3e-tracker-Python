#!/usr/bin/python3
import sys

from PyQt5 import QtGui, QtCore, QtWidgets

import ZeltInit as Z
from lib import attack_gui, decisive_gui, main_window, new_character_ui, join_battle_gui, character_picker_ui, \
    Modification_Window, other_action_gui, About_gui


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setup_buttons()
        self.setup_menu_items()

        self.statusBar()
        # self.Withering_btn.
        character_list = Z.character_list
        Z.sort_table()
        self.model = QtGui.QStandardItemModel(len(character_list), 5, self)
        self.setup_model()
        self.window2 = None

    def setup_menu_items(self):
        self.actionLoad_Players.triggered.connect(self.add_players_from_file)
        self.actionQuit.triggered.connect(sys.exit)
        self.actionAbout.triggered.connect(self.about_window)
        self.actionLoad_NPCs.triggered.connect(self.load_npcs)

    def about_window(self):
        AboutWindow().exec()

    def load_npcs(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', "", "*.txt")

        if fname[0]:
            Z.add_npcs(fname[0])
        self.setup_model()

    def setup_buttons(self):
        self.Withering_btn.clicked.connect(self.open_attack_window)
        self.Decisive_btn.clicked.connect(self.open_decisive_window)
        self.join_battle_btn.clicked.connect(self.join_battle)
        self.add_npc_btn.clicked.connect(self.open_new_character_window)
        self.modify_init_btn.clicked.connect(self.modify_character)
        self.other_action_btn.clicked.connect(self.other_action_window)
        self.remove_from_combat_btn.clicked.connect(self.remove_character)
        self.reset_btn.clicked.connect(self.reset)

    def modify_character(self):
        if len(Z.character_list) == 0:
            QtWidgets.QMessageBox.warning(self.window2, "Message", "Please add characters first.")
            return
        character_index = CharacterPickerWindow(self.model).exec()
        if character_index is not None:
            character = Z.character_list[character_index]

            values = ModifyCharacterWindow(character_index, self.model).exec()
            if values:
                self.setup_model()

    def other_action_window(self):
        if len(Z.character_list) == 0:
            QtWidgets.QMessageBox.warning(self.window2, "Message", "Please add characters first.")
            return
        values = OtherActionWindow(self.model).exec()

        if values is not None:
            Z.handle_other_actions(*values)
            self.setup_model()

    def join_battle(self):
        c_list = Z.character_list

        if len(c_list) == 0:
            QtWidgets.QMessageBox.warning(self.window2, "Message", "Please add characters first.")
            return

        for character in c_list:
            if character.join_battle_pool == 0:
                # Ask for Initiative

                values = JoinBattleWindow(character.name).exec()
                if values is not None:
                    join_battle = values + 3
                    character.initiative = join_battle
                else:
                    break

            else:
                character.join_battle()

        self.setup_model()

    def open_attack_window(self):
        if len(Z.character_list) <= 1:
            QtWidgets.QMessageBox.warning(self.window2, "Message", "Please add characters first.")

            return

        values = AttackWindow(self.model).exec()

        if values:
            Z.handle_withering(*values)
            Z.sort_table()
            self.setup_model()

    def open_decisive_window(self):
        if len(Z.character_list) <= 1:
            QtWidgets.QMessageBox.warning(self.window2, "Message", "Please add characters first.")
            return
        values = DecisiveWindow(self.model).exec()

        if values:
            if len(values) == 3:
                Z.handle_decisive(*values)

            else:
                Z.handle_gambits(*values)
            Z.sort_table()
            self.setup_model()

    def open_new_character_window(self):

        values = AddCharacterWindow(self.model).exec()

        if values:
            Z.add_npc(*values)
            Z.sort_table()
            self.setup_model()

    def add_players_from_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', "", "*.txt")

        if fname[0]:
            Z.add_players(fname[0])
        self.setup_model()

    def reset(self):
        Z.reset_combat()
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

        progress = self.progressBar

        row = 0
        number_gone = 0

        for character in character_list:
            self.model.setHeaderData(row, QtCore.Qt.Vertical, row)
            self.model.setData(self.model.index(row, 0, QtCore.QModelIndex()), character.name)
            self.model.setData(self.model.index(row, 1, QtCore.QModelIndex()), character.initiative)
            self.model.setData(self.model.index(row, 2, QtCore.QModelIndex()), character.crash_state)
            self.model.setData(self.model.index(row, 3, QtCore.QModelIndex()), character.has_gone)
            if character.shift_target:
                self.model.setData(self.model.index(row, 4, QtCore.QModelIndex()), character.shift_target.name)
            self.model.setData(self.model.index(row, 6, QtCore.QModelIndex()), character)
            row += 1
            if character.has_gone:
                number_gone += 1

        self.tableView.resizeColumnsToContents()

        if row == 0:
            progress.setMaximum(1)
        else:
            progress.setMaximum(row)
        progress.setMinimum(0)
        progress.setValue(number_gone)

    def reset_tracker(self):
        self.reset()

    def remove_character(self):
        if len(Z.character_list) == 0:
            QtWidgets.QMessageBox.warning(self.window2, "Message", "Please add characters first.")
            return

        character_index = CharacterPickerWindow(self.model).exec()
        if character_index is not None:
            character = Z.character_list[character_index]

            Z.character_list.remove(character)
            self.setup_model()


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


class OtherActionWindow(QtWidgets.QDialog, other_action_gui.Ui_Dialog):
    def __init__(self, model, parent=None):
        super().__init__()
        self.setupUi(self)
        self.model = model
        self.character_box.setModel(self.model)

        for action in Z.action_names:
            self.Action_box.addItem(action)
        self.cost_spinbox.setValue(Z.action_dict[self.Action_box.currentText()])
        self.Action_box.activated.connect(self.change_cost)

    def exec(self):
        super().exec()

        if self.result():
            return self.get_values()
        else:
            return None

    def get_values(self):
        cost = self.cost_spinbox.value()
        character_index = self.character_box.currentIndex()
        if self.Action_box.currentText() == "Delay":
            delay = True
        else:
            delay = False

        return character_index, cost, delay

    def change_cost(self):
        self.cost_spinbox.setValue(Z.action_dict[self.Action_box.currentText()])


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
        self.defender_idx = 1
        self.defender_box.currentIndexChanged.connect(self.set_onslaught)
        self.defender = Z.character_list[self.defender_idx]
        self.onslaught_lbl.setText(str(self.defender.onslaught))

    def set_onslaught(self):
        self.defender_idx = self.defender_box.currentIndex()
        self.defender = Z.character_list[self.defender_idx]
        self.onslaught_lbl.setText(str(self.defender.onslaught))

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
        self.defender_idx = 1
        self.defender_box.currentIndexChanged.connect(self.set_onslaught)
        self.defender = Z.character_list[self.defender_idx]
        self.onslaught_lbl.setText(str(self.defender.onslaught))

    def set_onslaught(self):
        self.defender_idx = self.defender_box.currentIndex()
        self.defender = Z.character_list[self.defender_idx]
        self.onslaught_lbl.setText(str(self.defender.onslaught))

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

        values = None

        if gambit_type == "Standard Decisive":
            # prepare for handle_decisive
            values = ((attacker, defender), success, trick)
        else:
            # prepare for handle_gambit
            if self.defender.initiative > Z.gambit_dict[gambit_type]:
                values = ((attacker, defender), success, gambit_type, trick)
            else:
                QtWidgets.QMessageBox.warning(self, "Message",
                                              "This Gambit would have crashed you, and has been canceled.")

        return values

    def set_cost_text(self):
        gambit = self.gambit_combo.currentText()

        if gambit != "Standard Decisive":
            difficulty = Z.gambit_dict[gambit]
            text = "Difficulty: " + str(difficulty)
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
        initiative = self.current_init_spinbox.value()
        values = name, inert_init, join_battle, initiative
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
    def __init__(self, character_index, model):

        super().__init__()
        self.setupUi(self)
        self.comboBox.setModel(model)
        self.c = Z.character_list[character_index]
        self.setup_old_values()

    def setup_old_values(self):

        old_values = self.c.get_values()
        self.name_edit.setText(next(old_values))
        self.Initiative_box.setValue(next(old_values))
        # print(next(old_values))
        self.inertcheckBox.setChecked(next(old_values))
        self.crashed_check.setChecked(next(old_values))
        self.crash_counter_box.setValue(next(old_values))
        self.crash_return_box.setValue(next(old_values))
        self.has_gone_check.setChecked(next(old_values))
        self.join_battle_box.setValue(next(old_values))
        shift_target = next(old_values)
        self.comboBox.setEnabled(self.crashed_check.isChecked())
        if self.crashed_check.isChecked():
            shift_index = Z.character_list.index(shift_target)
            self.comboBox.setCurrentIndex(shift_index)
        self.crashed_recentlycheck.setChecked(next(old_values))
        self.onslaught_spinbox.setValue(next(old_values))

        self.crashed_check.clicked.connect(self.disable_shift)

    def disable_shift(self):
        self.comboBox.setEnabled(self.crashed_check.isChecked())

    def exec(self):
        super().exec()

        if self.result():
            self.get_values()
            return True
        else:
            return None

    def get_values(self):
        name = self.name_edit.text()
        init = self.Initiative_box.value()
        crash_counter = self.crash_counter_box.value()
        crash_return = self.crash_return_box.value()
        join_battle_pool = self.join_battle_box.value()

        crashed = self.crashed_check.isChecked()
        has_gone = self.has_gone_check.isChecked()
        crashed_recently = self.crashed_recentlycheck.isChecked()
        inert_initiative = self.inertcheckBox.isChecked()
        onslaught = self.onslaught_spinbox.value()

        if crashed:
            shift_target = self.comboBox.currentIndex()
        else:
            shift_target = None

        old_values = self.c.get_values()
        kwargs = {}
        # yield self.name
        # yield self.initiative
        # yield self.inert_initiative
        # yield self.crash_state
        # yield self.crash_counter
        # yield self.crash_return_counter
        # yield self.has_gone
        # yield self.join_battle_pool
        # yield self.shift_target
        # yield self.recently_crashed
        if name != next(old_values):
            self.c.name = name
        if init != next(old_values):
            self.c.initiative = init
        if inert_initiative != next(old_values):
            self.c.inert_initiative = inert_initiative
        if crashed != next(old_values):
            self.c.crash_state = crashed
        if crash_counter != next(old_values):
            self.c.crash_counter = crash_counter
        if crash_return != next(old_values):
            self.c.crash_return_counter = crash_return
        if has_gone != next(old_values):
            self.c.has_gone = has_gone
        if join_battle_pool != next(old_values):
            self.c.join_battle_pool = join_battle_pool
        if shift_target != next(old_values):
            self.c.shift_target = shift_target
        if crashed_recently != next(old_values):
            self.c.recently_crashed = crashed_recently
        if onslaught != next(old_values):
            self.c.onslaught = onslaught

        return


class AboutWindow(QtWidgets.QDialog, About_gui.Ui_Dialog):
    def __init__(self, parent=None, ):
        super().__init__()
        self.setupUi(self)

    def exec(self):
        super().exec()


app = QtWidgets.QApplication(sys.argv)
# Z.set_up_test()

window = MainWindow()

window.show()
sys.exit(app.exec())
