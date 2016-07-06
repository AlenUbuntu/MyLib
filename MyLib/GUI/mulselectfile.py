# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mulselectfile.ui'
#
# Created: Sat Jun 18 14:21:32 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QFileDialog

class Ui_Form_mulSelectFile(object):
    def setupUi(self, Form_mulSelectFile,resultSet,target):
        Form_mulSelectFile.setObjectName("Form_mulSelectFile")
        Form_mulSelectFile.resize(404, 44)
        self.splitter = QtWidgets.QSplitter(Form_mulSelectFile)
        self.splitter.setGeometry(QtCore.QRect(11, 11, 391, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.textBrowser_file = QtWidgets.QTextBrowser(self.splitter)
        self.textBrowser_file.setObjectName("textBrowser_file")
        self.pushButton_select = QtWidgets.QPushButton(self.splitter)
        self.pushButton_select.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_select.setIcon(icon)
        self.pushButton_select.setObjectName("pushButton_select")
        self.pushButton_add = QtWidgets.QPushButton(self.splitter)
        self.pushButton_add.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon1)
        self.pushButton_add.setObjectName("pushButton_add")

        self.retranslateUi(Form_mulSelectFile)
        QtCore.QMetaObject.connectSlotsByName(Form_mulSelectFile)

        self.pushButton_select.clicked.connect(lambda: self.selectFile(resultSet))
        self.pushButton_add.clicked.connect(lambda: self.addSelf(resultSet,target))

    def retranslateUi(self, Form_mulSelectFile):
        _translate = QtCore.QCoreApplication.translate
        Form_mulSelectFile.setWindowTitle(_translate("Form_mulSelectFile", "Form"))
    
    def selectFile(self,resultSet):
        qurl = QFileDialog.getOpenFileUrl()
        if qurl:
            url = qurl[0].url()[7:]
            if url not in resultSet:
                resultSet.append(url)
            self.textBrowser_file.setText(url)
            print(resultSet)
    def addSelf(self,resultSet,target):
        new = QWidget()
        Ui_Form_mulSelectFile().setupUi(new,resultSet,target)
        target.addWidget(new)

import GUI.rs_rc
