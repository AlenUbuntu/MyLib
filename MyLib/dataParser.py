import csv
import re
import sys,os
from PyQt5.QtWidgets import QProgressBar
import callback

class csvParser:
    def __init__(self,filepath,delim='\t'):
        self.filepath = filepath
        self.delim = delim
    
    def printFile(self):
        self.parseToDict()
        # print parsing information to console
        header = ''
        for token in self.head:
            header += token + '\t\t'
        print(header)
        
        for idx in range(len(self.dictionary[self.head[0]])):
            out = ''
            for key in self.head:
                out += self.dictionary[key][idx]
                out += '\t\t'
            print(out)
           
    def parseToDict(self,progressBar=None):
        print('delim:',self.delim)
        with open(self.filepath,encoding='utf8') as csvfile:
            reader = csv.reader(csvfile,delimiter=self.delim)
            self.head = next(reader)
            
            
            # read following data into a dictionary
            # start to read data, could set progress bar here

            reader = csv.DictReader(csvfile,fieldnames=self.head,delimiter=self.delim)
                
            self.dictionary={key:[] for key in self.head}
            filesize =os.path.getsize(self.filepath)
            counter = 0
   
            print('size',filesize)
            print('counter',counter)

            for line in reader:
                for key in self.head:
                    self.dictionary[key].append(line[key])
                    if progressBar: 
                        counter += sys.getsizeof(line[key])
                        progress = counter
                        progressBar.setValue(progress)
            if progressBar:
                progressBar.setValue(filesize)  
            return self.head,self.dictionary

    def checkNoise(self,data,format,result=None,target=None):
            ''' 
            format rule: 
                d represents a single digit
                l represents a lowercase letter
                L represents an uppercase letter
                url represents a url
                num represents a number
                strs represents any normal string
                email represents an email address
                / represents 'or'
            '''
          #  print('entered')
          #  print(data)
          #  print(result)
            if result: result[0] = None
            noise = []
            if format == 'url':
                pattern = re.compile('http[s]*://www\.[a-zA-Z0-9_]+\.[a-zA-Z]+[/a-zA-Z0-9_]*\.*[a-zA-Z]*')
            elif format == 'num':
                pattern = re.compile('[0-9]+')
            elif format == 'strs':
                pattern = re.compile('[,a-zA-Z:\. 0-9]+')
            elif format == 'email':
                pattern = re.compile('[a-zA-Z0-9\._]+@[a-zA-Z0-9_]+[\.][a-zA-Z]+[\.a-zA-Z]*')
            else:
                while '/' in format:
                    tmp = format.index('/')
                    format = format[:tmp+2]+'*'+format[tmp+2:]
                    format = format.replace('/','*',1)
                if '**' in format:
                    format = format.replace('**','*')
                if 'd' in format:
                    format = format.replace('d','[0-9]')
                if 'l' in format:
                    format = format.replace('l','[a-z]')
                if 'L' in format:
                    format = format.replace('L','[A-Z]')
                if '(' in format and ')' in format:
                    format = format.replace('(','\(')
                    format = format.replace(')','\)') 
                pattern = re.compile(format)

            for idx in range(len(data)):                   
                mobj = pattern.fullmatch(data[idx])
                if not mobj:
                    noise.append(idx)
            if not result:
               # print('1')
                return noise
            else:
               # print('2')
                result[0]=noise
               # print(result[0])
                callback.callbacks().setviewText('\n'.join([data[i] for i in result[0]]),target)

                
        
    def noiseCorrect(self,old,new,dataIndex,data,target=None):
            print(dataIndex)
            for idx in dataIndex:
                data[idx] = data[idx].replace(old,new)
            callback.callbacks().setviewText('Corrected Result: \n'+'\n'.join(data[i] for i in dataIndex),target)

#parse = csvParser(r'D:\Dropbox\Computer_science\UTD COURSE\2016 summer\database design\Project\Project Code\Data\borrowers.csv',',')
#parse.parseToDict()
#tmp = parse.checkNoise(parse.dictionary['email'],'email')
#parse.noiseCorrect('-','_',tmp,parse.dictionary['email'])
#print(list(parse.dictionary['email'][idx] for idx in parse.checkNoise(parse.dictionary['email'],'email')))
