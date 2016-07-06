from GUI.dialog_borrview_modify import *
from GUI.dialog_checkfine import *
from GUI.dialog_checkoverdue import *
from PyQt5.QtWidgets import QDialog,QHeaderView,QTableWidgetItem
from PyQt5.QtGui import QIcon
from loan_fine import *
from sqlCommand import *
from borr_manage_ved import *
from PyQt5.QtWidgets import QHeaderView


class checkOverdue_callbacks(borr_manage_mod):
    def __init__(self,sql=None):
        super(checkOverdue_callbacks,self).__init__(sql)
        self.view_pressed = 0
        self.genSelectionList = []

    def open_dialog_checkOverdue(self):
        #self.view_overdue_pressed = 0
        self.dialog_checkOverdue = QDialog()
        self.open_checkOverdue_dialog = Ui_Dialog_checkOverdue()
        self.open_checkOverdue_dialog.setupUi(self.dialog_checkOverdue)
        self.dialog_checkOverdue.show()

        self.open_checkOverdue_dialog.pushButton_borr.clicked.connect(self.open_select_dialog)
        self.open_checkOverdue_dialog.pushButton_view.clicked.connect(self.printOverdue)

    def open_select_dialog(self):
        print('entered')
        self.view_pressed = 0
        self.dialog_select = QDialog()
        self.open_select_dialog = Ui_Dialog_borrmain()
        self.open_select_dialog.setupUi(self.dialog_select)
        self.open_select_dialog.pushButton_edit.hide()
        self.open_select_dialog.pushButton_delete.hide()
        self.dialog_select.show()
        self.open_select_dialog.pushButton_setting.clicked.connect(lambda: self.open_createBorr(True))
        self.open_select_dialog.pushButton_view.clicked.connect(lambda: self.showContent(self.open_select_dialog.tableWidget_view))
        self.open_select_dialog.buttonBox.accepted.connect(self.printOverdue)

    def printOverdue(self):
        print(self.genSelectionList)

        if not self.genSelectionList or not self.genSelectionList[0]['Card_no']:
            overdue_rec = self.findOverDue()
        else:
            overdue_rec = findOverDue(self.sql,None,self.genSelectionList[0]['Card_no'][0])
        if not overdue_rec:
            QMessageBox.information(None,'Information','No overdue record is found')
        else:
            headerList = [
                'Loan_id',
                'Card_no',
                'Isbn',
                'Title',
                'Book_authors',
                'Date_out',
                'Due_date'
            ]

            loan_idList = [row[0] for row in overdue_rec]
            query = (
                "SELECT bl.loan_id,bl.Card_no,b.Isbn,b.Title,b.Book_authors,bl.Date_out,bl.Due_date "
                "FROM book AS b, book_copies AS bc, book_loans AS bl "
                "WHERE bl.Book_id=bc.Book_id AND bc.Isbn=b.Isbn "
                "AND bl.loan_id=%s;"
            )
            self.open_checkOverdue_dialog.tableWidget_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.open_checkOverdue_dialog.tableWidget_view.setSelectionMode(1)
            self.open_checkOverdue_dialog.tableWidget_view.setSelectionBehavior(1)
            self.open_checkOverdue_dialog.tableWidget_view.clearContents()
            self.open_checkOverdue_dialog.tableWidget_view.setColumnCount(len(headerList))
            self.open_checkOverdue_dialog.tableWidget_view.setRowCount(len(overdue_rec))

            i=0
            for head in headerList:
                self.open_checkOverdue_dialog.tableWidget_view.setHorizontalHeaderItem(i,QTableWidgetItem(QIcon('GUI/resources/sort-up.png'),head))
                i+=1
            rowContent = []
            for loanId in loan_idList:
                res = self.sql.query(query,(loanId,))
                rowContent += res
            for row in range(len(rowContent)):
                tmp = rowContent[row]
                for idx in range(len(tmp)):
                    self.open_checkOverdue_dialog.tableWidget_view.setItem(row,idx,QTableWidgetItem(str(tmp[idx])))
            #self.view_overdue_pressed += 1




    def findOverDue(self):
        query = (
            "SELECT * FROM book_loans "
            "WHERE NOW()>Due_date AND Date_in IS NULL;"
        )
        return self.sql.query(query,None)
