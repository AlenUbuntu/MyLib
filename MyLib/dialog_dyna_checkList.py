from GUI.dialog_checkList import *
from PyQt5.QtWidgets import QCheckBox,QDialog
import sys

'''
best usage: maximum 10 items
'''
class dyna_checkList_Dialog(Ui_Dialog):
    def __init__(self,Dialog,name=None,size=None):
        super(dyna_checkList_Dialog,self).setupUi(Dialog)
        if name:
            Dialog.setObjectName(name)
        if size:
            Dialog.resize(*size)
    
    def addWidgets(self,widgets):
        for widget in widgets:
            self.checkList_VL.addWidget(widget)
    
    def createCheckBoxs(self,content):
        self.widgetList = []
        for cont in content:
            self.widgetList.append(self.newCheckBox(cont))
        return self.widgetList
    
    def newCheckBox(self,content):
        box = QCheckBox(content)
        box.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        box.setStyleSheet(
            "font: 75 10pt \"Bitstream Charter\";"
        )
        box.setObjectName(content)
        return box
    
    def getWidgets(self):
        return self.widgetList
    

    
