# MyLib
a Library Management Software based on PyQt5

####Design Document
https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/Design%20Document.pdf
####User Guide
https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide.pdf
####Install Instruction
#####Framework and third-party library used:

    Qt Version 5.2.1
    Python3 - PyQt5             install Qt and Python3-PyQt5:  pip3 install PyQt5
    Python 3.4.3
    MySQL-Python interface      download from MySQL official website and install it.

#####Platform： 
Linux Mint

#####Install Instruction

1. go to MyLib/Option/

   keyword.csv    --   this is automatic extracted keywords while importing the data by the application.
                       It is used for fuzzy-finder embedded in the application. Strongly suggested to
                       import to support full functionality.
                       
  keywordImport.py --  this is a python script which create a table in the Library database and import
                       keyword.csv into the database. Strongly suggested to run to support full functionality

  loan_fine_test.py--  for test purpose only. Do not run!
2. open a terminal and find the umain.py file. Input following command to start application.

   python3 uimain.py
   
####Examples

#####Import Data
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/import%20data%201.gif)
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/import%20data%202.gif)
#####Search
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/search.gif)
#####Check In/Out
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/check%20out%20and%20in.gif)
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/check%20out%20and%20in%202.gif)
#####Check Out but find an overdue book
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/check_out_overdue.gif)
#####Check in an overdue book, generate a fine record and check Out but find an unpaid fine
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/Overdue%20and%20fine.gif)
#####Check Loan and check fine
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/Check%20loan%20and%20fine.gif)
#####Check fine and payment
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/Check%20fine%20and%20fine%20payment.gif)
#####Add/Edit borrower:
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/add_edit_borrower.gif)
#####Check overdue books
![](https://github.com/AlenUbuntu/MyLib/blob/master/MyLib/User%20Guide/check_overdue.gif)


