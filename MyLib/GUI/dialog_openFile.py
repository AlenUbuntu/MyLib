# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_openFile.ui'
#
# Created: Thu Jun 16 16:51:10 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_openFile(object):
    def setupUi(self, Dialog_openFile):
        Dialog_openFile.setObjectName("Dialog_openFile")
        Dialog_openFile.resize(535, 220)
        self.groupBox = QtWidgets.QGroupBox(Dialog_openFile)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 861, 231))
        self.groupBox.setStyleSheet("background-image: url(:/new/prefix1/resources/background4.jpg);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(180, 180, 341, 32))
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_2.setGeometry(QtCore.QRect(10, 90, 301, 61))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.filter_delimiter_label = QtWidgets.QLabel(self.splitter_2)
        self.filter_delimiter_label.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.filter_delimiter_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filter_delimiter_label.setObjectName("filter_delimiter_label")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lineEdit_filter_delimiter = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_filter_delimiter.setObjectName("lineEdit_filter_delimiter")
        self.pushButton_filter_delSubmit = QtWidgets.QPushButton(self.splitter)
        self.pushButton_filter_delSubmit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_filter_delSubmit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_filter_delSubmit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/enter-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_filter_delSubmit.setIcon(icon)
        self.pushButton_filter_delSubmit.setFlat(True)
        self.pushButton_filter_delSubmit.setObjectName("pushButton_filter_delSubmit")
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_4.setGeometry(QtCore.QRect(10, 10, 441, 61))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.filter_path_label = QtWidgets.QLabel(self.splitter_4)
        self.filter_path_label.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.filter_path_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filter_path_label.setObjectName("filter_path_label")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.textView_filter_showFile = QtWidgets.QTextBrowser(self.splitter_3)
        self.textView_filter_showFile.setObjectName("textView_filter_showFile")
        self.pushButton_filter_select = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_filter_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_filter_select.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_filter_select.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_filter_select.setIcon(icon1)
        self.pushButton_filter_select.setFlat(True)
        self.pushButton_filter_select.setObjectName("pushButton_filter_select")

        self.retranslateUi(Dialog_openFile)
        self.buttonBox.accepted.connect(Dialog_openFile.accept)
        self.buttonBox.rejected.connect(Dialog_openFile.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_openFile)

    def retranslateUi(self, Dialog_openFile):
        _translate = QtCore.QCoreApplication.translate
        Dialog_openFile.setWindowTitle(_translate("Dialog_openFile", "Dialog"))
        self.filter_delimiter_label.setText(_translate("Dialog_openFile", "Delimiter"))
        self.filter_path_label.setText(_translate("Dialog_openFile", "File Path"))

import GUI.rs_rc
