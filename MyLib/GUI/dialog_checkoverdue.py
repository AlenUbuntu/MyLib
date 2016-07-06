# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_checkoverdue.ui'
#
# Created: Tue Jul  5 13:30:44 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_checkOverdue(object):
    def setupUi(self, Dialog_checkOverdue):
        Dialog_checkOverdue.setObjectName("Dialog_checkOverdue")
        Dialog_checkOverdue.resize(880, 552)
        Dialog_checkOverdue.setStyleSheet("background-image: url(:/new/prefix1/resources/background6.jpg);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_checkOverdue)
        self.buttonBox.setGeometry(QtCore.QRect(690, 500, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog_checkOverdue)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 861, 481))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_view = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_view.setGeometry(QtCore.QRect(0, 60, 861, 411))
        self.tableWidget_view.setObjectName("tableWidget_view")
        self.tableWidget_view.setColumnCount(0)
        self.tableWidget_view.setRowCount(0)
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(740, 16, 101, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_borr = QtWidgets.QPushButton(self.splitter)
        self.pushButton_borr.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_borr.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/user_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_borr.setIcon(icon)
        self.pushButton_borr.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_borr.setFlat(True)
        self.pushButton_borr.setObjectName("pushButton_borr")
        self.pushButton_view = QtWidgets.QPushButton(self.splitter)
        self.pushButton_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_view.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view.setIcon(icon1)
        self.pushButton_view.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_view.setFlat(True)
        self.pushButton_view.setObjectName("pushButton_view")

        self.retranslateUi(Dialog_checkOverdue)
        self.buttonBox.accepted.connect(Dialog_checkOverdue.accept)
        self.buttonBox.rejected.connect(Dialog_checkOverdue.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_checkOverdue)

    def retranslateUi(self, Dialog_checkOverdue):
        _translate = QtCore.QCoreApplication.translate
        Dialog_checkOverdue.setWindowTitle(_translate("Dialog_checkOverdue", "Dialog"))

import GUI.rs_rc
