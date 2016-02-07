# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/HornetBookstore/PycharmProjects/ex-3e-init-tracker/lib/new_character_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(317, 236)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.name_edit = QtWidgets.QLineEdit(Dialog)
        self.name_edit.setObjectName("name_edit")
        self.verticalLayout_3.addWidget(self.name_edit)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.player_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.player_checkBox.setObjectName("player_checkBox")
        self.gridLayout.addWidget(self.player_checkBox, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.legendary_size_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.legendary_size_checkBox.setObjectName("legendary_size_checkBox")
        self.gridLayout.addWidget(self.legendary_size_checkBox, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.Join_battle_box = QtWidgets.QSpinBox(self.groupBox_3)
        self.Join_battle_box.setMinimum(-99)
        self.Join_battle_box.setObjectName("Join_battle_box")
        self.verticalLayout_2.addWidget(self.Join_battle_box)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.current_init_spinbox = QtWidgets.QSpinBox(self.groupBox_3)
        self.current_init_spinbox.setObjectName("current_init_spinbox")
        self.verticalLayout_2.addWidget(self.current_init_spinbox)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add New Character"))
        self.label.setText(_translate("Dialog", "Name"))
        self.player_checkBox.setText(_translate("Dialog", "Player"))
        self.checkBox.setText(_translate("Dialog", "Inert Initiative"))
        self.legendary_size_checkBox.setText(_translate("Dialog", "Legendary Size"))
        self.label_3.setText(_translate("Dialog", "Join Battle Pool"))
        self.label_2.setText(_translate("Dialog", "Used for automatically rolling for NPCs"))
        self.label_4.setText(_translate("Dialog", "Current Initiative"))

