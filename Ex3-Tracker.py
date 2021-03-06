#!/usr/bin/python3
import os, sys, platform
from config import TrackerConfig
from requests import get

from PyQt5 import QtGui, QtCore, QtWidgets

import ZeltInit as Z
from lib import attack_gui, decisive_gui, main_window, new_character_ui, join_battle_gui, character_picker_ui, \
    Modification_Window, other_action_gui, About_gui, preferences_window, custom_gambit

version = [0, 4, 3]


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, path):
        super().__init__()

        self.setupUi(self)
        self.setup_buttons()
        self.setup_menu_items()

        # self.statusBar()
        character_list = Z.character_list
        self.model = QtGui.QStandardItemModel(len(character_list), 5, self)
        try:
            fontstring = Z.config['Settings']['tracker Font']
            font = QtGui.QFont()
            font.fromString(fontstring)
            self.tableView.setFont(font)
            self.tableView.horizontalHeader().setFont(font)

        except KeyError:
            pass

        self.setup_model()

        self.window2 = None
        self.application_path = path
        self.save_path = path

    def setup_menu_items(self):
        self.actionLoad_Players.triggered.connect(self.add_players_from_file)
        self.actionQuit.triggered.connect(sys.exit)
        self.actionAbout.triggered.connect(self.about_window)
        self.actionLoad_NPCs.triggered.connect(self.load_npcs)
        self.actionLoad_Combat.triggered.connect(self.load_combat)
        self.actionSave_Combat.triggered.connect(self.save_combat)
        self.actionResume_Combat.triggered.connect(self.resume_combat)
        self.actionSave_to_Text_File.triggered.connect(self.save_to_text)
        self.actionPreferences.triggered.connect(self.preferences_window)
        self.actionCustom_Gambits.triggered.connect(self.custom_gambit_window)
        self.actionChoose_Font.triggered.connect(self.choose_font)
        self.actionCheck_for_Updates.triggered.connect(self.check_for_updates)

    def choose_font(self):
        font, ok = QtWidgets.QFontDialog.getFont()
        if ok:
            # self.lbl.setFont(font)
            # QtWidgets.QApplication.setFont(font)

            self.tableView.setFont(font)
            Z.config['Settings']['tracker font'] = font.toString()
            current_config.save_config()
            self.setup_model()

    def custom_gambit_window(self):
        CustomGambitWindow().exec()

    def about_window(self):
        AboutWindow().exec()

    def load_combat(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', self.save_path,
                                                      "Save File (*.sav *.txt)")
        fname = fname[0]

        if fname:

            self.save_path = os.path.dirname(fname)
            try:
                Z.load_combat(fname)
                self.setup_model()
            except Z.pickle.UnpicklingError:
                # Fallback to text loading
                try:
                    Z.load_combat_from_text(fname)
                    self.setup_model()
                except Exception as error:
                    m = "Unable to load.\n" + str(type(error)) + ": " + str(error)

                    QtWidgets.QMessageBox.warning(self.window2, "Message", m)

    def resume_combat(self):
        try:
            Z.resume_combat()
            self.setup_model()
        except IOError:
            QtWidgets.QMessageBox.warning(self.window2, "Message",
                                          ("Unable to load combat.This may be due to the file being saved on "
                                           "an older version or choosing an invalid file."))
            self.tableView.resizeRowsToContents()
            self.tableView.resizeColumnsToContents()

    def save_combat(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(None, 'Open file', self.save_path, "Save File (*.sav)")
        fname = fname[0]
        if fname:
            self.save_path = os.path.dirname(fname)
            try:
                Z.save_pickler(fname)
            except IOError:
                QtWidgets.QMessageBox.warning(self.window2, "Message", "Cannot open file to write.")
            except Z.pickle.PickleError:
                QtWidgets.QMessageBox.warning(self.window2, "Message", "Unable to create save file")
                # QtWidgets.QFileDialog.getSaveFileName()

    def save_to_text(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(None, 'Open file', self.save_path, "Text file (*.txt)")
        fname = fname[0]
        if fname:
            self.save_path = os.path.dirname(fname)
            try:
                Z.save_combat_to_text(fname)
            except IOError:
                QtWidgets.QMessageBox.warning(self.window2, "Message", "Cannot open file to write.")
                # except Z.pickle.PickleError:
                #     QtWidgets.QMessageBox.warning(self.window2, "Message", "Unable to create save file")
                #     # QtWidgets.QFileDialog.getSaveFileName()
            except Exception as error:
                print(error)

    def load_npcs(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', self.save_path, "Text file (*.txt)")
        fname = fname[0]

        if fname:
            Z.add_npcs(fname)
        self.setup_model()

        if fname:
            self.save_path = os.path.dirname(fname[0])

    def add_players_from_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', self.save_path, "Text file (*.txt)")
        fname = fname[0]

        if fname:
            Z.add_players(fname)
            self.save_path = os.path.dirname(fname)
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
        self.skip_btn.clicked.connect(self.skip)

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
        add_3 = Z.config['Settings'].getboolean('Join Battle automatically adds 3')

        if len(c_list) == 0:
            QtWidgets.QMessageBox.warning(self.window2, "Message", "Please add characters first.")
            return

        i = 0
        values = JoinBattleWindow().exec()
        if values is not None:
            for character in c_list:
                # Ask for Initiative

                join_battle = values[i]
                if add_3:
                    join_battle += 3
                character.initiative = join_battle
                i += 1

        self.setup_model()

    def open_attack_window(self):
        if len(Z.character_list) <= 1:
            QtWidgets.QMessageBox.warning(self.window2, "Message", "Please add characters first.")
            return

        values = AttackWindow(self.model).exec()

        if values:
            Z.handle_withering(**values)
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
            Z.add_npc(**values)
            Z.sort_table()
            self.setup_model()

    def reset(self):
        Z.reset_combat()
        self.setup_model()

    def setup_model(self):

        character_list = Z.character_list
        Z.sort_table()
        self.model = QtGui.QStandardItemModel(len(character_list), 6, self)

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Initiative")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Crash")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Onslaught")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Has Gone")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Shift Target")

        self.table = self.tableView
        self.tableView.setModel(self.model)

        character_list = Z.character_list

        # Z.sort_table()

        progress = self.progressBar

        row = 0
        number_gone = 0

        for character in character_list:
            self.model.setHeaderData(row, QtCore.Qt.Vertical, row)
            self.model.setData(self.model.index(row, 0, QtCore.QModelIndex()), character.name)
            self.model.setData(self.model.index(row, 1, QtCore.QModelIndex()), character.initiative)
            self.model.setData(self.model.index(row, 2, QtCore.QModelIndex()), character.crash_state)
            self.model.setData(self.model.index(row, 3, QtCore.QModelIndex()), character.onslaught)
            self.model.setData(self.model.index(row, 4, QtCore.QModelIndex()), character.has_gone)
            if character.shift_target:
                self.model.setData(self.model.index(row, 5, QtCore.QModelIndex()), character.shift_target.name)
            self.model.setData(self.model.index(row, 6, QtCore.QModelIndex()), character)
            row += 1
            if character.has_gone:
                number_gone += 1

        self.tableView.resizeColumnsToContents()

        if row == 0:
            progress.setMaximum(1)
        else:
            progress.setMaximum(row)
        initial_progress = progress.value()
        try:
            if number_gone < initial_progress and Z.config['Settings'].getboolean('End of round alert'):
                print('End of Round!')
        except Exception as error:
            QtWidgets.QErrorMessage(self.window2, "Error", error)
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

    def skip(self):
        if len(Z.character_list) <= 1:
            QtWidgets.QMessageBox.warning(self.window2, "Message", "Please add characters first.")
            return
        Z.skip_turn()
        self.setup_model()

    def preferences_window(self):
        result = PreferencesWindow().exec()

        if result:
            self.resize(self.sizeHint())
            self.setup_model()

    def check_for_updates(self):
        r = get('https://www.dropbox.com/s/feeycgizkochox0/Ex3-Tracker.txt?dl=1')
        latest = r.text.split('.')
        global version

        new_version_available = False
        for i in range(2):
            number = int(latest[i])
            if number > version[i]:
                new_version_available = True
                break

        if new_version_available:
            QtWidgets.QMessageBox.warning(self.window2, "Message",
                                          "Version " + str(latest[0]) + '.' + str(latest[1]) + '.' + str(
                                              latest[2]) + " now available.")
        else:
            QtWidgets.QMessageBox.warning(self.window2, "Message",
                                          "Version " + str(latest[0]) + '.' + str(latest[1]) + '.' + str(
                                              latest[2]) + " is up to date.")


# class JoinBattleWindow(QtWidgets.QDialog, join_battle_gui.Ui_Dialog):
#     def __init__(self, name, parent=None, ):
#         super().__init__()
#         self.setupUi(self)
#         self.groupBox.setTitle(name)
#
#     def exec(self):
#         super().exec()
#
#         if self.result():
#             return self.get_values()
#         else:
#             return None
#
#     def get_values(self):
#         join_battle = self.spinBox.value()
#         return join_battle


class JoinBattleWindow(QtWidgets.QDialog):
    def __init__(self, parent=None, ):
        Dialog = super().__init__()
        self.setupUi(self)
        # self.groupBox.setTitle(name)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 112)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.spinboxes = self.create_list(self)
        self.horizontalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        # self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # def retranslateUi(self, Dialog):
    #     _translate = QtCore.QCoreApplication.translate
    #     Dialog.setWindowTitle(_translate("Dialog", "Join Battle!"))
    #     self.label.setText(_translate("Dialog", "TextLabel"))

    def create_list(self, Dialog):
        i = 0
        spinboxes = list()
        for character in Z.character_list:
            label = QtWidgets.QLabel(Dialog)
            label.setObjectName(str(character.name))
            label.setText(character.name)
            self.formLayout.setWidget(i, QtWidgets.QFormLayout.LabelRole, label)
            spinBox = QtWidgets.QSpinBox(Dialog)
            spinBox.setObjectName(character.name + "_spinBox")
            self.formLayout.setWidget(i, QtWidgets.QFormLayout.FieldRole, spinBox)
            i += 1
            spinboxes.append(spinBox)
        return spinboxes

    def exec(self):
        super().exec()

        if self.result():
            return self.get_values()
        else:
            return None

    def get_values(self):
        # join_battle = self.spinBox.value()
        values = [(spinbox.value()) for spinbox in self.spinboxes]
        return values


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
        self.success_radioButton.setChecked(True)
        self.defender_box.currentIndexChanged.connect(self.defender_changed)
        self.defender = Z.character_list[self.defender_idx]
        self.onslaught_lbl.setText(str(self.defender.onslaught))
        self.special_rules()

    def defender_changed(self):
        self.set_onslaught()
        self.special_rules()

    def special_rules(self):
        #  Disable rout check if defender not inert.
        self.rout_spinBox.setEnabled(self.defender.inert_initiative)
        self.label_6.setEnabled(self.defender.inert_initiative)

        # disable post soak checkbox unless defender is legendary
        self.post_soak_damage_exceeds_10_checkBox.setEnabled(self.defender.legendary_size)

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
        rout = self.rout_spinBox.value()
        success = self.success_radioButton.isChecked()
        damage_exceeds_10 = self.post_soak_damage_exceeds_10_checkBox.isChecked()

        combatants = (attacker, defender)

        if attacker_trick != 0 or defender_trick != 0:
            tricks = True
        else:
            tricks = False

        trick = (tricks, attacker_trick, defender_trick)

        values = {'combatants': combatants, 'damage': damage, 'trick': trick, 'rout': rout,
                  'damage_exceeds_10': damage_exceeds_10}

        # values = (attacker, defender), damage, trick, rout, success
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

        gambit_list = ['Standard Decisive']
        # gambit_list.append("Standard Decisive")
        if Z.gambits:
            for gambit in Z.gambits:
                gambit_list.append(gambit)
        else:
            for gambit in Z.DEFAULT_GAMBITS:
                gambit_list.append(gambit[0])

        gambit_list.append('Custom Gambit')

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
            print(self.difficulty_spinbox.value())
            # prepare for handle_gambit
            a = Z.character_list[attacker]
            if a.initiative > self.difficulty_spinbox.value() + 1:
                values = ((attacker, defender), success, gambit_type, trick, self.difficulty_spinbox.value())
            else:
                QtWidgets.QMessageBox.warning(self, "Message",
                                              "This Gambit would have crashed you, and has been canceled.")

        return values

    def set_cost_text(self):
        gambit = self.gambit_combo.currentText()

        if gambit == "Standard Decisive":
            self.difficulty_spinbox.setEnabled(False)
            diff = 0

        elif gambit == 'Custom Gambit':
            self.difficulty_spinbox.setEnabled(True)
            diff = 0

        else:
            self.difficulty_spinbox.setEnabled(False)
            diff = Z.gambit_dict[gambit]
        self.difficulty_spinbox.setValue(diff)


class AddCharacterWindow(QtWidgets.QDialog, new_character_ui.Ui_Dialog):
    def __init__(self, parent=None, ):
        super().__init__()
        self.setupUi(self)

        self.checkBox.clicked.connect(self.disable_legendary)

    def disable_legendary(self):
        self.legendary_size_checkBox.setEnabled(not self.checkBox.isChecked())

    def exec(self):

        super().exec()

        if self.result():
            return self.get_values()
        else:
            return None

    def get_values(self):
        values = {}
        values['name'] = self.name_edit.text()
        values['inert'] = self.checkBox.isChecked()
        values['jb_pool'] = self.Join_battle_box.value()
        values['initiative'] = self.current_init_spinbox.value()
        values['player'] = self.player_checkBox.isChecked()
        values['legendary_size'] = self.legendary_size_checkBox.isChecked()
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
        self.old = self.c.get_values()
        self.setup_old_values()

    def setup_old_values(self):
        old = (self.old)

        self.name_edit.setText(old['name'])
        self.Initiative_box.setValue(old['initiative'])

        self.inertcheckBox.setChecked(old['inert_initiative'])
        self.legendary_size_checkBox.setEnabled(not self.inertcheckBox.isChecked())
        self.crashed_check.setChecked(old['crash_state'])
        self.crash_counter_box.setValue(old['crash_counter'])
        self.crash_return_box.setValue(old['crash_return_counter'])
        self.has_gone_check.setChecked(old['has_gone'])
        self.join_battle_box.setValue(old['join_battle_pool'])
        self.comboBox.setEnabled(self.crashed_check.isChecked())
        if self.crashed_check.isChecked() and old['shift_target']:
            shift_index = Z.character_list.index(old['shift_target'])
            self.comboBox.setCurrentIndex(shift_index)
        self.crashed_recentlycheck.setChecked(old['recently_crashed'])
        self.onslaught_spinbox.setValue(old['onslaught'])
        self.player_checkBox.setChecked(old['player'])
        self.delayed_checkBox.setChecked(old['delayed'])
        self.legendary_size_checkBox.setChecked(old['legendary_size'])

        self.crashed_check.clicked.connect(self.disable_shift)
        self.inertcheckBox.clicked.connect(self.disable_legendary)

    def disable_legendary(self):
        print("Click")
        print(str(not self.inertcheckBox.isChecked()))
        self.legendary_size_checkBox.setEnabled(not self.inertcheckBox.isChecked())

    def disable_shift(self):
        self.comboBox.setEnabled(self.crashed_check.isChecked())

    def exec(self):
        super().exec()

        if self.result():
            new = self.get_values()
            self.c.__dict__.update(new)
            return True
        else:
            return None

    def get_values(self):
        new = {}

        new['name'] = self.name_edit.text()
        new['initiative'] = self.Initiative_box.value()
        new['crash_counter'] = self.crash_counter_box.value()
        new['crash_return_counter'] = self.crash_return_box.value()
        new['join_battle_pool'] = self.join_battle_box.value()

        new['crash_state'] = self.crashed_check.isChecked()
        new['has_gone'] = self.has_gone_check.isChecked()
        new['recently_crashed'] = self.crashed_recentlycheck.isChecked()
        new['inert_initiative'] = self.inertcheckBox.isChecked()
        new['onslaught'] = self.onslaught_spinbox.value()

        new['legendary_size'] = self.legendary_size_checkBox.isChecked()
        new['delayed'] = self.delayed_checkBox.isChecked()
        new['player'] = self.player_checkBox.isChecked()

        if new['crash_state']:
            shift_target = Z.character_list[self.comboBox.currentIndex()]
            new['shift_target'] = shift_target
        else:
            new['shift_target'] = None

        changed = {}
        if self.old != new:
            for k in self.old.keys():
                if self.old[k] != new[k]:
                    changed[k] = new[k]
        print(str(changed))
        return changed


class AboutWindow(QtWidgets.QDialog, About_gui.Ui_Dialog):
    def __init__(self, parent=None, ):
        super().__init__()
        self.setupUi(self)
        self.version_label.setText('Version ' + '.'.join([str(x) for x in version]))

    def exec(self):
        super().exec()


class CustomGambitWindow(QtWidgets.QDialog, custom_gambit.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        gambit_string = ""
        gambit_string += self.get_default_gambits()
        gambit_string += self.get_custom_gambits()

        self.Gambits.setText(gambit_string)

    def get_default_gambits(self):

        gambits = Z.DEFAULT_GAMBITS
        # print(gambits)
        gambit_string = ""
        for gambit, difficulty in gambits:
            string = str(gambit) + " : " + str(difficulty) + ",\n"
            gambit_string += string
        return gambit_string

    def get_custom_gambits(self):
        if 'gambits' in Z.config['Custom']:
            gambits = Z.config["Custom"]["gambits"]
            gambit_string = gambits
            return gambit_string
        else:
            return ""

    def exec(self):
        super().exec()

        if self.result():
            gambit_string = self.Gambits.toPlainText()
            try:
                current_config.process_custom_gambits(gambit_string)
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Error", "Unable to parse custom gambits\n" + str(e))


class PreferencesWindow(QtWidgets.QDialog, preferences_window.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.config = Z.config['Settings']
        self.new_font = None
        self.old_font = QtWidgets.QApplication.font()
        self.font_change = False
        try:
            self.setup_values()
        except Exception:
            QtWidgets.QMessageBox.warning(self, "Message", "Unable to load config. Recreating with default settings")
            current_config.recreate_config()
            self.config = Z.config['Settings']
            self.setup_values()

        self.choose_font_btn.clicked.connect(self.change_font)
        self.Reset_Button_btn.clicked.connect(self.reset_fonts)

    def reset_fonts(self):
        Z.config.remove_option('Settings', 'font')
        Z.config.remove_option('Settings', 'tracker font')
        current_config.save_config()
        QtWidgets.QMessageBox.warning(None, "Message",
                                      "Please restart this application to return to your system default fonts.")
        self.close()

    def change_font(self):
        fontDialog = QtWidgets.QFontDialog()

        fontDialog.setCurrentFont(self.old_font)
        font, ok = fontDialog.getFont(self.old_font)
        if ok:
            # self.lbl.setFont(font)
            global app
            QtWidgets.QApplication.setFont(font)
            self.new_font = font.toString()
            self.resize(self.sizeHint())
            self.font_change = True
        else:
            print(font.toString())
            # font.setPointSize(32)
            # global app
            # app.setFont(font)

    def exec(self):
        super().exec()

        if self.result():
            self.set_config()
            return self.font_change
        else:
            QtWidgets.QApplication.setFont(self.old_font)

    def setup_values(self):
        self.set_auto_save()
        self.jb_checkBox.setChecked(self.config.getboolean('Join Battle automatically adds 3'))
        self.reset_checkBox.setChecked(self.config.getboolean('Reset includes players'))
        style = self.config.get('Style', 'default')
        global app

        if style == 'Fusion':
            self.style_comboBox.setCurrentIndex(1)
        else:
            self.style_comboBox.setCurrentIndex(0)

    def set_auto_save(self):
        setting = self.config['Auto-save']
        selections = {'Every Turn': 0, 'Every Round': 1, 'Off': 2}
        self.auto_save_comboBox.setCurrentIndex(selections[setting])

    def get_auto_save(self):
        selections = {'0': 'Every Turn', '1': 'Every Round', '2': 'Off'}
        index = str(self.auto_save_comboBox.currentIndex())
        return selections[index]

    def set_config(self):
        auto_save = self.get_auto_save()
        jb_add_3 = str(self.jb_checkBox.isChecked())
        reset_players = str(self.reset_checkBox.isChecked())

        self.config['Auto-save'] = auto_save
        self.config['Join Battle automatically adds 3'] = jb_add_3
        self.config['Reset includes players'] = reset_players
        if self.new_font:
            self.config['Font'] = self.new_font
        style = str(self.style_comboBox.itemText(self.style_comboBox.currentIndex()))
        print(style)

        self.config['Style'] = style

        global app
        if style == 'Fusion':
            app.setStyle('Fusion')
        else:
            if platform.system() == 'Windows':
                app.setStyle('WindowsVista')

            elif platform.system() == 'Darwin':
                app.setStyle('Macintosh')

        global current_config
        current_config.save_config()


config_name = 'Ex3-Tracker.cfg'

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)

elif __file__:
    application_path = os.path.dirname(__file__)
    version.append('alpha')

app = QtWidgets.QApplication(sys.argv)
default_font = QtGui.QFont().toString()
config_path = os.path.join(application_path, config_name)

current_config = TrackerConfig(application_path, version, default_font)
Z.auto_save_path = os.path.relpath(os.path.join(application_path, '__autosave.sav'))

# app.setStyle('Fusion')



try:
    fontstring = Z.config['Settings']['Font']
    font = QtGui.QFont()
    font.fromString(fontstring)
    app.setFont(font)
except KeyError:
    pass

# Z.set_up_test()

window = MainWindow(application_path)
# QtWidgets.QMessageBox.warning(window, "Message", config_path)


style = Z.config['Settings'].get('Style', 'default')

if style == 'Fusion':
    app.setStyle('Fusion')
else:
    if platform.system() == 'Windows':
        app.setStyle('WindowsVista')

    elif platform.system() == 'Darwin':
        app.setStyle('Macintosh')

window.show()

sys.exit(app.exec())
