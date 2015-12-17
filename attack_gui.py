# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attack_gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 281, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.attacker_combo = QtWidgets.QComboBox(self.frame)
        self.attacker_combo.setObjectName("attacker_combo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.attacker_combo)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.a_trick = QtWidgets.QLineEdit(self.frame)
        self.a_trick.setObjectName("a_trick")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.a_trick)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.defender_combobox = QtWidgets.QComboBox(self.frame)
        self.defender_combobox.setObjectName("defender_combobox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.defender_combobox)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.d_trick = QtWidgets.QLineEdit(self.frame)
        self.d_trick.setObjectName("d_trick")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.d_trick)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Attacker"))
        self.label_2.setText(_translate("Dialog", "Initiative Modifier"))
        self.label_3.setText(_translate("Dialog", "Defender"))
        self.label_4.setText(_translate("Dialog", "Initiative Modifier"))
