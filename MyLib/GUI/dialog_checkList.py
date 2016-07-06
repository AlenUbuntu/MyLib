# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_checkList.ui'
#
# Created: Fri Jun 17 21:51:47 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(555, 493)
        #Dialog.setStyleSheet("background-image: url(:/new/prefix1/resources/background4.jpg);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 450, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 401, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.checkList_VL = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.checkList_VL.setContentsMargins(0, 0, 0, 0)
        self.checkList_VL.setObjectName("checkList_VL")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

