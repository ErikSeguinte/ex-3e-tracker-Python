# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Primefactorx01\Documents\Python\ex-3e-init-tracker\lib\preferences_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(415, 88)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.horizontalLayout.addLayout(self.formLayout)
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
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Auto-save frequency"))
        self.auto_save_comboBox.setItemText(0, _translate("Dialog", "Every Turn"))
        self.auto_save_comboBox.setItemText(1, _translate("Dialog", "Every Round"))
        self.auto_save_comboBox.setItemText(2, _translate("Dialog", "Never"))
        self.jb_checkBox.setText(_translate("Dialog", "Join Battle automatically adds 3"))
        self.reset_checkBox.setText(_translate("Dialog", "Reset includes Players"))
