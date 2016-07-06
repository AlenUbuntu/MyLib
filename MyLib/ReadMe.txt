############################################
Framework and third-party library used:
############################################
    Qt Version 5.2.1
    Python3 - PyQt5             install Qt and Python3-PyQt5:  pip3 install PyQt5
    Python 3.4.3
    MySQL-Python interface      download from MySQL official website and install it.

############################################
Platform： Linux Mint
############################################

############################################
Install Instruction
############################################
1. go to MyLib/Option/
   keyword.csv    --   this is automatic extracted keywords while importing the data by the application.
                       It is used for fuzzy-finder embedded in the application. Strongly suggested to
                       import to support full functionality.
  keywordImport.py --  this is a python script which create a table in the Library database and import
                       keyword.csv into the database. Strongly suggested to run to support full functionality

  loan_fine_test.py--  for test purpose only. Do not run!
2. open a terminal and find the umain.py file. Input following command to start application.
   python3 uimain.py

   I have include a pre-build executable version in the dist/. It supports all the functionality
   except a issue of loading several dynamically created GUI widget's icons.

    
