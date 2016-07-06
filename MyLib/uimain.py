from GUI.mainwindow import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import functools
from callback import callbacks
from bookManage_callback import *
from borr_manage_add import *
from borr_manage_ved import *
from checkfine_callback import *
from checkOverdue_callback import *

class Ui_Setup:
    def __init__(self):
        app = QApplication(sys.argv)
        self.feeRate=0.25
        self.bookloan_allowed_duration=14
        self.sql=sqlCommand()
        mainWindow = QMainWindow()
        self.callback = callbacks()
        self.bookM_callback = bookm_call(bookloan_allowed_duration=self.bookloan_allowed_duration,feeRate=self.feeRate,sql=self.sql)
        self.borrManage = borrMagCallback(sql=self.sql)
        self.setupMainWindow(mainWindow)
        mainWindow.show()
        sys.exit(app.exec_())

    def setupMainWindow(self,MainWindow,*args):
        self.Ui_MainWd = GUI.mainwindow.Ui_MainWindow()
        self.Ui_MainWd.setupUi(MainWindow)
        self.Ui_MainWd.MyLib_filter_fileSelector.clicked.connect(lambda: self.callback.button_openFileDialog(self.Ui_MainWd.MyLib_filter_textview))
        self.Ui_MainWd.pushButton.clicked.connect(lambda: self.callback.button_openFilterSettingDialog(self.Ui_MainWd.MyLib_filter_textview))
        self.Ui_MainWd.MyLib_filter_start.clicked.connect(lambda: self.callback.readFiles(self.Ui_MainWd.MyLib_filter_progressbar,self.Ui_MainWd.MyLib_filter_textview))
        self.Ui_MainWd.pushButton_2.clicked.connect(lambda: self.callback.writeFiles(MainWindow))
        self.Ui_MainWd.pushButton_importDB.clicked.connect(self.bookM_callback.button_openFurFilterDialog)
        self.Ui_MainWd.pushButton_search.clicked.connect( lambda: self.search(self.sql))
        self.Ui_MainWd.pushButton_checkOut.clicked.connect(lambda: self.check_in_out(self.sql,0))
        self.Ui_MainWd.pushButton_checkIn.clicked.connect(lambda: self.check_in_out(self.sql,1))
        self.Ui_MainWd.pushButton_createBorr.clicked.connect(self.borrManage.open_createBorr)
        self.Ui_MainWd.pushButton_viewBorr.clicked.connect(lambda:self.borr_mod(self.sql,0))
        self.Ui_MainWd.pushButton_modifyBorr.clicked.connect(lambda:self.borr_mod(self.sql,1))
        self.Ui_MainWd.pushButton_deleteBorr.clicked.connect(lambda:self.borr_mod(self.sql,2))
        self.Ui_MainWd.pushButton_checkFIne.clicked.connect(self.checkFine)
        self.Ui_MainWd.pushButton_setting.clicked.connect(self.getSettingVal)
        self.Ui_MainWd.pushButton_checkOverdue.clicked.connect(self.checkOverdue)

    def getSettingVal(self):
        res = QInputDialog.getDouble(None,'Fee Rate of Fine','Fine Fee Rate:',value=0.25,min=0,decimals=2)
        if res[1]:
            self.feeRate = res[0]
        else:
            self.feeRate = 0.25    #default value
        print(self.feeRate)

    def search(self,sql):
        print('enter')
        callback0 = bookm_functional_call(bookloan_allowed_duration=self.bookloan_allowed_duration,feeRate=self.feeRate,sql=sql)
        callback0.button_openSearch(True)

    def check_in_out(self,sql,flag):
        print('enter')
        callback = bookm_functional_call(bookloan_allowed_duration=self.bookloan_allowed_duration,feeRate=self.feeRate,sql=sql)
        callback.button_openSearch(flag=flag)
    def borr_mod(self,sql,flag):
        print('enter')
        self.callback2 = borr_manage_mod(sql=sql)
        self.callback2.open_mod_dialog(flag)

    def checkFine(self):
        self.checkfineManage = checkfine_callbacks(self.sql)
        self.checkfineManage.open_dialog_checkfine()
    def checkOverdue(self):
        self.checkoverdueManage = checkOverdue_callbacks(self.sql)
        self.checkoverdueManage.open_dialog_checkOverdue()

if __name__=='__main__':
    ui = Ui_Setup()
