# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_bookm_main.ui'
#
# Created: Sun Jul  3 01:36:46 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Search(object):
    def setupUi(self, Dialog_Search):
        Dialog_Search.setObjectName("Dialog_Search")
        Dialog_Search.resize(1029, 637)
        Dialog_Search.setStyleSheet("background-image: url(:/new/prefix1/resources/background6.jpg);")
        self.groupBox = QtWidgets.QGroupBox(Dialog_Search)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1001, 131))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 60, 691, 36))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Search = QtWidgets.QLabel(self.layoutWidget)
        self.label_Search.setStyleSheet("font: 75 italic 12pt \"Sans\";\n"
"color: rgb(112, 27, 27);")
        self.label_Search.setObjectName("label_Search")
        self.horizontalLayout.addWidget(self.label_Search)
        self.lineEdit_searchField = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_searchField.setObjectName("lineEdit_searchField")
        self.horizontalLayout.addWidget(self.lineEdit_searchField)
        self.pushButton_search = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_search.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search.setIcon(icon)
        self.pushButton_search.setFlat(True)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout.addWidget(self.pushButton_search)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 941, 35))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_icon = QtWidgets.QLabel(self.layoutWidget1)
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap(":/new/prefix1/resources/check_fine.png"))
        self.label_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout_2.addWidget(self.label_icon)
        self.label_branch_id = QtWidgets.QLabel(self.layoutWidget1)
        self.label_branch_id.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label_branch_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_branch_id.setObjectName("label_branch_id")
        self.horizontalLayout_2.addWidget(self.label_branch_id)
        self.comboBox_branch_id = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_branch_id.setObjectName("comboBox_branch_id")
        self.horizontalLayout_2.addWidget(self.comboBox_branch_id)
        self.label_branch_name = QtWidgets.QLabel(self.layoutWidget1)
        self.label_branch_name.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label_branch_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_branch_name.setObjectName("label_branch_name")
        self.horizontalLayout_2.addWidget(self.label_branch_name)
        self.comboBox_branch_name = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_branch_name.setObjectName("comboBox_branch_name")
        self.horizontalLayout_2.addWidget(self.comboBox_branch_name)
        self.label_branch_address = QtWidgets.QLabel(self.layoutWidget1)
        self.label_branch_address.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label_branch_address.setAlignment(QtCore.Qt.AlignCenter)
        self.label_branch_address.setObjectName("label_branch_address")
        self.horizontalLayout_2.addWidget(self.label_branch_address)
        self.comboBox_branch_address = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_branch_address.setObjectName("comboBox_branch_address")
        self.horizontalLayout_2.addWidget(self.comboBox_branch_address)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 90, 571, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.suggestion_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.suggestion_layout.setContentsMargins(0, 0, 0, 0)
        self.suggestion_layout.setObjectName("suggestion_layout")
        self.pushButton_switch = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_switch.setGeometry(QtCore.QRect(960, 100, 31, 27))
        self.pushButton_switch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_switch.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_switch.setAutoFillBackground(False)
        self.pushButton_switch.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_switch.setIcon(icon1)
        self.pushButton_switch.setAutoRepeat(False)
        self.pushButton_switch.setFlat(True)
        self.pushButton_switch.setObjectName("pushButton_switch")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog_Search)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 150, 981, 471))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 981, 441))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget_mainList = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidget_mainList.setMouseTracking(True)
        self.tableWidget_mainList.setObjectName("tableWidget_mainList")
        self.tableWidget_mainList.setColumnCount(0)
        self.tableWidget_mainList.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidget_mainList)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 541, 421))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 40, 541, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_card_no = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_card_no.setObjectName("lineEdit_card_no")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_card_no)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_ssn = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_ssn.setObjectName("lineEdit_ssn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ssn)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_Fname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_Fname.setObjectName("lineEdit_Fname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Fname)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_Lname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_Lname.setObjectName("lineEdit_Lname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Lname)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_Address = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_Address.setObjectName("lineEdit_Address")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Address)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_Phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_Phone.setObjectName("lineEdit_Phone")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Phone)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_7.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label_7.setObjectName("label_7")
        self.pushButton_check_borrower = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_check_borrower.setGeometry(QtCore.QRect(90, 10, 31, 27))
        self.pushButton_check_borrower.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_check_borrower.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_check_borrower.setAutoFillBackground(False)
        self.pushButton_check_borrower.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_check_borrower.setIcon(icon2)
        self.pushButton_check_borrower.setFlat(True)
        self.pushButton_check_borrower.setObjectName("pushButton_check_borrower")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_1.setGeometry(QtCore.QRect(0, 240, 541, 181))
        self.tableWidget_1.setMouseTracking(True)
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(0)
        self.tableWidget_1.setRowCount(0)
        self.label_changable = QtWidgets.QLabel(self.page_2)
        self.label_changable.setGeometry(QtCore.QRect(570, 60, 191, 17))
        self.label_changable.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.label_changable.setObjectName("label_changable")
        self.splitter = QtWidgets.QSplitter(self.page_2)
        self.splitter.setGeometry(QtCore.QRect(650, 300, 241, 34))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_checkLoan = QtWidgets.QPushButton(self.splitter)
        self.pushButton_checkLoan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_checkLoan.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_checkLoan.setAutoFillBackground(False)
        self.pushButton_checkLoan.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.pushButton_checkLoan.setIcon(icon2)
        self.pushButton_checkLoan.setFlat(True)
        self.pushButton_checkLoan.setObjectName("pushButton_checkLoan")
        self.pushButton_checkFine = QtWidgets.QPushButton(self.splitter)
        self.pushButton_checkFine.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_checkFine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_checkFine.setAutoFillBackground(False)
        self.pushButton_checkFine.setStyleSheet("font: 75 12pt \"Bitstream Charter\";")
        self.pushButton_checkFine.setIcon(icon2)
        self.pushButton_checkFine.setFlat(True)
        self.pushButton_checkFine.setObjectName("pushButton_checkFine")
        self.splitter_2 = QtWidgets.QSplitter(self.page_2)
        self.splitter_2.setGeometry(QtCore.QRect(750, 340, 51, 81))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton_checkout = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_checkout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_checkout.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_checkout.setAutoFillBackground(False)
        self.pushButton_checkout.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/Check_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_checkout.setIcon(icon3)
        self.pushButton_checkout.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_checkout.setFlat(True)
        self.pushButton_checkout.setObjectName("pushButton_checkout")
        self.pushButton_checkin = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_checkin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_checkin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_checkin.setAutoFillBackground(False)
        self.pushButton_checkin.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/new/prefix1/resources/Check_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_checkin.setIcon(icon4)
        self.pushButton_checkin.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_checkin.setFlat(True)
        self.pushButton_checkin.setObjectName("pushButton_checkin")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(570, 90, 411, 192))
        self.tableWidget_2.setMouseTracking(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Dialog_Search)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Search)

    def retranslateUi(self, Dialog_Search):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Search.setWindowTitle(_translate("Dialog_Search", "Dialog"))
        self.label_Search.setText(_translate("Dialog_Search", "Search"))
        self.label_branch_id.setText(_translate("Dialog_Search", "Branch id"))
        self.label_branch_name.setText(_translate("Dialog_Search", "Branch Name"))
        self.label_branch_address.setText(_translate("Dialog_Search", "Branch Address"))
        self.label.setText(_translate("Dialog_Search", "Card No"))
        self.label_2.setText(_translate("Dialog_Search", "SSN"))
        self.label_3.setText(_translate("Dialog_Search", "Fname"))
        self.label_4.setText(_translate("Dialog_Search", "Lname"))
        self.label_5.setText(_translate("Dialog_Search", "Address"))
        self.label_6.setText(_translate("Dialog_Search", "Phone"))
        self.label_7.setText(_translate("Dialog_Search", "Borrower"))
        self.label_changable.setText(_translate("Dialog_Search", "Book Selected"))
        self.pushButton_checkLoan.setText(_translate("Dialog_Search", "Check Loans"))
        self.pushButton_checkFine.setText(_translate("Dialog_Search", "Check Fine"))

import GUI.rs_rc
