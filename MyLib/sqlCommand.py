import mysql.connector
import sys
from mysql.connector import errorcode
from PyQt5.QtWidgets import QMessageBox,QApplication,QInputDialog,QProgressDialog

class sqlCommand:

    def __init__(self,flag=None):
        ans = QMessageBox.question(None,'Log In','click Yes to log in!')
        if ans == 0x00004000:
            username = QInputDialog.getText(None,"Database User Name","Please Enter User Name")[0]
            passwd = QInputDialog.getText(None,"Database User Password","Please Enter User Password")[0]
            host = QInputDialog.getText(None,"Database Host Address","Please Enter IP address:")[0]
            db = QInputDialog.getText(None,"Database Name","Default database is Library")[0]


            if username and passwd and host:
                if db == '':
                    self.logIn(username,passwd,host)
                else:
                    self.logIn(username,passwd,host,db)
            else:
                QMessageBox.critical(None,"Failed!","Missing information to log into the database")
                sys.exit()
        else:
            QMessageBox.critical(None,'Login Required!','Please log in first')
            sys.exit()
            if flag: flag[0] = 0


    def logIn(self,username,passwd,host,db='Library'):

        try:
            self.cnx = mysql.connector.connect(
                user=username,
                password=passwd,
                host=host,
                database=db
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.critical(None,"Error!","Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_HOST_ERROR:
                QMessageBox.critical(None,"Error!","Host address does not exist")
            else:
                QMessageBox.critical(None,"Error!",str(err))
            sys.exit()
        else:
            if self.cnx.is_connected():
                QMessageBox.information(None,"Succeed!",'Connection Established')
                self.cursor=self.cnx.cursor(buffered=True)

    def submite(self):
        self.cnx.commit()

    def disconnect(self):
        self.cursor.close()
        self.cnx.close()
        QMessageBox.information(None,'Status','connection to database disconnected successfully')

    def query(self,statement,params=None):
        if params:
            self.cursor.execute(statement,params)
        else:
            self.cursor.execute(statement)

        if self.cursor.with_rows:
            result = self.cursor.fetchall()
        return result
    def executeCmd(self,cmd,params):
        self.cursor.execute(cmd,params)
