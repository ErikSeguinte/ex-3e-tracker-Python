# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Modification_Window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(381, 264)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.name_edit = QtWidgets.QLineEdit(Dialog)
        self.name_edit.setObjectName("name_edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_edit)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Initiative_box = QtWidgets.QSpinBox(Dialog)
        self.Initiative_box.setMinimum(-99)
        self.Initiative_box.setObjectName("Initiative_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Initiative_box)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.crash_counter_box = QtWidgets.QSpinBox(Dialog)
        self.crash_counter_box.setObjectName("crash_counter_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.crash_counter_box)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.crash_return_box = QtWidgets.QSpinBox(Dialog)
        self.crash_return_box.setObjectName("crash_return_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.crash_return_box)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.join_battle_box = QtWidgets.QSpinBox(Dialog)
        self.join_battle_box.setObjectName("join_battle_box")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.join_battle_box)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.onslaught_spinbox = QtWidgets.QSpinBox(Dialog)
        self.onslaught_spinbox.setMinimum(-99)
        self.onslaught_spinbox.setMaximum(0)
        self.onslaught_spinbox.setObjectName("onslaught_spinbox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.onslaught_spinbox)
        self.horizontalLayout.addLayout(self.formLayout)
        self.CheckBoxes = QtWidgets.QVBoxLayout()
        self.CheckBoxes.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.CheckBoxes.setObjectName("CheckBoxes")
        self.player_checkBox = QtWidgets.QCheckBox(Dialog)
        self.player_checkBox.setObjectName("player_checkBox")
        self.CheckBoxes.addWidget(self.player_checkBox)
        self.inertcheckBox = QtWidgets.QCheckBox(Dialog)
        self.inertcheckBox.setObjectName("inertcheckBox")
        self.CheckBoxes.addWidget(self.inertcheckBox)
        self.legendary_size_checkBox = QtWidgets.QCheckBox(Dialog)
        self.legendary_size_checkBox.setObjectName("legendary_size_checkBox")
        self.CheckBoxes.addWidget(self.legendary_size_checkBox)
        self.crashed_check = QtWidgets.QCheckBox(Dialog)
        self.crashed_check.setObjectName("crashed_check")
        self.CheckBoxes.addWidget(self.crashed_check)
        self.crashed_recentlycheck = QtWidgets.QCheckBox(Dialog)
        self.crashed_recentlycheck.setObjectName("crashed_recentlycheck")
        self.CheckBoxes.addWidget(self.crashed_recentlycheck)
        self.has_gone_check = QtWidgets.QCheckBox(Dialog)
        self.has_gone_check.setObjectName("has_gone_check")
        self.CheckBoxes.addWidget(self.has_gone_check)
        self.delayed_checkBox = QtWidgets.QCheckBox(Dialog)
        self.delayed_checkBox.setObjectName("delayed_checkBox")
        self.CheckBoxes.addWidget(self.delayed_checkBox)
        self.horizontalLayout.addLayout(self.CheckBoxes)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_8.setText(_translate("Dialog", "Shift Target"))
        self.label_2.setText(_translate("Dialog", "Initiative"))
        self.label_4.setText(_translate("Dialog", "Crash Counter"))
        self.label_5.setText(_translate("Dialog", "Crash Return"))
        self.label_7.setText(_translate("Dialog", "Join Battle Pool"))
        self.label_3.setText(_translate("Dialog", "Onslaught"))
        self.player_checkBox.setText(_translate("Dialog", "Player"))
        self.inertcheckBox.setText(_translate("Dialog", "Inert Initiative"))
        self.legendary_size_checkBox.setText(_translate("Dialog", "Legendary Size"))
        self.crashed_check.setText(_translate("Dialog", "Crashed"))
        self.crashed_recentlycheck.setText(_translate("Dialog", "Crashed Recently"))
        self.has_gone_check.setText(_translate("Dialog", "Has Gone"))
        self.delayed_checkBox.setText(_translate("Dialog", "Delayed"))

