# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Primefactorx01\Documents\Python\ex-3e-init-tracker\lib\decisive_gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 276)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.attacker_combo = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attacker_combo.sizePolicy().hasHeightForWidth())
        self.attacker_combo.setSizePolicy(sizePolicy)
        self.attacker_combo.setObjectName("attacker_combo")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.attacker_combo)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.a_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.a_spinBox.setMinimum(-99)
        self.a_spinBox.setObjectName("a_spinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.a_spinBox)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.defender_combobox = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defender_combobox.sizePolicy().hasHeightForWidth())
        self.defender_combobox.setSizePolicy(sizePolicy)
        self.defender_combobox.setObjectName("defender_combobox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.defender_combobox)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.d_spinbox = QtWidgets.QSpinBox(self.groupBox_2)
        self.d_spinbox.setMinimum(-99)
        self.d_spinbox.setObjectName("d_spinbox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.d_spinbox)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.onslaught_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.onslaught_lbl.setObjectName("onslaught_lbl")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.onslaught_lbl)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.gambit_combo = QtWidgets.QComboBox(Dialog)
        self.gambit_combo.setObjectName("gambit_combo")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.gambit_combo)
        self.init_cost_label = QtWidgets.QLabel(Dialog)
        self.init_cost_label.setObjectName("init_cost_label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.init_cost_label)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setObjectName("spinBox")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.success_radio = QtWidgets.QRadioButton(self.groupBox_4)
        self.success_radio.setObjectName("success_radio")
        self.verticalLayout_3.addWidget(self.success_radio)
        self.fail_radio = QtWidgets.QRadioButton(self.groupBox_4)
        self.fail_radio.setObjectName("fail_radio")
        self.verticalLayout_3.addWidget(self.fail_radio)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Attacker"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Initiative Modifier"))
        self.groupBox_2.setTitle(_translate("Dialog", "Defender"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.label_4.setText(_translate("Dialog", "Initiative Modifier"))
        self.label_7.setText(_translate("Dialog", "Onslaught Penalty"))
        self.onslaught_lbl.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "Gambit"))
        self.init_cost_label.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "Rout Check"))
        self.success_radio.setText(_translate("Dialog", "Successful"))
        self.fail_radio.setText(_translate("Dialog", "Failed"))

