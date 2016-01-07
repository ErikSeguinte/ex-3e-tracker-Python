# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/HornetBookstore/PycharmProjects/ex-3e-init-tracker/lib/other_action_gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(358, 110)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.character_box = QtWidgets.QComboBox(Dialog)
        self.character_box.setObjectName("character_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.character_box)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Action_box = QtWidgets.QComboBox(Dialog)
        self.Action_box.setObjectName("Action_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Action_box)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cost_spinbox = QtWidgets.QSpinBox(Dialog)
        self.cost_spinbox.setObjectName("cost_spinbox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cost_spinbox)
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
        Dialog.setWindowTitle(_translate("Dialog", "Other Action Dialog"))
        self.label.setText(_translate("Dialog", "Character"))
        self.label_2.setText(_translate("Dialog", "Action"))
        self.label_3.setText(_translate("Dialog", "Initiative Cost"))
