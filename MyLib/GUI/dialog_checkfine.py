# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_checkfine.ui'
#
# Created: Mon Jul  4 23:42:59 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_checkfine(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 557)
        Dialog.setStyleSheet("background-image: url(:/new/prefix1/resources/background6.jpg);")
        Dialog.setModal(False)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 671, 541))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_fine = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_fine.setGeometry(QtCore.QRect(10, 80, 611, 411))
        self.tableWidget_fine.setObjectName("tableWidget_fine")
        self.tableWidget_fine.setColumnCount(0)
        self.tableWidget_fine.setRowCount(0)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(310, 510, 341, 32))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(390, 30, 241, 34))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_select_borr = QtWidgets.QPushButton(self.splitter)
        self.pushButton_select_borr.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_select_borr.setAutoFillBackground(False)
        self.pushButton_select_borr.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/check_fine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_select_borr.setIcon(icon)
        self.pushButton_select_borr.setFlat(True)
        self.pushButton_select_borr.setObjectName("pushButton_select_borr")
        self.lineEdit_fine = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_fine.setObjectName("lineEdit_fine")
        self.pushButton_pay = QtWidgets.QPushButton(self.splitter)
        self.pushButton_pay.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_pay.setAutoFillBackground(False)
        self.pushButton_pay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/give-money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_pay.setIcon(icon1)
        self.pushButton_pay.setFlat(True)
        self.pushButton_pay.setObjectName("pushButton_pay")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

import GUI.rs_rc
