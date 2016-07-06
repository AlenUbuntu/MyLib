from borr_manage_add import *
from PyQt5.QtWidgets import QDialog,QHeaderView,QTableWidgetItem
from PyQt5.QtGui import QIcon
from loan_fine import *

from GUI.dialog_borrview_modify import *

class borr_manage_mod(borrMagCallback):
    def __init__(self,sql=None):
        super(borr_manage_mod,self).__init__(sql)
        self.view_pressed = 0

    def open_mod_dialog(self,flag):
        print('entered',flag)
        self.dialog_mod = QDialog()
        self.open_mod_dialog = Ui_Dialog_borrmain()
        self.open_mod_dialog.setupUi(self.dialog_mod)
        self.internal_open_dialog(flag)
        print('exit')

    def internal_open_dialog(self,flag):
        if flag == 0:
            self.open_mod_dialog.pushButton_edit.hide()
            self.open_mod_dialog.pushButton_delete.hide()
        if flag == 1:
            self.open_mod_dialog.pushButton_delete.hide()
        if flag == 2:
            self.open_mod_dialog.pushButton_edit.hide()
        self.dialog_mod.show()

        self.open_mod_dialog.pushButton_setting.clicked.connect(lambda: self.open_createBorr(True))
        self.open_mod_dialog.pushButton_view.clicked.connect(lambda: self.showContent(self.open_mod_dialog.tableWidget_view))
        if flag == 1:
            self.open_mod_dialog.pushButton_edit.clicked.connect(self.editBorr)
        if flag == 2:
            self.open_mod_dialog.pushButton_delete.clicked.connect(self.deleteBorr)

    def deleteBorr(self):
        if not self.genSelectionList[0]['row']:
            QMessageBox.critical(None,'Error','No borrower is selected for deletion!')
            return
        self.func_delete_borr()

    def func_delete_borr(self):
        overdue_rec = findOverDue(self.sql,None,self.genSelectionList[0]['Card_no'][0])
        query = (
            "SELECT loan_id "
            "FROM book_loans "
            "WHERE Card_no=%s;"
        )
        cmd=(
            "DELETE FROM borrower "
            "WHERE Card_no=%s"
        )
        loan_idList = self.sql.query(query,(self.genSelectionList[0]['Card_no'][0],))
        if loan_idList:
            loan_idList = [item[0] for item in loan_idList]
            fine_rec = findFine(self.sql,loan_idList)
        else:
            fine_rec = []
        if fine_rec or overdue_rec:
            QMessageBox.critical(None,'Error','Cannot delete this borrower either because of an overdue loan or an unpaid fine!')
            return
        else:
            self.sql.executeCmd(cmd,(self.genSelectionList[0]['Card_no'][0],))
            self.sql.submite()
            QMessageBox.information(None,'Information','Operation Completes')







    def editBorr(self):
        if not self.genSelectionList[0]['row']:
            QMessageBox.critical(None,'Error','No borrower is selected for modification!')
            return
        print('backup:',self.backup_card_no)
        self.open_createBorr(True)
        self.create_dialog.buttonBox.accepted.connect(lambda:self.func_modify_borr(self.backup_card_no))

    def func_modify_borr(self,backup_card_no):
            cmd = [
                "UPDATE borrower",
                "SET ",
                "WHERE Card_no=%s;"
            ]

            #self.printall()
            i = 0
            param = []
            if (not self.card_no[0]) and (not self.ssn[0]) and (not self.fname[0]) and (not self.lname[0]) and (not self.street_address[0]) and (not self.city[0]) and (not self.state[0]) and (not self.phone[0]):
                return
            else:

                if self.card_no[0]:
                    cmd[1] += 'Card_no=%s'
                    param.append(self.card_no[0])
                    i += 1
                if self.ssn[0]:
                    if i == 0:
                        statement = 'Ssn=%s'
                    else:
                        statement = ',Ssn=%s'
                    cmd[1] += statement
                    param.append(self.ssn[0])
                    i += 1
                if self.fname[0]:
                    if i == 0:
                        statement = 'Fname=%s'
                    else:
                        statement = ',Fname=%s'
                    cmd[1] += statement
                    param.append(self.fname[0])
                    i += 1
                if self.lname[0]:
                    if i == 0:
                        statement = 'Lname=%s'
                    else:
                        statement = ',Lname=%s'
                    cmd[1] += statement
                    param.append(self.lname[0])
                    i += 1
                if self.street_address[0]:
                    if i == 0:
                        statement = 'Street_Address=%s'
                    else:
                        statement = ',Street_Address=%s'
                    cmd[1] += statement
                    param.append(self.street_address[0])
                    i += 1
                if self.email[0]:
                    if i == 0:
                        statement = 'email=%s'
                    else:
                        statement = ',email=%s'
                    cmd[1] += statement
                    param.append(self.email[0])
                    i += 1
                if self.city[0]:
                    if i == 0:
                        statement = 'City=%s'
                    else:
                        statement = ',City=%s'
                    cmd[1] += statement
                    param.append(self.city[0])
                    i += 1
                if self.state[0]:
                    if i == 0:
                        statement = 'State=%s'
                    else:
                        statement = ',State=%s'
                    cmd[1] += statement
                    param.append(self.state[0])
                    i += 1
                if self.phone[0]:
                    if i == 0:
                        statement = 'Phone=%s'
                    else:
                        statement = ',Phone=%s'
                    cmd[1] += statement
                    param.append(self.phone[0])
                    i += 1
                cmd = ' '.join(cmd)
                cmd += ';'
                param.append(backup_card_no)
                print(cmd,param)
                self.sql.executeCmd(cmd,tuple(param))
                self.sql.submite()
                QMessageBox.information(None,'Information','Operation Completes')

    def showContent(self,target):

        headerList = [
            'Card_no',
            'Ssn',
            'Fname',
            'Lname',
            'email',
            'Street Address',
            'City',
            'State',
            'Phone'
        ]

        query = (
            "SELECT * FROM borrower "
        )

        #self.printall()
        i = 0
        param = []
        if (not self.card_no[0]) and (not self.ssn[0]) and (not self.fname[0]) and (not self.lname[0]) and (not self.street_address[0]) and (not self.city[0]) and (not self.state[0]) and (not self.phone[0]):
                query += ';'
                res = self.sql.query(query,None)
        else:
            query += 'WHERE '

            if self.card_no[0]:
                query += 'Card_no=%s '
                param.append(self.card_no[0])
                i += 1
            if self.ssn[0]:
                if i == 0:
                    statement = 'Ssn=%s '
                else:
                    statement = 'AND Ssn=%s '
                query += statement
                param.append(self.ssn[0])
                i += 1
            if self.fname[0]:
                if i == 0:
                    statement = 'Fname=%s '
                else:
                    statement = 'AND Fname=%s '
                query += statement
                param.append(self.fname[0])
                i += 1
            if self.lname[0]:
                if i == 0:
                    statement = 'Lname=%s '
                else:
                    statement = 'AND Lname=%s '
                query += statement
                param.append(self.lname[0])
                i += 1
            if self.street_address[0]:
                if i == 0:
                    statement = 'Street_Address=%s '
                else:
                    statement = 'AND Street_Address=%s '
                query += statement
                param.append(self.street_address[0])
                i += 1
            if self.email[0]:
                if i == 0:
                    statement = 'email=%s '
                else:
                    statement = 'AND email=%s '
                query += statement
                param.append(self.email[0])
                i += 1
            if self.city[0]:
                if i == 0:
                    statement = 'City=%s '
                else:
                    statement = 'AND City=%s '
                query += statement
                param.append(self.city[0])
                i += 1
            if self.state[0]:
                if i == 0:
                    statement = 'State=%s '
                else:
                    statement = 'AND State=%s '
                query += statement
                param.append(self.state[0])
                i += 1
            if self.phone[0]:
                if i == 0:
                    statement = 'Phone=%s '
                else:
                    statement = 'AND Phone=%s '
                query += statement
                param.append(self.phone[0])
                i += 1
            query += ';'
        res = self.sql.query(query,param)
        target.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        target.setColumnCount(len(headerList))
        selectionDict = {}
        self.fillContent(headerList,res,target,selectionDict)

    def fillContent(self,headerList,content,target,selectionDict):
            target.clearContents()
            if self.view_pressed >0:
                target.cellClicked.disconnect()
            i = 0
            for head in headerList:
                target.setHorizontalHeaderItem(i,QTableWidgetItem(QIcon('GUI/resources/sort-up.png'),head))
                i+=1
            defaultRowNum = len(content)
            target.setRowCount(defaultRowNum)
            for row in range(len(content)):
                tmp = content[row]
                for idx in range(len(tmp)):
                    target.setItem(row,idx,QTableWidgetItem(tmp[idx]))
            target.setSelectionBehavior(1)
            target.setSelectionMode(1)
            selectionDict.clear()
            selectionDict['row_number']=[]
            selectionDict['row']=[]
            selectionDict['table']=target
            selectionDict['headerList'] = headerList
            for item in headerList:
                selectionDict[item] = []

            self.genSelectionList = [selectionDict]
            target.cellClicked.connect(self.setCheckState)
            self.view_pressed += 1

    def setCheckState(self,row,column):

        self.genSelectionList[0]['row_number'].clear()
        self.genSelectionList[0]['row_number'].append(row)
        rowContent = []
        for idx in range(len(self.genSelectionList[0]['headerList'])):
            widget = self.genSelectionList[0]['table'].item(row,idx)
            rowContent.append(widget.text())
            self.genSelectionList[0][self.genSelectionList[0]['headerList'][idx]].clear()
            self.genSelectionList[0][self.genSelectionList[0]['headerList'][idx]].append(widget.text())
        self.genSelectionList[0]['row'].clear()
        self.genSelectionList[0]['row'].append(rowContent)

        self.backup_card_no = self.genSelectionList[0]['Card_no'][0]

        print(self.backup_card_no,'\n')
