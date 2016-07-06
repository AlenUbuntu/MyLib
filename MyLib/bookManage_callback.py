from GUI.dialog_bookM_import import Ui_Dialog_import
from PyQt5.QtWidgets import QDialog,QMessageBox,QInputDialog,QTextBrowser,QTableWidget,QTableWidgetItem,QHeaderView
from PyQt5.QtWidgets import QFileDialog,QWidget
from PyQt5.QtGui import QIcon
from GUI.dialog_openFile import *
from GUI.dialog_filter import *
from dialog_dyna_checkList import dyna_checkList_Dialog
from GUI.dialog_filelist import Ui_Dialog_fileList
from GUI.dialog_bookm_main import Ui_Dialog_Search
import functools
from GUI.mulselectfile import *
import databaseImport
import os,csv
from dataParser import *
from further_filter import *
from callback import callbacks
from sqlCommand import *
from loan_fine import *
import copy,datetime

class bookm_call(callbacks):

    def __init__(self,bookloan_allowed_duration=14,feeRate=0.25,sql=None):
        super(bookm_call,self).__init__()
        self.noisyresult=[None,None]
        self.showSelect=[None]
        self.collection = [
            '\\',
            '/',
            '&amp;',
            ';',
            '#',
            '(',
            ')',
            '%',
            '-',
            '+',
            '=',
            ':',
            '<',
            '>',
            '?',
            '$',
            '|',
            '~',
            '?',
            ','
        ]
        if sql:
            self.sql=sql
        else:
            flag=[1]
            self.sql = sqlCommand(flag)
            if flag[0] == 0:
                return
        self.backup_param = [bookloan_allowed_duration,feeRate,sql]
        self.bookloan_allowed_duration = bookloan_allowed_duration
        self.selection = [self.collection]
        self.selectedBorrDict={}
        self.checkBorrowerPressed = False
        self.reSelectionDict = {}
        self.selectedIsbns = []
        self.selectedLoanDict = {}
        self.selectedFineDict = {}
        self.selectedRows = []
        self.fine_record = []
        self.loan_record = []
        self.feeRate = feeRate
        self.idIndex = [0]
        self.nameIndex = [0]
        self.addressIndex = [0]
        self.searchContent = [0]
        self.flag = [0]
        self.nextIndex = [1]
        self.card_no = [None]
        self.ssn = [None]
        self.fname = [None]
        self.lname = [None]
        self.address = [None]
        self.phone = [None]
        self.keywords = []
        self.PB_seaPressedNum = 0
        self.checkLoanPressed = False



    def button_openFurFilterDialog(self,targets = None):

        self.dialogFurFilter = QDialog()
        self.open_dialogFurFilter = Ui_Dialog_import()
        self.open_dialogFurFilter.setupUi(self.dialogFurFilter)
        self.dialogFurFilter.show()

        self.open_dialogFurFilter.comboBox_bookM_type.addItems(self.collection)

        self.open_dialogFurFilter.pushButton_bookM_select.clicked.connect(lambda: self.button_openFileDialog(
            self.open_dialogFurFilter.textView_bookM_detail,
            self.open_dialogFurFilter.textview_bookM_file
        ))

        self.open_dialogFurFilter.pushButton_bookM_delSubmit.clicked.connect(lambda:self.readFiles(
            None,
            self.open_dialogFurFilter.textView_bookM_detail,
            self.open_dialogFurFilter.comboBox_bookM_column,
            self.open_dialogFurFilter.comboBox_repSelect
        ))

        self.filterIndex = [0]
        self.repIndex = [0]
        self.showSelect = [0]


        self.open_dialogFurFilter.comboBox_bookM_type.currentIndexChanged.connect(lambda :self.comboBox_getCurrentItem(
            self.open_dialogFurFilter.comboBox_bookM_type,
            self.showSelect
        ))

        self.open_dialogFurFilter.comboBox_bookM_column.currentIndexChanged.connect(lambda: self.comboBox_getCurrentItem(
            self.open_dialogFurFilter.comboBox_bookM_column,
            self.filterIndex
        ))

        self.open_dialogFurFilter.comboBox_repSelect.currentIndexChanged.connect(lambda :self.comboBox_getCurrentItem(
            self.open_dialogFurFilter.comboBox_repSelect,
            self.repIndex
        ))

        self.open_dialogFurFilter.lineEdit_bookM_noise.textChanged.connect(lambda: self.getNoise(self.open_dialogFurFilter.lineEdit_bookM_noise))
        self.open_dialogFurFilter.lineEdit_bookM_noise.returnPressed.connect(lambda: self.getNoise(self.open_dialogFurFilter.lineEdit_bookM_noise))
        self.open_dialogFurFilter.lineEdit_bookM_noise.editingFinished.connect(lambda: self.getNoise(self.open_dialogFurFilter.lineEdit_bookM_noise))
        self.open_dialogFurFilter.lineEdit_bookM_noise.editingFinished.connect(lambda: self.setviewText(
            target=self.open_dialogFurFilter.textView_bookM_detail,
            text='noise:\t'+ self.noise))

        self.open_dialogFurFilter.lineEdit_bookM_replace.textChanged.connect(lambda: self.getRep(self.open_dialogFurFilter.lineEdit_bookM_replace))
        self.open_dialogFurFilter.lineEdit_bookM_replace.returnPressed.connect(lambda: self.getRep(self.open_dialogFurFilter.lineEdit_bookM_replace))
        self.open_dialogFurFilter.lineEdit_bookM_replace.editingFinished.connect(lambda: self.getRep(self.open_dialogFurFilter.lineEdit_bookM_replace))
        self.open_dialogFurFilter.lineEdit_bookM_replace.editingFinished.connect(lambda: self.setviewText(
            target=self.open_dialogFurFilter.textView_bookM_detail,
            text='replaced with:\t'+ self.rep))

        self.open_dialogFurFilter.pushButton_check.clicked.connect(lambda: FFilter(self.url,self.delim).checkNoise(
            self.dicts[self.header[self.filterIndex[0]]],
            self.selection[0],
            self.noisyresult,
            self.open_dialogFurFilter.textView_bookM_detail,
            self.collection[self.showSelect[0]],
            self.open_dialogFurFilter.comboBox_bookM_type
        ))

        self.open_dialogFurFilter.pushButton_repEnter.clicked.connect(lambda: FFilter(self.url,self.delim).noiseCorrect(
            self.noise,
            self.rep,
            self.noisyresult[0][self.collection[self.showSelect[0]]],
            self.dicts[self.header[self.repIndex[0]]],
            self.open_dialogFurFilter.textView_bookM_detail
        ))

        self.open_dialogFurFilter.pushButton_selectSym.clicked.connect(self.onCheckSelected)

        self.open_dialogFurFilter.pushButton_view.clicked.connect(lambda: FFilter(self.url,self.delim).showNoise(
            self.checkNull(self.selection[0])[self.showSelect[0]],
            self.open_dialogFurFilter.textView_bookM_detail,
            self.noisyresult[1]
        ))

        self.open_dialogFurFilter.pushButton_write.clicked.connect(lambda: self.choice(None))

    def onCheckSelected(self):
        self.checkListDialog = QDialog()
        self.open_dialogDynaCheckList = dyna_checkList_Dialog(self.checkListDialog)
        self.widgetList = self.open_dialogDynaCheckList.createCheckBoxs(self.collection)
        self.open_dialogDynaCheckList.addWidgets(self.widgetList)
        self.checkListDialog.show()
        self.selection[0]=[]

        for widget in self.widgetList:
            widget.stateChanged.connect(functools.partial(self.checkboxclicked,widget,self.selection[0]))

    def checkboxclicked(self,widget,target):
        if widget.isChecked():
            target.append(widget.text())
        else:
            target.remove(widget.text())

        #print(self.selection)

    def checkNull(self,choice):
        if choice != []:
            return choice
        else:
            self.selection[0] = self.collection
            return self.selection[0]

    def choice(self,target=None):
        saveM = QMessageBox.question(target,"Want to write file?","click Save to save filtered file!", QMessageBox.Save|QMessageBox.No)
        if saveM == 0x00000800:
            self.writeFiles(target)
        self.importDialog = QDialog()
        self.open_dialogFurFilter.importDBDialog = Ui_Dialog_fileList()
        self.open_dialogFurFilter.importDBDialog.setupUi(self.importDialog)
        self.importFileList = [[]]

        widget = QWidget()
        mulSelectFile = Ui_Form_mulSelectFile()
        mulSelectFile.setupUi(widget,self.importFileList[0],self.open_dialogFurFilter.importDBDialog.verticalLayout_file)
        self.open_dialogFurFilter.importDBDialog.verticalLayout_file.addWidget(widget)

        widget = QWidget()
        mulSelectFile = Ui_Form_mulSelectFile()
        mulSelectFile.setupUi(widget,self.importFileList[0],self.open_dialogFurFilter.importDBDialog.verticalLayout_file)
        self.open_dialogFurFilter.importDBDialog.verticalLayout_file.addWidget(widget)

        widget = QWidget()
        mulSelectFile = Ui_Form_mulSelectFile()
        mulSelectFile.setupUi(widget,self.importFileList[0],self.open_dialogFurFilter.importDBDialog.verticalLayout_file)
        self.open_dialogFurFilter.importDBDialog.verticalLayout_file.addWidget(widget)

        self.importDialog.show()

        self.importDialog.accepted.connect(self.startImport)

    def startImport(self):
        username = QInputDialog.getText(None,"Database User Name","Please Enter User Name")
        passwd = QInputDialog.getText(None,"Database User Password","Please Enter User Password")
        host = QInputDialog.getText(None,"Database Host Address","Please Enter IP address:")
        #print(username,passwd,host)
        if username[1] and passwd[1] and host[1]:
            databaseImport.start(self.importFileList[0],username[0],passwd[0],host[0])
        else:
            QMessageBox.critical(None,"Failed!","Missing information to log into the database")

