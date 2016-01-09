# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Primefactorx01\Documents\Python\ex-3e-init-tracker\lib\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.progressBar)
        self.progress_bar_lbl = QtWidgets.QLabel(self.centralwidget)
        self.progress_bar_lbl.setObjectName("progress_bar_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.progress_bar_lbl)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Withering_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Withering_btn.setObjectName("Withering_btn")
        self.verticalLayout.addWidget(self.Withering_btn)
        self.Decisive_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Decisive_btn.setObjectName("Decisive_btn")
        self.verticalLayout.addWidget(self.Decisive_btn)
        self.other_action_btn = QtWidgets.QPushButton(self.centralwidget)
        self.other_action_btn.setObjectName("other_action_btn")
        self.verticalLayout.addWidget(self.other_action_btn)
        self.add_npc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_npc_btn.setObjectName("add_npc_btn")
        self.verticalLayout.addWidget(self.add_npc_btn)
        self.join_battle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.join_battle_btn.setObjectName("join_battle_btn")
        self.verticalLayout.addWidget(self.join_battle_btn)
        self.modify_init_btn = QtWidgets.QPushButton(self.centralwidget)
        self.modify_init_btn.setObjectName("modify_init_btn")
        self.verticalLayout.addWidget(self.modify_init_btn)
        self.remove_from_combat_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_from_combat_btn.setObjectName("remove_from_combat_btn")
        self.verticalLayout.addWidget(self.remove_from_combat_btn)
        self.skip_btn = QtWidgets.QPushButton(self.centralwidget)
        self.skip_btn.setObjectName("skip_btn")
        self.verticalLayout.addWidget(self.skip_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 662, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setDefault(False)
        self.reset_btn.setFlat(False)
        self.reset_btn.setObjectName("reset_btn")
        self.verticalLayout.addWidget(self.reset_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLoad_Players = QtWidgets.QAction(MainWindow)
        self.actionLoad_Players.setObjectName("actionLoad_Players")
        self.actionLoad_NPCs = QtWidgets.QAction(MainWindow)
        self.actionLoad_NPCs.setObjectName("actionLoad_NPCs")
        self.actionReadme = QtWidgets.QAction(MainWindow)
        self.actionReadme.setObjectName("actionReadme")
        self.actionSave_Combat = QtWidgets.QAction(MainWindow)
        self.actionSave_Combat.setObjectName("actionSave_Combat")
        self.actionLoad_Combat = QtWidgets.QAction(MainWindow)
        self.actionLoad_Combat.setObjectName("actionLoad_Combat")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionResume_Combat = QtWidgets.QAction(MainWindow)
        self.actionResume_Combat.setObjectName("actionResume_Combat")
        self.actionSave_to_Text_File = QtWidgets.QAction(MainWindow)
        self.actionSave_to_Text_File.setObjectName("actionSave_to_Text_File")
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionLoad_Players)
        self.menuEdit.addAction(self.actionLoad_NPCs)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSave_Combat)
        self.menuEdit.addAction(self.actionSave_to_Text_File)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionLoad_Combat)
        self.menuEdit.addAction(self.actionResume_Combat)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionReadme)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Exalted Initiative"))
        self.progress_bar_lbl.setText(_translate("MainWindow", "Round Progress"))
        self.Withering_btn.setText(_translate("MainWindow", "&Withering Attack"))
        self.Decisive_btn.setText(_translate("MainWindow", "&Decisive && Gambits"))
        self.other_action_btn.setText(_translate("MainWindow", "&Other Actions"))
        self.add_npc_btn.setText(_translate("MainWindow", "&Add NPCs"))
        self.join_battle_btn.setText(_translate("MainWindow", "&Join Battle!"))
        self.modify_init_btn.setText(_translate("MainWindow", "&Modify Character"))
        self.remove_from_combat_btn.setText(_translate("MainWindow", "&Remove from Combat"))
        self.skip_btn.setToolTip(_translate("MainWindow", "Skip character currently at the top of the initiative."))
        self.skip_btn.setText(_translate("MainWindow", "Skip"))
        self.reset_btn.setToolTip(_translate("MainWindow", "Resets tracker, removing all characters"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLoad_Players.setText(_translate("MainWindow", "Load Players"))
        self.actionLoad_NPCs.setText(_translate("MainWindow", "Load NPCs"))
        self.actionReadme.setText(_translate("MainWindow", "Readme"))
        self.actionSave_Combat.setText(_translate("MainWindow", "Save Combat"))
        self.actionLoad_Combat.setText(_translate("MainWindow", "Load Combat"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionResume_Combat.setText(_translate("MainWindow", "Resume Combat"))
        self.actionSave_to_Text_File.setText(_translate("MainWindow", "Save to Text File"))

