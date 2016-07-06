from borr_manage_ved import *
from GUI.dialog_checkfine import *
from GUI.dialog_borrview_modify import *
from PyQt5.QtWidgets import QDialog,QHeaderView,QTableWidgetItem
from PyQt5.QtGui import QIcon
from loan_fine import *
from PyQt5.QtWidgets import QHeaderView

class checkfine_callbacks(borr_manage_mod):
    def __init__(self,sql=None):
        super(checkfine_callbacks,self).__init__(sql)
        self.pay_Pressed = 0


    def open_dialog_checkfine(self):
        self.dialog_fine = QDialog()
        self.open_checkfine_dialog = Ui_Dialog_checkfine()
        self.open_checkfine_dialog.setupUi(self.dialog_fine)
        self.dialog_fine.show()
        self.Fine_amt = [0]

        self.open_checkfine_dialog.pushButton_select_borr.clicked.connect(self.open_select_dialog)
        self.open_checkfine_dialog.lineEdit_fine.textChanged.connect(lambda: self.getContent(self.open_checkfine_dialog.lineEdit_fine,self.Fine_amt))
        self.open_checkfine_dialog.lineEdit_fine.returnPressed.connect(lambda: self.getContent(self.open_checkfine_dialog.lineEdit_fine,self.Fine_amt))
        self.open_checkfine_dialog.lineEdit_fine.editingFinished.connect(lambda: self.getContent(self.open_checkfine_dialog.lineEdit_fine,self.Fine_amt))
        self.open_checkfine_dialog.pushButton_pay.clicked.connect(self.payFine)

    def payFine(self):
        print(self.backup_loan_id)
        cmd_1 = (
            'UPDATE fines '
            'SET Fine_amt=%s '
            'WHERE loan_id=%s;'
        )
        cmd_2 = (
            'UPDATE fines '
            'SET Fine_amt=0,Paid=1 '
            'WHERE loan_id=%s'
        )
        print(self.fineselectionList[0]['Fine_amt'])
        print(self.Fine_amt)
        if float(self.Fine_amt[0]) == float(self.fineselectionList[0]['Fine_amt'][0]):
            self.sql.executeCmd(cmd_2,(self.backup_loan_id,))
            self.sql.submite()
            QMessageBox.information(None,'Information','Full amount of fine has been paid')
        else:
            remained_fine = float(self.fineselectionList[0]['Fine_amt'][0])-float(self.Fine_amt[0])
            self.sql.executeCmd(cmd_1,(str(remained_fine),self.backup_loan_id))
            self.sql.submite()
            QMessageBox.information(None,'Information','Partial amount of fine has been paid')


    def getContent(self,target,container):
        container[0] = target.text()
        container[0] = container[0].lstrip(' ').rstrip(' ')

    def open_select_dialog(self):
        print('entered')
        self.view_pressed=0
        self.dialog_select = QDialog()
        self.open_select_dialog = Ui_Dialog_borrmain()
        self.open_select_dialog.setupUi(self.dialog_select)
        self.open_select_dialog.pushButton_edit.hide()
        self.open_select_dialog.pushButton_delete.hide()
        self.dialog_select.show()
        self.open_select_dialog.pushButton_setting.clicked.connect(lambda: self.open_createBorr(True))
        self.open_select_dialog.pushButton_view.clicked.connect(lambda: self.showContent(self.open_select_dialog.tableWidget_view))
        self.open_select_dialog.buttonBox.accepted.connect(self.printFine)

    def printFine(self):
        selectionDict = {}

        #print(self.genSelectionList[0])
        loan_rec = findLoan(self.sql,None,self.genSelectionList[0]['Card_no'][0],fullRecord=True)
        print('loan_rec',loan_rec)
        if not loan_rec:
            QMessageBox.information(None,'information','No loan and fine record are found for this user')
        else:
            loan_idList = [row[0] for row in loan_rec]
            fine_rec = findFine(self.sql,loan_idList,True)
            print(fine_rec)
            if not fine_rec:
                QMessageBox.information(None,'Information','No fine record is found')
            else:
                headerList = [
                    "Loan_id",
                    "Fine_amt",
                    "Paid"
                ]

                self.open_checkfine_dialog.tableWidget_fine.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.open_checkfine_dialog.tableWidget_fine.setSelectionBehavior(1)
                self.open_checkfine_dialog.tableWidget_fine.setSelectionMode(1)
                self.open_checkfine_dialog.tableWidget_fine.clearContents()
                self.open_checkfine_dialog.tableWidget_fine.setColumnCount(len(headerList))
                self.open_checkfine_dialog.tableWidget_fine.setRowCount(len(fine_rec))
                if self.pay_Pressed > 0:
                    self.open_checkfine_dialog.tableWidget_fine.cellClicked.disconnect()
                i = 0
                for head in headerList:
                    self.open_checkfine_dialog.tableWidget_fine.setHorizontalHeaderItem(i,QTableWidgetItem(QIcon('GUI/resources/sort-up.png'),head))
                    i+=1
                for row in range(len(fine_rec)):
                    tmp = fine_rec[row]
                    for idx in range(len(tmp)):
                        if idx<2:
                            self.open_checkfine_dialog.tableWidget_fine.setItem(row,idx,QTableWidgetItem(str(tmp[idx])))
                        else:
                            if tmp[idx] == 0:
                                self.open_checkfine_dialog.tableWidget_fine.setItem(row,idx,QTableWidgetItem(QIcon('GUI/resources/hourglass.png'),'Waiting'))
                            else:
                                self.open_checkfine_dialog.tableWidget_fine.setItem(row,idx,QTableWidgetItem(QIcon('GUI/resources/paid.png'),'Paid'))
                selectionDict.clear()
                selectionDict['row_number']=[]
                selectionDict['row']=[]
                selectionDict['table']=self.open_checkfine_dialog.tableWidget_fine
                selectionDict['headerList'] = headerList
                for item in headerList:
                    selectionDict[item] = []
                self.fineselectionList = [selectionDict]
                self.open_checkfine_dialog.tableWidget_fine.cellClicked.connect(self.setFineCheckState)

    def setFineCheckState(self,row,column):
        self.fineselectionList[0]['row_number'].clear()
        self.fineselectionList[0]['row_number'].append(row)
        rowContent = []
        for idx in range(len(self.fineselectionList[0]['headerList'])):
            widget = self.fineselectionList[0]['table'].item(row,idx)
            rowContent.append(widget.text())
            self.fineselectionList[0][self.fineselectionList[0]['headerList'][idx]].clear()
            self.fineselectionList[0][self.fineselectionList[0]['headerList'][idx]].append(widget.text())
        self.fineselectionList[0]['row'].clear()
        self.fineselectionList[0]['row'].append(rowContent)
        self.backup_loan_id = self.fineselectionList[0]['Loan_id'][0]
        print(self.fineselectionList[0])
