# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_filelist.ui'
#
# Created: Sat Jun 18 16:23:04 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_fileList(object):
    def setupUi(self, Dialog_fileList):
        Dialog_fileList.setObjectName("Dialog_fileList")
        Dialog_fileList.resize(827, 578)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_fileList)
        self.buttonBox.setGeometry(QtCore.QRect(470, 530, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog_fileList)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 20, 631, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_file = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_file.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_file.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_file.setObjectName("verticalLayout_file")

        self.retranslateUi(Dialog_fileList)
        self.buttonBox.accepted.connect(Dialog_fileList.accept)
        self.buttonBox.rejected.connect(Dialog_fileList.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_fileList)

    def retranslateUi(self, Dialog_fileList):
        _translate = QtCore.QCoreApplication.translate
        Dialog_fileList.setWindowTitle(_translate("Dialog_fileList", "Dialog"))

