from sqlCommand import *
from PyQt5.QtWidgets import QDialog
from GUI.dialog_addborrower import *
from GUI.dialog_borrview_modify import *
import re

class borrMagCallback:
    def __init__(self,sql=None):
        if sql:
            self.sql=sql
        else:
            self.sql=sqlCommand()
        self.card_no = [None]
        self.ssn = [None]
        self.fname = [None]
        self.lname = [None]
        self.lname = [None]
        self.email = [None]
        self.street_address = [None]
        self.city = [None]
        self.state = [None]
        self.phone = [None]

    def getContent(self,target,container):
        container[0] = target.text()
        container[0] = container[0].lstrip(' ').rstrip(' ')
        #self.printall()

    def open_createBorr(self,flag=False):
        self.dialog = QDialog()
        self.create_dialog = Ui_Dialog()
        self.create_dialog.setupUi(self.dialog)
        self.dialog.show()

        self.card_no = [None]
        self.ssn = [None]
        self.fname = [None]
        self.lname = [None]
        self.lname = [None]
        self.email = [None]
        self.street_address = [None]
        self.city = [None]
        self.state = [None]
        self.phone = [None]

        self.create_dialog.lineEdit_card_no.textChanged.connect(lambda: self.getContent(self.create_dialog.lineEdit_card_no,self.card_no))
        self.create_dialog.lineEdit_card_no.returnPressed.connect(lambda: self.getContent(self.create_dialog.lineEdit_card_no,self.card_no))
        self.create_dialog.lineEdit_card_no.editingFinished.connect(lambda: self.getContent(self.create_dialog.lineEdit_card_no,self.card_no))

        self.create_dialog.lineEdit_ssn.textChanged.connect(lambda: self.getContent(self.create_dialog.lineEdit_ssn,self.ssn))
        self.create_dialog.lineEdit_ssn.returnPressed.connect(lambda: self.getContent(self.create_dialog.lineEdit_ssn,self.ssn))
        self.create_dialog.lineEdit_ssn.editingFinished.connect(lambda: self.getContent(self.create_dialog.lineEdit_ssn,self.ssn))

        self.create_dialog.lineEdit_fname.textChanged.connect(lambda: self.getContent(self.create_dialog.lineEdit_fname,self.fname))
        self.create_dialog.lineEdit_fname.returnPressed.connect(lambda: self.getContent(self.create_dialog.lineEdit_fname,self.fname))
        self.create_dialog.lineEdit_fname.editingFinished.connect(lambda: self.getContent(self.create_dialog.lineEdit_fname,self.fname))

        self.create_dialog.lineEdit_lname.textChanged.connect(lambda: self.getContent(self.create_dialog.lineEdit_lname,self.lname))
        self.create_dialog.lineEdit_lname.returnPressed.connect(lambda: self.getContent(self.create_dialog.lineEdit_lname,self.lname))
        self.create_dialog.lineEdit_lname.editingFinished.connect(lambda: self.getContent(self.create_dialog.lineEdit_lname,self.lname))

        self.create_dialog.lineEdit_email.textChanged.connect(lambda: self.getContent(self.create_dialog.lineEdit_email,self.email))
        self.create_dialog.lineEdit_email.returnPressed.connect(lambda: self.getContent(self.create_dialog.lineEdit_email,self.email))
        self.create_dialog.lineEdit_email.editingFinished.connect(lambda: self.getContent(self.create_dialog.lineEdit_email,self.email))

        self.create_dialog.lineEdit_saddress.textChanged.connect(lambda: self.getContent(self.create_dialog.lineEdit_saddress,self.street_address))
        self.create_dialog.lineEdit_saddress.returnPressed.connect(lambda: self.getContent(self.create_dialog.lineEdit_saddress,self.street_address))
        self.create_dialog.lineEdit_saddress.editingFinished.connect(lambda: self.getContent(self.create_dialog.lineEdit_saddress,self.street_address))

        self.create_dialog.lineEdit_City.textChanged.connect(lambda: self.getContent(self.create_dialog.lineEdit_City,self.city))
        self.create_dialog.lineEdit_City.returnPressed.connect(lambda: self.getContent(self.create_dialog.lineEdit_City,self.city))
        self.create_dialog.lineEdit_City.editingFinished.connect(lambda: self.getContent(self.create_dialog.lineEdit_City,self.city))

        self.create_dialog.lineEdit_State.textChanged.connect(lambda: self.getContent(self.create_dialog.lineEdit_State,self.state))
        self.create_dialog.lineEdit_State.returnPressed.connect(lambda: self.getContent(self.create_dialog.lineEdit_State,self.state))
        self.create_dialog.lineEdit_State.editingFinished.connect(lambda: self.getContent(self.create_dialog.lineEdit_State,self.state))

        self.create_dialog.lineEdit_Phone.textChanged.connect(lambda: self.getContent(self.create_dialog.lineEdit_Phone,self.phone))
        self.create_dialog.lineEdit_Phone.returnPressed.connect(lambda: self.getContent(self.create_dialog.lineEdit_Phone,self.phone))
        self.create_dialog.lineEdit_Phone.editingFinished.connect(lambda: self.getContent(self.create_dialog.lineEdit_Phone,self.phone))

        if not flag:
            self.create_dialog.buttonBox.accepted.connect(self.start_borrCreation)


    def start_borrCreation(self):
        print('enter')
        if not self.ssn[0]:
            QMessageBox.critical(None,'Error','SSN cannot be empty!')
            return
        if not self.street_address[0] or (not self.city[0]) or (not self.state[0]):
            QMessageBox.critical(None,'Error','Address cannot be empty!')
            return
        if not self.fname[0] or (not self.lname[0]):
            QMessageBox.critical(None,'Error','Name cannot be empty!')
            return

        maxid_query = (
            "SELECT MAX(`Card_no`) "
            "FROM borrower;"
        )
        duplicate_query = (
            "SELECT * FROM borrower "
            "WHERE Ssn=%s;"
        )
        add_borrower=(
            "INSERT INTO borrower "
            "VALUES ("
            "%s,%s,%s,%s,%s,%s,%s,%s,%s"
            ");"
        )

        max_id = self.sql.query(maxid_query,None)[0][0]
        duplicate = self.sql.query(duplicate_query,(self.ssn[0],))
        if duplicate:
            QMessageBox.critical(None,'Error','Ssn entered already exists!')
            return
        pattern = re.compile('[0-9]+')
        id_num = pattern.search(max_id).group(0)
        width = len(id_num)

        if self.card_no[0] and self.card_no[0] > id_num:
            new_id = self.card_no[0]
        else:
            new_id ='ID'+ str(int(id_num)+1).zfill(width)
        param = []
        param.append(new_id)
        param.append(self.ssn[0])
        param.append(self.fname[0])
        param.append(self.lname[0])
        if self.email[0]:
            param.append(self.email[0])
        else:
            param.append(None)
        param.append(self.street_address[0])
        param.append(self.city[0])
        param.append(self.state[0])
        if self.phone[0]:
            param.append(self.phone[0])
        else:
            param.append(None)

        self.sql.executeCmd(add_borrower,tuple(param))
        self.sql.submite()


    def printall(self):
        print('card_no:',self.card_no)
        print('city:',self.city)
        print('email:',self.email)
        print('fname:',self.fname)
        print('lname:',self.lname)
        print('ssn:',self.ssn)
        print('street_address:',self.street_address)
        print('state:',self.state)
        print('phone:',self.phone)