class bookm_functional_call(bookm_call):
    def __init__(self,bookloan_allowed_duration=14,feeRate=0.25,sql=None):
        print(sql)
        super(bookm_functional_call,self).__init__(bookloan_allowed_duration,feeRate,sql)

    def button_openSearch(self,searchFlag=False,flag=None):
        self.dialogSearch = QDialog()
        self.open_dialogSearch = Ui_Dialog_Search()
        self.open_dialogSearch.setupUi(self.dialogSearch)
        self.dialogSearch.show()

        if flag == 1:
            self.checkIn_searchFlag = True
        else:
            self.checkIn_searchFlag = False

        query = (
            "SELECT * FROM `library_branch`"
        )

        self.suggestion = self.buildSuggestion(self.open_dialogSearch.lineEdit_searchField)
        self.open_dialogSearch.suggestion_layout.addWidget(self.suggestion)
        result = self.sql.query(query)
        branch_id = []
        branch_name = []
        branch_address = []
        for res in result:
            branch_id.append(str(res[0]))
            branch_name.append(str(res[1]))
            branch_address.append(str(res[2])+', '+str(res[3]))
        self.open_dialogSearch.comboBox_branch_id.addItems(branch_id)
        self.open_dialogSearch.comboBox_branch_name.addItems(branch_name)
        self.open_dialogSearch.comboBox_branch_address.addItems(branch_address)
        target = [
            self.open_dialogSearch.comboBox_branch_id,
            self.open_dialogSearch.comboBox_branch_name,
            self.open_dialogSearch.comboBox_branch_address
        ]

        self.idIndex = [0]
        self.nameIndex = [0]
        self.addressIndex = [0]
        self.searchContent = [0]
        self.flag = [0]
        self.nextIndex = [1]

        self.open_dialogSearch.comboBox_branch_id.currentIndexChanged.connect(lambda: self.comboBox_getCurrentItem(
            self.open_dialogSearch.comboBox_branch_id,
            self.idIndex
        ))
        self.open_dialogSearch.comboBox_branch_name.currentIndexChanged.connect(lambda: self.comboBox_getCurrentItem(
            self.open_dialogSearch.comboBox_branch_name,
            self.nameIndex
        ))
        self.open_dialogSearch.comboBox_branch_address.currentIndexChanged.connect(lambda: self.comboBox_getCurrentItem(
            self.open_dialogSearch.comboBox_branch_address,
            self.addressIndex
        ))
        self.open_dialogSearch.comboBox_branch_id.currentIndexChanged.connect(lambda:self.synchronizeIndex(self.idIndex[0],target))
        self.open_dialogSearch.comboBox_branch_name.currentIndexChanged.connect(lambda:self.synchronizeIndex(self.nameIndex[0],target))
        self.open_dialogSearch.comboBox_branch_address.currentIndexChanged.connect(lambda:self.synchronizeIndex(self.addressIndex[0],target))


        self.open_dialogSearch.lineEdit_searchField.textChanged.connect(lambda: self.getContent(self.open_dialogSearch.lineEdit_searchField,self.searchContent))
        self.open_dialogSearch.lineEdit_searchField.textChanged.connect(lambda: self.showSuggestion(self.suggestion))
        self.open_dialogSearch.lineEdit_searchField.returnPressed.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_searchField,self.searchContent))
        self.open_dialogSearch.lineEdit_searchField.editingFinished.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_searchField,self.searchContent))
        self.open_dialogSearch.lineEdit_searchField.editingFinished.connect(lambda: self.hideSuggestion(self.suggestion))
        self.open_dialogSearch.lineEdit_searchField.textChanged.connect(lambda:self.setviewText(self.sugg_list,self.suggestion))
        self.open_dialogSearch.lineEdit_searchField.returnPressed.connect(lambda: self.multifieldParser(self.searchContent,self.flag[0]))
        self.open_dialogSearch.pushButton_search.clicked.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_searchField,self.searchContent))
        self.open_dialogSearch.pushButton_search.clicked.connect(self.onSearchClicked)
        self.open_dialogSearch.pushButton_search.clicked.connect(lambda: self.hideSuggestion(self.suggestion))
        if not searchFlag:
            if flag == 0:
                self.open_dialogSearch.pushButton_checkin.hide()
            if flag == 1:
                self.open_dialogSearch.pushButton_checkout.hide()
            self.open_dialogSearch.pushButton_switch.clicked.connect(lambda: self.switch(self.nextIndex))
        else:
            self.open_dialogSearch.pushButton_switch.hide()

        # start page 2 of stackedWidget
        self.card_no = [None]
        self.ssn = [None]
        self.fname = [None]
        self.lname = [None]
        self.address = [None]
        self.phone = [None]
        self.selectedRows = []
        self.selectedIsbns = []
        self.selectedAuthors = []

        self.open_dialogSearch.lineEdit_card_no.textChanged.connect(lambda: self.getContent(self.open_dialogSearch.lineEdit_card_no,self.card_no))
        self.open_dialogSearch.lineEdit_card_no.returnPressed.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_card_no,self.card_no))
        self.open_dialogSearch.lineEdit_card_no.editingFinished.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_card_no,self.card_no))

        self.open_dialogSearch.lineEdit_ssn.textChanged.connect(lambda: self.getContent(self.open_dialogSearch.lineEdit_ssn,self.ssn))
        self.open_dialogSearch.lineEdit_ssn.returnPressed.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_ssn,self.ssn))
        self.open_dialogSearch.lineEdit_ssn.editingFinished.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_ssn,self.ssn))

        self.open_dialogSearch.lineEdit_Fname.textChanged.connect(lambda: self.getContent(self.open_dialogSearch.lineEdit_Fname,self.fname))
        self.open_dialogSearch.lineEdit_Fname.returnPressed.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_Fname,self.fname))
        self.open_dialogSearch.lineEdit_Fname.editingFinished.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_Fname,self.fname))

        self.open_dialogSearch.lineEdit_Lname.textChanged.connect(lambda: self.getContent(self.open_dialogSearch.lineEdit_Lname,self.lname))
        self.open_dialogSearch.lineEdit_Lname.returnPressed.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_Lname,self.lname))
        self.open_dialogSearch.lineEdit_Lname.editingFinished.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_Lname,self.lname))

        self.open_dialogSearch.lineEdit_Address.textChanged.connect(lambda: self.getContent(self.open_dialogSearch.lineEdit_Address,self.address))
        self.open_dialogSearch.lineEdit_Address.returnPressed.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_Address,self.address))
        self.open_dialogSearch.lineEdit_Address.editingFinished.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_Address,self.address))

        self.open_dialogSearch.lineEdit_Phone.textChanged.connect(lambda: self.getContent(self.open_dialogSearch.lineEdit_Phone,self.phone))
        self.open_dialogSearch.lineEdit_Phone.returnPressed.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_Phone,self.phone))
        self.open_dialogSearch.lineEdit_Phone.editingFinished.connect(lambda:self.getContent(self.open_dialogSearch.lineEdit_Phone,self.phone))

        self.open_dialogSearch.pushButton_check_borrower.clicked.connect(self.onCheckBorrowerClicked)
        self.open_dialogSearch.pushButton_checkLoan.clicked.connect(self.onCheckLoanClicked)

        self.open_dialogSearch.pushButton_checkFine.clicked.connect(self.onCheckFineClicked)

        self.open_dialogSearch.pushButton_checkout.clicked.connect(self.checkOut)
        self.open_dialogSearch.pushButton_checkin.clicked.connect(self.checkIn)



    def synchronizeIndex(self,value,target):
        for each in target:
            each.setCurrentIndex(value)


    def buildSuggestion(self,parent):
        suggestion = QTextBrowser()
        geo = [0,0]
        tmp = parent.geometry()
        geo[0] = tmp.width()
        geo[1] = tmp.height()
        suggestion.setGeometry(0,0,geo[0],geo[1])
        suggestion.hide()
        return suggestion

    def showSuggestion(self,target):
        target.show()
    def hideSuggestion(self,target):
        target.hide()

    def getContent(self,target,container):
        container[0] = target.text()
        container[0] = container[0].lstrip(' ').rstrip(' ')
        self.searchContent_parser(container,self.flag)

    def searchContent_parser(self,container,flag=None):

        # flag indicate the type of the content
        # flag = 0 if content is simply integers
        # flag = 1 if content contains only literal characters (may contain a few additional digits)
        # flag = 2 if content contains both
        #check if content is ISBN
        pattern = re.compile('[0-9]+[a-zA-Z]?')
        mobj = pattern.fullmatch(container[0])
        self.keywords = []

        if mobj:
            flag = 0
            container[0] = [container[0]]
        elif len(container[0]) >= 10:
            pattern = re.compile(r'[0-9]{9}[0-9a-zA-Z]')
            tmpObj = pattern.search(container[0])

            if tmpObj:
                tmp = []
                tmp.append(tmpObj.group(0))
                tmp_2 = container[0].partition(tmp[0])
                tmp.append(tmp_2[0]+tmp_2[2])
                container[0] = tmp
                flag = 2
            else:
                flag = 1
                container[0] = [container[0]]
        else:
            flag = 1
            container[0] = [container[0]]
        self.flag[0]=flag

        if container[0][0] != '':
            query = (
                "SELECT `word` FROM `KeywordList` WHERE `word` LIKE %s LIMIT 3;"
                )
            if flag == 0:
                self.sugg_list = self.sql.query(query,(container[0][0]+'%',))
            elif flag == 2:
                self.sugg_list = []
                self.sugg_list.append(self.sql.query(query,(container[0][0]+'%',)))
                self.sugg_list.append(self.sql.query(query,(container[0][1]+'%',)))
            else:
                self.sugg_list = self.sql.query(query,(container[0][0]+'%',))


    def multifieldParser(self,container,flag):
        query = (
            "SELECT `word` FROM `KeywordList` WHERE `word`=%s;"
        )
        #print(container,flag)
        if container[0][0] != '':
            if flag == 0:
                self.keywords += [container[0][0]]
                return
            if flag == 1 or flag == 2:
                if flag == 1:
                    content = container[0][0]
                else:
                    self.keywords += [container[0][0]]
                    content = container[0][1]

            res = self.sql.query(query,(content,))
            if res:
                self.keywords += [content]
            else:
                i = 1
                maxIteration = 1
                fields = []
                content = content.lstrip(' ')
                while len(content)>0 and maxIteration<40:
                    maxIteration +=1
                    tmp = content.rsplit(' ',maxsplit = i)
                    if ' ' in tmp[0]:
                        tmp_field = ' '.join(tmp[1:])
                    else:
                        if len(tmp)==2:
                            tmp_field = ' '.join(tmp[1:])
                            res = self.sql.query(query,(tmp_field,))
                            if res:
                                pass
                            else:
                                tmp_field = content
                                tmp[0]='' # set tmp[0] to speical value to exit the loop
                        else:
                            fields.append(content)
                            break;
                    res = self.sql.query(query,(tmp_field,))
                    #print('tmp_field=',tmp_field,'content=',content,'res=',res)
                    if not res:
                        i += 1
                        continue
                    else:
                        fields.append(tmp_field)
                        content = tmp[0]
                        i = 1
                if maxIteration == 40:
                    self.keywords.append(content)
                self.keywords += filter(None,fields)
        if not self.keywords:
            self.keywords += container[0]


    def setviewText(self,textSource,target):
        text = ''
        for item in textSource:
            if not isinstance(item,list):
                text += item[0]
                text +='; '
            else:
                break;
        target.clear()
        target.setText(text)

    def onSearchClicked(self):
        #self.keywords=['0195153448', 'Heti', 'Sheila', "D'Este", 'Carlo', '074322678X', 'Classical Mythology']
        #self.keywords=['019515344', '074322678']
        #self.keywords = ['Classical Mythology','Clara Callan: A Novel']
        #self.keywords = ['077107467','Adams', 'David']
        query1 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND b.Isbn LIKE %s ;"
        )
        query2 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND b.Title LIKE %s;"
        )
        query3 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND (a.FName LIKE %s AND a.MName LIKE %s AND a.LName LIKE %s);"
        )
        query4 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND (a.FName LIKE %s AND a.MName IS %s AND a.LName LIKE %s);"
        )
        query5 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND (a.FName LIKE %s AND a.MName IS %s AND a.LName IS %s);"
        )
        query6 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND (a.FName LIKE %s OR a.MName LIKE %s OR a.LName LIKE %s);"
        )
        query7 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND b.Isbn LIKE %s "
            "AND b.Title LIKE %s "
            "AND (a.FName LIKE %s OR a.MName LIKE %s OR a.LName LIKE %s); "
        )
        query8 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND (b.Isbn LIKE %s "
        )
        query9 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND (b.Title LIKE %s "
        )
        query10 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND ((a.FName LIKE %s OR a.MName LIKE %s OR a.LName LIKE %s) "

        )
        query11 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND b.Isbn LIKE %s "
            "AND b.Title LIKE %s;"
        )
        query12 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND b.Isbn LIKE %s "
            "AND ((a.FName LIKE %s OR a.MName LIKE %s OR a.LName LIKE %s) "
        )
        query13 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND b.Title LIKE %s "
            "AND ((a.FName LIKE %s OR a.MName LIKE %s OR a.LName LIKE %s) "
        )
        query14 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND b.Isbn LIKE %s "
            "AND b.Title LIKE %s "
            "AND ((a.FName LIKE %s OR a.MName LIKE %s OR a.LName LIKE %s) "
        )
        query15 = (
            "SELECT DISTINCT b.Isbn,Title,b.Book_authors,No_of_copies "
            "FROM book AS b, book_authors AS ba, authors AS a, library_branch AS lb, book_copies AS bc "
            "WHERE b.Isbn=ba.Isbn "
            "AND ba.Author_id=a.Author_id "
            "AND lb.Branch_id=bc.Branch_id "
            "AND b.Isbn=bc.Isbn "
            "AND lb.Branch_id=%s "
            "AND b.Book_authors LIKE %s;"
        )
        statement1 = "OR b.Isbn LIKE %s "
        statement2 = "OR b.Title LIKE %s "
        statement3 = "OR (a.FName LIKE %s OR a.MName LIKE %s OR a.LName LIKE %s) "
        statement4 = "AND (a.FName LIKE %s OR a.MName LIKE %s OR a.LName LIKE %s) "

        self.multifieldParser(self.searchContent,self.flag[0])
        #print(self.keywords)
        headerList = [
            'ISBN',
            'Book Title',
            'Book Authors',
            'Available'
        ]
        self.open_dialogSearch.tableWidget_mainList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.open_dialogSearch.tableWidget_mainList.setColumnCount(4)
        i=0
        for head in headerList:
            self.open_dialogSearch.tableWidget_mainList.setHorizontalHeaderItem(i,QTableWidgetItem(QIcon('GUI/resources/sort-up.png'),head))
            i+=1

        currId = self.open_dialogSearch.comboBox_branch_id.currentText()
        tmp_recombine_result = []
        # Determine the query we want to use
        #print('keywords before processing:',self.keywords)
        if len(self.keywords) == 1:
            pattern = re.compile('[0-9]+[a-zA-Z]?')
            mobj = pattern.fullmatch(self.keywords[0])

            if mobj:
                res = self.sql.query(query1,(currId,self.keywords[0]+'%'))
                print('Isbn=',res)
            else:
                res = self.sql.query(query2,(currId,self.keywords[0]+'%'))
                print('Title=',res)
                if not res:
                    tmp = self.keywords[0].split(' ')
                    tmp = list(filter(None,tmp))
                    if len(tmp)>2:
                        tmp[2] = ' '.join(tmp[2:])
                        res = self.sql.query(query3,(currId,tmp[0]+'%',tmp[1]+'%',tmp[2]+'%'))
                    if len(tmp) == 1:
                        tmp.append(None)
                        tmp.append(None)
                        res = self.sql.query(query5,(currId,tmp[0]+'%',tmp[1],tmp[2]))
                        if not res:
                            res = self.sql.query(query6,(currId,tmp[0]+'%',tmp[0]+'%',tmp[0]+'%'))

                    elif len(tmp) == 2:
                        tmp.insert(1,None)
                        res = self.sql.query(query4,(currId,tmp[0]+'%',tmp[1],tmp[2]+'%'))
                    print(res)
        else:
            print('original=',self.keywords)
            Isbn_list = []
            Title_list = []
            tmp_3 = copy.deepcopy(self.keywords)
            tmp_3.reverse()
            tmp_keyword = ' '.join(list(filter(None,tmp_3)))
            print('tmp_keyword',tmp_keyword)
            pattern = re.compile('[0-9]+[a-zA-Z]?')

            # test if the input itself is an keywords which is ambiguous with other fields
            param = []
            param.append(currId)
            param.append('%'+tmp_keyword+'%')
            res = self.sql.query(query2,tuple(param))
            if res:
                tmp_recombine_result += res
            param = []
            param.append(currId)
            param.append('%'+tmp_keyword+'%')
            res = self.sql.query(query15,tuple(param))
            if res:
                tmp_recombine_result += res


            for each in self.keywords:
                mobj = pattern.fullmatch(each)
                if mobj:
                    term = mobj.group(0)
                    Isbn_list.append(term)
            print('Isbn_list=',Isbn_list)
            for each in Isbn_list:
                self.keywords.remove(each)

            for each in self.keywords:
                res = self.sql.query(query2,(currId,each+'%'))
                if res:
                    Title_list.append(each)
            print('Title_list=',Title_list)
            for each in Title_list:
                self.keywords.remove(each)

            self.keywords.reverse()
            author_list = self.keywords
            for each in Title_list:
                res = self.sql.query(query6,(currId,each+'%',each+'%',each+'%'))
                if res:
                    author_list.append(each)
            for each in author_list:
                if each in Title_list:
                    Title_list.remove(each)   # We suppose this word is more likely referred to author name
            print('author_list=',author_list)
            print('Title_list=',Title_list)

            if Isbn_list and (not Title_list) and (not author_list):
                query = query8
                for i in range(len(Isbn_list)-1):
                    query += statement1
                query += ");"
                for idx in range(len(Isbn_list)):
                    Isbn_list[idx] = Isbn_list[idx]+'%'
                Isbn_list.insert(0,currId)
                res = self.sql.query(query,tuple(Isbn_list))
                #print('res =',res)

            if Title_list and (not Isbn_list) and (not author_list):
                query = query9
                for i in range(len(Title_list)-1):
                    query += statement2
                query += ");"
                for idx in range(len(Title_list)):
                    Title_list[idx] = Title_list[idx]+'%'
                Title_list.insert(0,currId)
                res = self.sql.query(query,tuple(Title_list))
                #print('res =',res)

            if author_list and (not Isbn_list) and (not Title_list):
                query = query10
                for i in range(len(author_list)-1):
                    query += statement3
                query += ");"
                param = []
                for idx in range(len(author_list)):
                    author_list[idx] = author_list[idx]+'%'
                    param += [author_list[idx]]*3
                param.insert(0,currId)
                res = self.sql.query(query,tuple(param))
                #print('res =',res)

            if Isbn_list and Title_list and (not author_list):
                query = query11
                param = []
                param += [currId]
                param += [Isbn_list[0]+'%']
                param += [Title_list[0]+'%']
                res = self.sql.query(query,tuple(param))
                #print('res =',res)

            if Isbn_list and author_list and (not Title_list):
                query = query12
                param = []
                param += [currId]
                param += [Isbn_list[0]+'%']
                for i in range(len(author_list)):
                    if i>0:
                        query += statement4
                    author_list[i] = author_list[i]+'%'
                    param += [author_list[i]]*3
                query += ");"
                res = self.sql.query(query,tuple(param))
                #print(res)

            if Title_list and author_list and (not Isbn_list):
                query = query13
                param = []
                param += [currId]
                param += [Title_list[0]+'%']
                for i in range(len(author_list)):
                    if i>0:
                        query += statement4
                    author_list[i] = author_list[i]+'%'
                    param += [author_list[i]]*3
                query += ");"
                res = self.sql.query(query,tuple(param))
                #print(res)

            if Isbn_list and Title_list and author_list:
                query = query14
                param = []
                param += [currId]
                param += [Isbn_list[0]+'%']
                param += [Title_list[0]+'%']
                for i in range(len(author_list)):
                    if i>0:
                        query += statement4
                    author_list[i] = author_list[i]+'%'
                    param += [author_list[i]]*3
                query += ");"
                res = self.sql.query(query,tuple(param))
                #print(res)
        self.bookSearch_result = res
        self.open_dialogSearch.tableWidget_2.clearContents()
        self.open_dialogSearch.tableWidget_1.clear()
        self.open_dialogSearch.tableWidget_1.setRowCount(0)
        self.open_dialogSearch.tableWidget_1.setColumnCount(0)
        if self.PB_seaPressedNum > 0:
            self.open_dialogSearch.tableWidget_mainList.cellClicked.disconnect()
        self.setTableContent(self.bookSearch_result+tmp_recombine_result,self.open_dialogSearch.tableWidget_mainList)

    def setTableContent(self,content,table):
        self.PB_seaPressedNum += 1
        table.clearContents()
        currCol = table.columnCount()
        defaultRow = len(content)
        table.setRowCount(defaultRow)
        for row in range(defaultRow):
            tmp = content[row]
            for idx in range(len(tmp)):
                if idx<3:
                    table.setItem(row,idx,QTableWidgetItem(tmp[idx]))
                else:
                    if tmp[idx]>=0:
                        table.setItem(row,currCol-1,QTableWidgetItem(QIcon('GUI/resources/checked.png'),'A'))
                    else:
                        table.setItem(row,currCol-1,QTableWidgetItem(QIcon('GUI/resources/not-available-circle.png'),'NA'))
        table.setSelectionBehavior(1)
        table.setSelectionMode(2)
        self.tmp_selectedRows = []
        self.tmp_selectedIsbns = []
        self.tmp_selectedAuthors = []
        #if self.PB_seaPressedNum > 0:
        #    table.cellClicked.disconnect()
        table.cellClicked.connect(self.setCheckState)

    def setCheckState(self,row,column):
        #self.PB_seaPressedNum += 1
        if row not in self.tmp_selectedRows:
            widget = self.open_dialogSearch.tableWidget_mainList.item(row,3)
            if widget.text() == 'NA' and not self.checkIn_searchFlag:
                    QMessageBox.warning(None,'Warning','This book is not available!')
            else:
                self.tmp_selectedRows.append(row)
                widget = self.open_dialogSearch.tableWidget_mainList.item(row,0)
                self.tmp_selectedIsbns.append(widget.text())
                widget = self.open_dialogSearch.tableWidget_mainList.item(row,2)
                self.selectedAuthors.append(widget.text())
        else:
            self.tmp_selectedRows.remove(row)
            widget = self.open_dialogSearch.tableWidget_mainList.item(row,0)
            self.tmp_selectedIsbns.remove(widget.text())
            widget = self.open_dialogSearch.tableWidget_mainList.item(row,2)
            self.selectedAuthors.remove(widget.text())
        self.selectedRows = list(set(self.selectedRows) | set(self.tmp_selectedRows))
        self.selectedIsbns = list(set(self.selectedIsbns) | set(self.tmp_selectedIsbns))


        print('row=',row,'column=',column,'self.selectedRows',self.selectedRows)

    def switch(self,nextIndex):
        print('Switch:',self.selectedRows)

        self.open_dialogSearch.stackedWidget.setCurrentIndex(nextIndex[0])

        #if nextIndex[0] == 0: self.init()
        print('nextIndex:',nextIndex[0])

        nextIndex[0] = 0 if nextIndex[0]==1 else 1
        if nextIndex[0]==0:
            self.open_dialogSearch.pushButton_switch.hide()

        self.open_dialogSearch.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.open_dialogSearch.tableWidget_2.setColumnCount(2)
        headerList = [
            'ISBN',
            'Book Authors',
        ]
        print(self.selectedRows,self.selectedIsbns,self.selectedAuthors)
        if self.selectedIsbns:
            rowContentList = []
            for i in range(len(self.selectedIsbns)):
                row = []
                row.append(self.selectedIsbns[i])
                row.append(self.selectedAuthors[i])
                rowContentList.append(row)

            self.reSelectionDict = {}
            self.generalSetTableContent(self.open_dialogSearch.tableWidget_2,rowContentList,headerList,self.reSelectionDict)


    def generalSetTableContent(self,table,rowContentList,headerList,selectionDict):
        i = 0
        for head in headerList:
            table.setHorizontalHeaderItem(i,QTableWidgetItem(QIcon('GUI/resources/sort-up.png'),head))
            i+=1
        defaultRow = len(rowContentList)
        table.setRowCount(defaultRow)
        for row in range(defaultRow):
            tmp = rowContentList[row]
            for idx in range(len(tmp)):
                table.setItem(row,idx,QTableWidgetItem(tmp[idx]))
        table.setSelectionBehavior(1)
        table.setSelectionMode(2)
        selectionDict.clear()
        selectionDict['row_number']=[]
        selectionDict['row']=[]
        selectionDict['table']=table
        selectionDict['headerList'] = headerList
        for item in headerList:
            selectionDict[item] = []

        self.genSelectionList = [selectionDict]
        table.cellClicked.connect(self.genSetCheckState)

    def genSetCheckState(self,row,column):
        #print('genSetCheckState:self.genSelectionList',self.genSelectionList)
        if row not in self.genSelectionList[0]['row_number']:
            self.genSelectionList[0]['row_number'].append(row)
            rowContent = []
            for idx in range(len(self.genSelectionList[0]['headerList'])):
                widget = self.genSelectionList[0]['table'].item(row,idx)
                rowContent.append(widget.text())
                self.genSelectionList[0][self.genSelectionList[0]['headerList'][idx]].append(widget.text())
            self.genSelectionList[0]['row'].append(rowContent)
        else:
            self.genSelectionList[0]['row_number'].remove(row)
            rowContent = []
            for idx in range(len(self.genSelectionList[0]['headerList'])):
                widget = self.genSelectionList[0]['table'].item(row,idx)
                rowContent.append(widget.text())
                self.genSelectionList[0][self.genSelectionList[0]['headerList'][idx]].remove(widget.text())
            self.genSelectionList[0]['row'].remove(rowContent)

        if len(self.genSelectionList[0]['row']) > 3:
            QMessageBox.warning(None,'Warning','Every borrower is allowed to check out only 3 books!')

        if self.genSelectionList[0] == self.selectedBorrDict and self.selectedIsbns:
            self.genSelectionList[0] = self.reSelectionDict

        print('reselect=',self.reSelectionDict)
        print('selectedRows=',self.selectedIsbns)
        print('selectedLoan=',self.selectedLoanDict)
        print('selectedFine=',self.selectedFineDict)


    def onCheckBorrowerClicked(self):

        self.checkBorrowerPressed = True
        print('Fname=',self.fname,'Lname=',self.lname,'Card_no=',self.card_no,'ssn=',self.ssn,'address=',self.address,'phone=',self.phone)

        headerList = [
            'Card_no',
            'SSN',
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
            "WHERE "
        )
        param = []
        i = 0
        if (not self.card_no[0]) and (not self.ssn[0]) and (not self.fname[0]) and (not self.lname[0]) and (not self.street_address[0]) and (not self.phone[0]):
            QMessageBox.critical(None,'Error','Lack of information for processing!')
        else:
            if self.card_no[0] and self.card_no[0][0] != '':
                statement = "Card_no=%s "
                query += statement
                param.append(self.card_no[0][0])
                i += 1

            if self.address[0] and self.address[0][0] != '':
                if i == 0:
                    statement = "Street_Address=%s "
                else:
                    statement = "AND Street_Address=%s "
                query += statement
                param.append(self.address[0][0])
                i += 1

            if self.phone[0] and self.phone[0][0] != '':
                if i==0:
                    statement = "Phone=%s "
                else:
                    statement = "AND Phone=%s "
                query += statement
                param.append(self.phone[0][0])
                i += 1

            if self.ssn[0] and self.ssn[0][0] != '':
                if i == 0:
                    statement = "Ssn=%s "
                else:
                    statement = "AND Ssn=%s "
                query += statement
                param.append(self.ssn[0][0])
                i += 1

            if self.fname[0] and self.fname[0][0] != '':
                if i==0:
                    statement = "Fname=%s "
                else:
                    statement = "AND Fname=%s "
                query += statement
                param.append(self.fname[0][0])
                i += 1
            if self.lname[0] and self.lname[0][0] != '':
                if i==0:
                    statement = "Lname=%s "
                else:
                    statement = "AND Lname=%s "
                query += statement
                param.append(self.lname[0][0])
                i += 1

            query += ';'

            result = self.sql.query(query,param)
            print('borrower:',result)
            self.selectedBorrDict = {}
            self.open_dialogSearch.tableWidget_1.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.open_dialogSearch.tableWidget_1.setColumnCount(len(headerList))
            self.generalSetTableContent(self.open_dialogSearch.tableWidget_1,result,headerList,self.selectedBorrDict)


    def onCheckLoanClicked(self,checkFineFlag=False,checkOutFlag=False,checkInFlag=False):
        if self.reSelectionDict:
            reselectList_tmp = copy.deepcopy(self.reSelectionDict['ISBN'])
        else:
            reselectList_tmp = None
        print('check borrower pressed',self.checkBorrowerPressed)
        print('selectedBorrDict',self.selectedBorrDict)
        print('selectedIsbns:',self.selectedIsbns)
        # check and set flag
        if self.checkBorrowerPressed and (not self.selectedIsbns):
            flag = 0
        elif (self.reSelectionDict or self.selectedIsbns) and not self.checkBorrowerPressed:
            flag = 1
        else:
            flag = 2
        if checkOutFlag: flag = 3
        if checkInFlag:
            if self.checkBorrowerPressed:
                flag = 0
            else:
                self.selectedBorrDict = {}
                self.selectedBorrDict['Card_no'] = self.selectedLoanDict['Card_no']
                flag = 0
        print('onCheckLoanClicked,flag:',flag)
        if checkFineFlag: flag2 = 4
        if checkFineFlag:
            self.loan_record, self.full_loan_record = self.checkLoan(reselectList_tmp,flag),self.checkLoan(reselectList_tmp,flag2)
        else:
            self.loan_record = self.checkLoan(reselectList_tmp,flag)

        print('loan_record=',self.loan_record)
        print('checkBorrowerPressed:',self.checkBorrowerPressed)
        print('selectedRows:',self.selectedIsbns)
        if not checkFineFlag:
            if not self.loan_record:
                QMessageBox.information(None,'Loan Information','No Loan record is found')
                return None
        else:
            if not self.full_loan_record:
                QMessageBox.information(None,'Loan Information','No Loan record is found')
                QMessageBox.information(None,'Fine Information','No Fine record is found')
                return None,None

        self.selectedLoanDict = {}
        headerList = [
            'Loan_id',
            'Book_id',
            'Card_no',
            'Date_out',
            'Due_date',
            'Date_in'
        ]
        rowContentList = []
        for tup in self.loan_record:
            row = []
            for idx in range(len(tup)):
                if idx < 3:
                    row.append(str(tup[idx]))
                else:
                    if tup[idx]:
                        date = str(tup[idx].year)+'-'+str(tup[idx].month)+'-'+str(tup[idx].day)
                        row.append(date)
                    else:
                        row.append('NA')
            rowContentList.append(row)
        if checkFineFlag:
            rowContentList2 = []
            for tup in self.full_loan_record:
                row = []
                for idx in range(len(tup)):
                    if idx < 3:
                        row.append(str(tup[idx]))
                    else:
                        if tup[idx]:
                            date = str(tup[idx].year)+'-'+str(tup[idx].month)+'-'+str(tup[idx].day)
                            row.append(date)
                        else:
                            row.append('NA')
                rowContentList2.append(row)
        print('onCheckLoanClicked loan_record:',rowContentList)
        if checkFineFlag:
            return rowContentList,rowContentList2


        #if self.selectedIsbns:
        #    self.checkBorrowerPressed = False
        if self.selectedIsbns:
            self.open_dialogSearch.tableWidget_2.cellClicked.disconnect()
        if self.checkBorrowerPressed and not checkInFlag:
            self.open_dialogSearch.tableWidget_1.cellClicked.disconnect()
        self.checkLoanPressed = True

        if self.selectedIsbns:
            headerList2 = [
                'ISBN',
                'Book Authors',
            ]
            self.open_dialogSearch.tableWidget_1.clear()
            self.open_dialogSearch.tableWidget_1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.open_dialogSearch.tableWidget_1.setColumnCount(2)
            if self.reSelectionDict['row']:
                self.generalSetTableContent(self.open_dialogSearch.tableWidget_1,self.reSelectionDict['row'],headerList2,self.reSelectionDict)
            else:
                rowContentList2 = []
                for i in range(len(self.selectedIsbns)):
                    row = []
                    row.append(self.selectedIsbns[i])
                    row.append(self.selectedAuthors[i])
                    rowContentList2.append(row)
                    self.generalSetTableContent(self.open_dialogSearch.tableWidget_1,rowContentList2,headerList2,self.reSelectionDict)
            self.open_dialogSearch.tableWidget_2.clear()
        # output to GUI
        self.open_dialogSearch.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.open_dialogSearch.label_changable.setText('Loan')
        self.open_dialogSearch.tableWidget_2.setColumnCount(len(headerList))
        self.generalSetTableContent(self.open_dialogSearch.tableWidget_2,rowContentList,headerList,self.selectedLoanDict)


    def onCheckFineClicked(self,checkOutFlag=False):
        rowContentList,rowContentList2 = self.onCheckLoanClicked(True,checkOutFlag)
        if not rowContentList2: return
        Loan_idList = [int(row[0]) for row in rowContentList2]
        self.fine_record = findFine(self.sql,Loan_idList)

        print('onCheckFineClicked fine_record:',self.fine_record)

        if not self.fine_record:
            QMessageBox.information(None,'Fine Information','No fine record is found')
            return

        if self.checkBorrowerPressed or (self.checkLoanPressed and self.selectedIsbns):
            self.open_dialogSearch.tableWidget_1.disconnect()
        self.open_dialogSearch.tableWidget_1.clear()
        self.open_dialogSearch.tableWidget_1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        headerList = [
            'loan_id',
            'Fine_amt',
            'Paid'
        ]

        rowContentList = []
        for tup in self.fine_record:
            row = []
            for idx in range(len(tup)):
                if idx < 2:
                    row.append(str(tup[idx]))
                else:
                    if tup[idx] == 0:
                        row.append('Unpaid')
                    else:
                        row.append('Paid')
            rowContentList.append(row)

        print('fine record:',rowContentList)

        self.selectedFineDict = {}
        self.open_dialogSearch.tableWidget_1.setColumnCount(len(headerList))
        self.generalSetTableContent(self.open_dialogSearch.tableWidget_1,rowContentList,headerList,self.selectedFineDict)
        return rowContentList



    def checkLoan(self,reselectList_tmp=None,flag=None):
        # flag=0 card_no only
        # flag=1 id list only
        # flag=2 both
        # flag=3 both,but for checkOut,check loan only according to Card_no
        # flag=4 card_no only, but check all the history loan record for a borrower, check fine only
        if flag == 0:
            return findLoan(self.sql,None,self.selectedBorrDict['Card_no'][0])
        if flag == 4:
            return findLoan(self.sql,None,self.selectedBorrDict['Card_no'][0],fullRecord=True)
        currId = self.open_dialogSearch.comboBox_branch_id.currentText()
        book_idList = []
        query = (
            "SELECT Book_id FROM book_copies "
            "WHERE Branch_id=%s "
            "AND ((Isbn=%s) "
        )
        statement = "OR (Isbn=%s) "

        if reselectList_tmp:
            Isbn_tmp_list = reselectList_tmp
        else:
            Isbn_tmp_list = self.selectedIsbns

        self.final_Isbn_list = Isbn_tmp_list
        print('checkLoan:',Isbn_tmp_list)

        i=0
        param = []
        param.append(currId)
        for each in Isbn_tmp_list:
            if i==0:
                pass
            else:
                query += statement
            param.append(each)
            i+=1
        query += ');'
        res = self.sql.query(query,tuple(param))
        for each in res:
            book_idList.append(each[0])

        if flag == 1:
            return findLoan(self.sql,book_idList,None)
        if flag == 2:
            loan_record = findLoan(self.sql,book_idList,self.selectedBorrDict['Card_no'][0])
            return loan_record
        if flag == 3:
            return findLoan(self.sql,None,self.selectedBorrDict['Card_no'][0])


    def checkOut(self):
        #self.onCheckLoanClicked(False,True)
        self.onCheckFineClicked(True)

        print('loan record=',self.loan_record)
        print('fine record=',self.fine_record)

        if self.fine_record:
            QMessageBox.critical(None,'Prohibited','This borrower has an unpaid fine record!')
            return
        if len(self.loan_record) >= 3:
            QMessageBox.critical(None,'Prohibited','This borrower has reached the allowed book loan number limit!')
            return
        self.Overdue_record = findOverDue(self.sql,None,self.selectedBorrDict['Card_no'][0])
        if self.Overdue_record:
            QMessageBox.critical(None,'Prohibited', 'overdue books are found in record!')
            return

        query = (
            "INSERT INTO `book_loans` "
            "(`Book_id`,`Card_no`,`Due_date`) "
            "VALUES ("
            "(SELECT `Book_id` FROM `book_copies` WHERE `Branch_id` = %s AND `Isbn`=%s),"
            "(SELECT `Card_no` FROM `borrower` WHERE `Card_no` = %s),"
            "(DATE_ADD(NOW(),INTERVAL %s DAY))"
            ");"
        )
        Cmd_copies_checkout = (
            "UPDATE `book_copies` "
            "SET No_of_copies=No_of_copies-1 "
            "WHERE `Branch_id` = %s AND `Isbn`=%s;"
        )
        currId = self.open_dialogSearch.comboBox_branch_id.currentText()
        if len(self.final_Isbn_list) > 3:
            QMessageBox.warning(None,'Warning','Every borrower is allowed to check out only 3 books!')
        i = 0
        for each in self.final_Isbn_list:
            i += 1
            print(len(self.loan_record)+i)
            if len(self.loan_record)+i>3:
                QMessageBox.warning(None,'Prohibited','This borrower has reached the allowed book loan number limit!\n Operation Completes')
                break
            param = []
            param.append(currId)
            param.append(each)
            param.append(self.selectedBorrDict['Card_no'][0])
            param.append(self.bookloan_allowed_duration)
            self.sql.executeCmd(query,param)
            self.sql.executeCmd(Cmd_copies_checkout,(currId,each))
            self.sql.submite()
        self.onCheckLoanClicked(False,True)
        QMessageBox.information(None,'Completed','Operation Completes!')

    def checkIn(self):
        if not self.selectedLoanDict or (not self.selectedLoanDict['Loan_id']):
            QMessageBox.warning(None,'Warning','Please Check Loan and select a loan record first!')

        Cmd = (
            "UPDATE `book_loans` "
            "SET Date_in=NOW() "
            "WHERE loan_id=%s;"
        )
        Cmd_copies_checkin = (
            "UPDATE `book_copies` "
            "SET No_of_copies=No_of_copies+1 "
            "WHERE `Book_id`="
            "(SELECT `Book_id` FROM book_loans WHERE loan_id=%s);"
        )
        Cmd_fine = (
            "INSERT INTO `fines` "
            "(`loan_id`,`Fine_amt`,`Paid`) "
            "VALUES ("
            "(SELECT `loan_id` FROM `book_loans` WHERE `loan_id` = %s), "
            "DATEDIFF("
            "CURDATE(),(SELECT DATE(Due_date) FROM `book_loans` WHERE `loan_id` = %s)"
            ")*%s,"
            "%s"
            ");"
        )
        for loan_id in self.selectedLoanDict['Loan_id']:
            overdue = checkOverdue(self.sql,loan_id)
            print('loan_id=',loan_id)
            print('feeRate',self.feeRate)
            if overdue:
                print('overdue')
                self.sql.executeCmd(Cmd,(int(loan_id),))
                self.sql.executeCmd(Cmd_fine,(int(loan_id),int(loan_id),self.feeRate,0))
                self.sql.executeCmd(Cmd_copies_checkin,(int(loan_id),))
                self.sql.submite()
            else:
                print('normal')
                self.sql.executeCmd(Cmd,(int(loan_id),))
                self.sql.executeCmd(Cmd_copies_checkin,(int(loan_id),))
                self.sql.submite()
        QMessageBox.information(None,'Check In','Operatio Completes!')
        self.onCheckLoanClicked(False,False,True)
