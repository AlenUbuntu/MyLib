from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5.QtWidgets import QFileDialog
from GUI.dialog_openFile import *
from GUI.dialog_filter import *
from dataParser import *
import os,csv

class callbacks:

    def __init__(self):
        self.url=''
        self.readFile=False
        self.delim = '\t'
        self.noiseList=[None]

    def getURL(self,target,*other):
        qurl = QFileDialog.getOpenFileUrl()
        self.url = qurl[0].url()
        self.open_dialog.textView_filter_showFile.setText(self.url)
        if other:
            for each in other:
                each.setText(self.url)
        self.setviewText('File selected:\t'+self.url,target)
    
    def readFiles(self,target1=None,target2=None,*otherCombo):
        
        # clear comboBoxes
        if otherCombo:
            for each in otherCombo:
                each.clear()
        
        # set default delimiter
        self.delim = self.delim or '\t'

        if not self.url:
            QMessageBox.warning(target2,'Serious Problem!','No File Selected For Processing!\nPlease select a file first',QMessageBox.Close)

        # remove 'file://'
        self.url=self.url[7:]
        pars = csvParser(self.url,self.delim)
        if target1:
            target1.setMinimum(0)
            target1.setMaximum(os.path.getsize(self.url))
        if target2:
            self.setviewText('start parsing file!',target2)

        self.header,self.dicts = pars.parseToDict(target1)

        if target2:
            self.setviewText('parsing finished!',target2) 
        # set status 
        self.readFile=True
        # restore default value
        self.bkDelim = self.delim
        self.delim='\t'


        if otherCombo:
            for each in otherCombo:
                each.addItems(self.header)


    def getviewText(self,target=None):
        self.text = ''
        if target:
            self.text =target.text()
        #print(self.text)
    
    def getDelimiter(self,target=None):
        if target:
            print(target.text())
            self.delim =target.text() or '\t'
    
    def getFormat(self,target=None):
        self.format = ''
        if target:
            self.format =target.text()
       # print(self.format)

    def getNoise(self,target=None):
        self.noise = ''
        if target:
            self.noise =target.text()
       # print(self.noise)
    
    def getRep(self,target=None):
        self.rep = ''
        if target:
            self.rep =target.text()
       # print(self.rep)
    
    def setviewText(self,text,target=None):
        if target:
            target.append(text)

    def button_openFileDialog(self,targets = None,*other):
        self.dialog = QDialog()
        self.open_dialog = Ui_Dialog_openFile()
        self.open_dialog.setupUi(self.dialog)
        self.dialog.show()
        self.open_dialog.pushButton_filter_select.clicked.connect(lambda: self.getURL(targets,*other))        
        self.open_dialog.lineEdit_filter_delimiter.textChanged.connect(lambda: self.getDelimiter(self.open_dialog.lineEdit_filter_delimiter))
        self.open_dialog.lineEdit_filter_delimiter.returnPressed.connect(lambda: self.getDelimiter(self.open_dialog.lineEdit_filter_delimiter))
        self.open_dialog.lineEdit_filter_delimiter.editingFinished.connect(lambda: self.getDelimiter(self.open_dialog.lineEdit_filter_delimiter))
        self.open_dialog.pushButton_filter_delSubmit.clicked.connect(lambda: self.getDelimiter(self.open_dialog.lineEdit_filter_delimiter))
        self.open_dialog.lineEdit_filter_delimiter.returnPressed.connect(lambda: self.setviewText(target=targets,text='delimiter:\t'+ self.delim))
        self.open_dialog.pushButton_filter_delSubmit.clicked.connect(lambda: self.setviewText(target=targets,text='delimiter:\t'+ self.delim))

    def button_openFilterSettingDialog(self,targets=None):
        if not self.url:
            QMessageBox.warning(targets,'Serious Problem!','No File Selected For Processing!\nPlease select a file first',QMessageBox.Close)
            return
        if not self.readFile:
            QMessageBox.warning(targets,'Serious Problem!','No data read in yet!\nPlease read the file first by pressing the start button',QMessageBox.Close)
            return

        self.dialogFilSetting = QDialog()
        self.open_dialogFilSetting = Ui_Dialog_filter()
        self.open_dialogFilSetting.setupUi(self.dialogFilSetting)
        self.dialogFilSetting.show()
        self.open_dialogFilSetting.comboBox_filter_column.addItems(self.header)
        self.open_dialogFilSetting.comboBox_repSelect.addItems(self.header)
        self.filterIndex = [0]
        self.repIndex = [0]
        self.open_dialogFilSetting.comboBox_filter_column.currentIndexChanged.connect(lambda: self.comboBox_getCurrentItem(
            self.open_dialogFilSetting.comboBox_filter_column,
            self.filterIndex
        ))
        self.open_dialogFilSetting.comboBox_repSelect.currentIndexChanged.connect(lambda: self.comboBox_getCurrentItem(
            self.open_dialogFilSetting.comboBox_repSelect,
            self.repIndex
        ))

        self.open_dialogFilSetting.lineEdit_filter_format.textChanged.connect(lambda: self.getFormat(self.open_dialogFilSetting.lineEdit_filter_format))
        self.open_dialogFilSetting.lineEdit_filter_format.returnPressed.connect(lambda: self.getFormat(self.open_dialogFilSetting.lineEdit_filter_format))
        self.open_dialogFilSetting.lineEdit_filter_format.editingFinished.connect(lambda: self.getFormat(self.open_dialogFilSetting.lineEdit_filter_format))
        self.open_dialogFilSetting.lineEdit_filter_format.editingFinished.connect(lambda: self.setviewText(
            target=self.open_dialogFilSetting.textView_filter_detail,
            text='format:\t'+ self.format))


        self.open_dialogFilSetting.lineEdit_filter_noise.textChanged.connect(lambda: self.getNoise(self.open_dialogFilSetting.lineEdit_filter_noise))
        self.open_dialogFilSetting.lineEdit_filter_noise.returnPressed.connect(lambda: self.getNoise(self.open_dialogFilSetting.lineEdit_filter_noise))
        self.open_dialogFilSetting.lineEdit_filter_noise.editingFinished.connect(lambda: self.getNoise(self.open_dialogFilSetting.lineEdit_filter_noise))
        self.open_dialogFilSetting.lineEdit_filter_noise.editingFinished.connect(lambda: self.setviewText(
            target=self.open_dialogFilSetting.textView_filter_detail,
            text='noise:\t'+ self.noise))
        
        self.open_dialogFilSetting.lineEdit_filter_replace.textChanged.connect(lambda: self.getRep(self.open_dialogFilSetting.lineEdit_filter_replace))
        self.open_dialogFilSetting.lineEdit_filter_replace.returnPressed.connect(lambda: self.getRep(self.open_dialogFilSetting.lineEdit_filter_replace))
        self.open_dialogFilSetting.lineEdit_filter_replace.editingFinished.connect(lambda: self.getRep(self.open_dialogFilSetting.lineEdit_filter_replace))
        self.open_dialogFilSetting.lineEdit_filter_replace.editingFinished.connect(lambda: self.setviewText(
            target=self.open_dialogFilSetting.textView_filter_detail,
            text='replaced with:\t'+ self.rep))
        
        self.open_dialogFilSetting.pushButton_check.clicked.connect(lambda: csvParser(self.url,self.delim).checkNoise(
            self.dicts[self.header[self.filterIndex[0]]],
            self.format,
            self.noiseList,
            self.open_dialogFilSetting.textView_filter_detail
            ))
        
        self.open_dialogFilSetting.pushButton_repEnter.clicked.connect(lambda: csvParser(self.url,self.delim).noiseCorrect(
            self.noise,
            self.rep,
            self.noiseList[0],
            self.dicts[self.header[self.repIndex[0]]],
            self.open_dialogFilSetting.textView_filter_detail
        ))
        
    def comboBox_getCurrentItem(self,comboBoxs,container):
        container[0] = comboBoxs.currentIndex()
        print(container[0])

    
    def writeFiles(self,target):
        qurl = QFileDialog.getSaveFileUrl()
        url = qurl[0].url()[7:]
        print('url',url,'qurl',qurl[0])
        with open(url,encoding='utf8',newline='',mode='w') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=self.header,delimiter=self.bkDelim)
            writer.writeheader()
            
            for i in range(len(self.dicts[self.header[0]])):
                writer.writerow({h:self.dicts[h][i] for h in self.header})
        
        QMessageBox.information(target,'Write Complete!','Check it by yourself\n')






