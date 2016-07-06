import re
import csv
from dataParser import csvParser
from callback import callbacks
from PyQt5.QtWidgets import QComboBox

class FFilter(csvParser):
    
    def __init__(self,filepath,delim='\t'):
        super(FFilter,self).__init__(filepath,delim)
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
    

    
    def checkNoise(self,data,selection=None,result=None,target=None,show=None,box=None):
        if not selection:
            selection = self.collection
        if box:
            box.clear()
            box.addItems(selection)

        self.noisy_collect = {}
        self.noisy_data_index = {}

        for char in selection:
            noisy_data = []
            index = []
            idx = 0
            for each in data:
                if char != ';':
                    if each.find(char) != -1:
                        noisy_data.append(each)
                        index.append(idx)
                else:
                    if each.find(char) != -1 and each.find('&amp;') == -1:
                        noisy_data.append(each)
                        index.append(idx)
                idx += 1
            self.noisy_collect[char] = noisy_data
            self.noisy_data_index[char] = index
        
        if result:
            result[0]=self.noisy_data_index
            result[1]=self.noisy_collect

    def showNoise(self,show=None,target=None,noisydata=None):
        if target and noisydata:
            callbacks().setviewText(self.printNoise(show,noisydata),target)
        
    def printNoise(self,selection,noisydata):
        if not selection: return ''
        
        printdata = '\n \n \nSelected Column: ' + selection +'\n \n'

        if not noisydata[selection]:
            printdata += 'No noisy data found\n'
        else:
            printdata += '\n'.join(noisydata[selection])
        return printdata

        
       
                    
    


        

    



    
