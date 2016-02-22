# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'join_battle_gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 150)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox1 = QtWidgets.QGroupBox(Dialog)
        self.groupBox1.setTitle("")
        self.groupBox1.setObjectName("groupBox1")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox1 = QtWidgets.QSpinBox(self.groupBox1)
        self.spinBox1.setMinimum(-99)
        self.spinBox1.setObjectName("spinBox1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox1)
        self.verticalLayout_2.addWidget(self.groupBox1)
        self.groupBox2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox2.setTitle("")
        self.groupBox2.setObjectName("groupBox2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox2)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBox2 = QtWidgets.QSpinBox(self.groupBox2)
        self.spinBox2.setMinimum(-99)
        self.spinBox2.setObjectName("spinBox2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox2)
        self.verticalLayout_2.addWidget(self.groupBox2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
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
        Dialog.setWindowTitle(_translate("Dialog", "Join Battle!"))
        self.label.setText(_translate("Dialog", "Join Battle!"))
        self.label_3.setText(_translate("Dialog", "Join Battle!"))
