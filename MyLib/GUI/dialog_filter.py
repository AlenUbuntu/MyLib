# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_filter.ui'
#
# Created: Fri Jun 17 15:22:49 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_filter(object):
    def setupUi(self, Dialog_filter):
        Dialog_filter.setObjectName("Dialog_filter")
        Dialog_filter.resize(860, 357)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_filter)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 861, 431))
        self.groupBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.groupBox_2.setStyleSheet("background-image: url(:/new/prefix1/resources/background4.jpg);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(10, 64, 491, 261))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textView_filter_detail = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textView_filter_detail.setGeometry(QtCore.QRect(0, 0, 491, 261))
        self.textView_filter_detail.setStyleSheet("font: 75 10pt \"Bitstream Charter\";")
        self.textView_filter_detail.setObjectName("textView_filter_detail")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.filter_detail_label = QtWidgets.QLabel(self.groupBox_2)
        self.filter_detail_label.setGeometry(QtCore.QRect(220, 20, 48, 20))
        self.filter_detail_label.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.filter_detail_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filter_detail_label.setObjectName("filter_detail_label")
        self.pushButton_check = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_check.setGeometry(QtCore.QRect(760, 120, 85, 27))
        self.pushButton_check.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_check.setStyleSheet("font: 75 10pt \"Bitstream Charter\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/tag-search-filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_check.setIcon(icon)
        self.pushButton_check.setFlat(True)
        self.pushButton_check.setObjectName("pushButton_check")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.buttonBox.setGeometry(QtCore.QRect(510, 310, 341, 32))
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton_repEnter = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_repEnter.setGeometry(QtCore.QRect(790, 280, 51, 20))
        self.pushButton_repEnter.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_repEnter.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/enter-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_repEnter.setIcon(icon1)
        self.pushButton_repEnter.setFlat(True)
        self.pushButton_repEnter.setObjectName("pushButton_repEnter")
        self.splitter_5 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_5.setGeometry(QtCore.QRect(550, 40, 291, 71))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.filter_col_label = QtWidgets.QLabel(self.splitter_2)
        self.filter_col_label.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.filter_col_label.setObjectName("filter_col_label")
        self.comboBox_filter_column = QtWidgets.QComboBox(self.splitter_2)
        self.comboBox_filter_column.setStyleSheet("font: 75 10pt \"Bitstream Charter\";")
        self.comboBox_filter_column.setObjectName("comboBox_filter_column")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.filter_format_label = QtWidgets.QLabel(self.splitter_3)
        self.filter_format_label.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.filter_format_label.setObjectName("filter_format_label")
        self.lineEdit_filter_format = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_filter_format.setStyleSheet("font: 75 10pt \"Bitstream Charter\";")
        self.lineEdit_filter_format.setObjectName("lineEdit_filter_format")
        self.splitter_9 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_9.setGeometry(QtCore.QRect(550, 160, 301, 111))
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.filter_column2_label = QtWidgets.QLabel(self.splitter_6)
        self.filter_column2_label.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.filter_column2_label.setObjectName("filter_column2_label")
        self.comboBox_repSelect = QtWidgets.QComboBox(self.splitter_6)
        self.comboBox_repSelect.setObjectName("comboBox_repSelect")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.filter_noise_label = QtWidgets.QLabel(self.splitter_7)
        self.filter_noise_label.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.filter_noise_label.setObjectName("filter_noise_label")
        self.lineEdit_filter_noise = QtWidgets.QLineEdit(self.splitter_7)
        self.lineEdit_filter_noise.setObjectName("lineEdit_filter_noise")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.filter_replace_label = QtWidgets.QLabel(self.splitter_8)
        self.filter_replace_label.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.filter_replace_label.setObjectName("filter_replace_label")
        self.lineEdit_filter_replace = QtWidgets.QLineEdit(self.splitter_8)
        self.lineEdit_filter_replace.setObjectName("lineEdit_filter_replace")

        self.retranslateUi(Dialog_filter)
        self.buttonBox.accepted.connect(Dialog_filter.accept)
        self.buttonBox.rejected.connect(Dialog_filter.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_filter)

    def retranslateUi(self, Dialog_filter):
        _translate = QtCore.QCoreApplication.translate
        Dialog_filter.setWindowTitle(_translate("Dialog_filter", "Dialog"))
        self.filter_detail_label.setText(_translate("Dialog_filter", "Details"))
        self.pushButton_check.setText(_translate("Dialog_filter", "Check"))
        self.filter_col_label.setText(_translate("Dialog_filter", "Column"))
        self.filter_format_label.setText(_translate("Dialog_filter", "Format"))
        self.filter_column2_label.setText(_translate("Dialog_filter", "Column"))
        self.filter_noise_label.setText(_translate("Dialog_filter", "Noise Char"))
        self.filter_replace_label.setText(_translate("Dialog_filter", "Replace With"))

import GUI.rs_rc