# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(387, 121)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.auto_save_comboBox = QtWidgets.QComboBox(Dialog)
        self.auto_save_comboBox.setObjectName("auto_save_comboBox")
        self.auto_save_comboBox.addItem("")
        self.auto_save_comboBox.addItem("")
        self.auto_save_comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.auto_save_comboBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.jb_checkBox = QtWidgets.QCheckBox(Dialog)
        self.jb_checkBox.setObjectName("jb_checkBox")
        self.verticalLayout.addWidget(self.jb_checkBox)
        self.reset_checkBox = QtWidgets.QCheckBox(Dialog)
        self.reset_checkBox.setObjectName("reset_checkBox")
        self.verticalLayout.addWidget(self.reset_checkBox)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Reset_Button_btn = QtWidgets.QPushButton(Dialog)
        self.Reset_Button_btn.setObjectName("Reset_Button_btn")
        self.horizontalLayout.addWidget(self.Reset_Button_btn)
        self.choose_font_btn = QtWidgets.QPushButton(Dialog)
        self.choose_font_btn.setObjectName("choose_font_btn")
        self.horizontalLayout.addWidget(self.choose_font_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Auto-save frequency"))
        self.auto_save_comboBox.setItemText(0, _translate("Dialog", "Every Turn"))
        self.auto_save_comboBox.setItemText(1, _translate("Dialog", "Every Round"))
        self.auto_save_comboBox.setItemText(2, _translate("Dialog", "Off"))
        self.jb_checkBox.setText(_translate("Dialog", "Join Battle automatically adds 3"))
        self.reset_checkBox.setText(_translate("Dialog", "Reset includes Players"))
        self.Reset_Button_btn.setText(_translate("Dialog", "Reset Fonts"))
        self.choose_font_btn.setText(_translate("Dialog", "Choose Font"))
