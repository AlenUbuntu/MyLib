# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_borrview_modify.ui'
#
# Created: Tue Jul  5 15:07:56 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_borrmain(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(912, 596)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-image: url(:/new/prefix1/resources/background6.jpg);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(560, 550, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 871, 531))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_view = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_view.setGeometry(QtCore.QRect(10, 70, 861, 461))
        self.tableWidget_view.setObjectName("tableWidget_view")
        self.tableWidget_view.setColumnCount(0)
        self.tableWidget_view.setRowCount(0)
        self.pushButton_delete = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_delete.setGeometry(QtCore.QRect(10, 30, 51, 27))
        self.pushButton_delete.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_delete.setAutoFillBackground(False)
        self.pushButton_delete.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon)
        self.pushButton_delete.setFlat(True)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(700, 30, 161, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_edit = QtWidgets.QPushButton(self.splitter)
        self.pushButton_edit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_edit.setAutoFillBackground(False)
        self.pushButton_edit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_edit.setIcon(icon1)
        self.pushButton_edit.setFlat(True)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.pushButton_setting = QtWidgets.QPushButton(self.splitter)
        self.pushButton_setting.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_setting.setAutoFillBackground(False)
        self.pushButton_setting.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/user_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_setting.setIcon(icon2)
        self.pushButton_setting.setFlat(True)
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.pushButton_view = QtWidgets.QPushButton(self.splitter)
        self.pushButton_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_view.setAutoFillBackground(False)
        self.pushButton_view.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view.setIcon(icon3)
        self.pushButton_view.setFlat(True)
        self.pushButton_view.setObjectName("pushButton_view")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

import GUI.rs_rc
