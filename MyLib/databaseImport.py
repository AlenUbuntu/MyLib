import mysql.connector
import sys
from mysql.connector import errorcode
from PyQt5.QtWidgets import QMessageBox,QApplication,QInputDialog,QProgressDialog
from collections import OrderedDict
from dataParser import csvParser
import os,csv

DB_NAME = 'Library'
def start(fileList,username,passwd,host):
    try:
        cnx = mysql.connector.connect(
            user=username,
            password=passwd,
            host=host
            )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            QMessageBox.critical(None,"Error!","Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_HOST_ERROR:
            QMessageBox.critical(None,"Error!","Host address does not exist")
        else:
            QMessageBox.critical(None,"Error!",str(err))
    else:
        if cnx.is_connected():
            QMessageBox.information(None,"Succeed!",'Connection Established\nStart Importing')

        cursor = cnx.cursor(buffered = True)

        try:
            cnx.database=DB_NAME
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                cnx.database = DB_NAME
            else:
                QMessageBox.critical(None,"Error!",str(err))
                exit(1)
        finally:
            try:
                create_tables(cursor)
                insertData(cursor,fileList,cnx)
            except mysql.connector.Error as err:
                QMessageBox.critical(None,"Error!",str(err))
            finally:
                cursor.close()
                cnx.close()
                QMessageBox.information(None,'Status','Data Injection Completes!\n Database is ready for use')


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME)
        )
        QMessageBox.information(None,"Status","create database {} successfully".format(DB_NAME))
    except mysql.connector.Error as err:
        QMessageBox.critical(None,"Failed!","Failed creating database!".format(str(err)))
        exit(1)

def create_tables(cursor):
    TABLES = OrderedDict()
    TABLES['book']=(
        "CREATE TABLE `book` ("
        " `Isbn` CHAR(10) NOT NULL,"
        " `Title` VARCHAR(255) NOT NULL,"
        " `Book_authors` VARCHAR(255) NOT NULL,"
        " PRIMARY KEY (`Isbn`)"
        ")"
    )

    TABLES['authors']=(
        "CREATE TABLE `authors` ("
        " `Author_id` int AUTO_INCREMENT,"
        " `FName` VARCHAR(255) NOT NULL,"
        " `MName` VARCHAR(255),"
        " `LName` VARCHAR(255),"
        " PRIMARY KEY (`Author_id`)"
        ")"
    )


    TABLES['book_authors']=(
        "CREATE TABLE `book_authors` ("
        " `Author_id` int,"
        " `Isbn` CHAR(10),"
        " PRIMARY KEY (`Author_id`,`Isbn`),"
        " FOREIGN KEY (`Author_id`) REFERENCES authors(`Author_id`) ON DELETE CASCADE ON UPDATE CASCADE,"
        " FOREIGN KEY (`Isbn`) REFERENCES book(`Isbn`) ON DELETE CASCADE ON UPDATE CASCADE"
        ")"
    )

    TABLES['library_branch']=(
        "CREATE TABLE `library_branch` ("
        " `Branch_id` int,"
        " `Branch_name` VARCHAR(255) NOT NULL,"
        " `Street_Address` VARCHAR(255) NOT NULL,"
        " `Zip` CHAR(5) NOT NULL,"
        " PRIMARY KEY (`Branch_id`)"
        ")"
    )

    TABLES['book_copies']=(
        "CREATE TABLE `book_copies` ("
        " `Book_id` int AUTO_INCREMENT,"
        " `Isbn` CHAR(10),"
        " `Branch_id` int,"
        " `No_of_copies` int NOT NULL CHECK(`No_of_copies` >-2),"
        " PRIMARY KEY (`Book_id`),"
        " FOREIGN KEY (`Isbn`) REFERENCES book(`Isbn`) ON DELETE CASCADE ON UPDATE CASCADE,"
        " FOREIGN KEY (`Branch_id`) REFERENCES library_branch(`Branch_id`) ON DELETE CASCADE ON UPDATE CASCADE"
        ")"
    )

    TABLES['borrower']=(
        "CREATE TABLE `borrower` ("
        " `Card_no` CHAR(8),"
        " `Ssn` CHAR(11) NOT NULL,"
        " `Fname` VARCHAR(255) NOT NULL,"
        " `Lname` VARCHAR(255),"
        " `email` VARCHAR(255),"
        " `Street_Address` VARCHAR(255),"
        " `City` VARCHAR(255),"
        " `State` VARCHAR(255),"
        " `Phone` CHAR(14),"
        " CONSTRAINT phone_ssn UNIQUE(`Ssn`,`Phone`),"
        " PRIMARY KEY (`Card_no`)"
        ")"
    )

    TABLES['book_loans']=(
        "CREATE TABLE `book_loans` ("
        " `loan_id` int AUTO_INCREMENT,"
        " `Book_id` int,"
        " `Card_no` CHAR(8),"
        " `Date_out` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,"
        " `Due_date` TIMESTAMP NULL DEFAULT NULL,"
        " `Date_in` TIMESTAMP NULL DEFAULT NULL,"
        " PRIMARY KEY (`loan_id`),"
        " FOREIGN KEY (`Book_id`) REFERENCES book_copies(`Book_id`),"
        " FOREIGN KEY (`Card_no`) REFERENCES borrower(`Card_no`)"
        ")"
    )

    TABLES['fines']=(
        "CREATE TABLE `fines` ("
        " `loan_id` int,"
        " `Fine_amt` DECIMAL(10,2) DEFAULT 0,"
        " `Paid` int(1) DEFAULT 0,"
        " PRIMARY KEY (`loan_id`),"
        " FOREIGN KEY (`loan_id`) REFERENCES book_loans(`loan_id`)"
        ")"
    )

    for name, ddl in TABLES.items():
        try:
           QMessageBox.information(None,"Status","creating table: {}".format(name))
           cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                QMessageBox.warning(None,'Warning!','{} table already exists.\n Request is ignored'.format(name))
                pass
            else:
                QMessageBox.critical(None,"Failed!","{}".format(str(err)))
        else:
            QMessageBox.information(None,'Status','Table {} Creation Succeed'.format(name))
            pass

def insertData(cursor,fileList,cnx):

    #cnx = mysql.connector.connect(
    #        user='root',
    #        password='qwe5813653',
    #        host='127.0.0.1',
    #        database='Library'
    #        )
    #cursor = cnx.cursor(buffered = True)
    #fileList = ['/mnt/hgfs/2016 summer/database design/Project/Project Code/MyLib/Data/clean_result/borrowers.csv', '/mnt/hgfs/2016 summer/database design/Project/Project Code/MyLib/Data/clean_result/book_copies.csv', '/mnt/hgfs/2016 summer/database design/Project/Project Code/MyLib/Data/clean_result/library_branch.csv', '/mnt/hgfs/2016 summer/database design/Project/Project Code/MyLib/Data/clean_result/books.csv']

    numOfFiles = len(fileList)
    filenameList = []
    parser = {}

    for i in range(numOfFiles):
        filenameList.append(filenameFinder(fileList[i]))

    idx = 0
    print(filenameList)

    for url in fileList:
        delim = QInputDialog.getText(None,filenameList[idx]+' delimiter:',"Please Enter {} delimiter (tab default):".format(filenameList[idx]))[0] or '\t'
        header,dictionary = csvParser(url,delim).parseToDict()
        parser[filenameList[idx]]=(header,dictionary)
        idx += 1

    # construct data collection for each table

    book = []
    author = []
    Isbn_author={}
    library_branch = []
    book_copies = []
    borrower=[]

    print(parser['books'][1].keys())

    for i in range(len(parser['books'][1]['ISBN10'])):
        tmp = {}
        tmp['Isbn'] = parser['books'][1]['ISBN10'][i]
        tmp['Title'] = parser['books'][1]['Title'][i]
        tmp['Book_authors'] = ';'.join(set(parser['books'][1]['Authro'][i].split(';')))
        book.append(tmp)
        tmp_author = list(set(parser['books'][1]['Authro'][i].lower().split(';')))           # transfer all names to lower case and remove duplicates
        Isbn_author[tmp['Isbn']]=tmp_author
        author += tmp_author
    Isbn_and_author = [set(author),Isbn_author]   # book_author table

    for i in range(len(parser['library_branch'][1]['branch_id'])):
        tmp = {}
        tmp['branch_id'] = parser['library_branch'][1]['branch_id'][i]
        tmp['branch_name'] = parser['library_branch'][1]['branch_name'][i]
        tmp['address'] = parser['library_branch'][1]['address'][i].split(',')
        tmp['address'][1] = tmp['address'][1].lstrip(' ')
        library_branch.append(tmp)

    for i in range(len(parser['book_copies'][1]['book_id'])):
        tmp = {}
        tmp['Isbn'] = parser['book_copies'][1]['book_id'][i]
        tmp['branch_id'] = parser['book_copies'][1]['branch_id'][i]
        tmp['no_of_copies'] = parser['book_copies'][1]['no_of_copies'][i]
        book_copies.append(tmp)

    for i in range(len(parser['borrowers'][1]['ID0000id'])):
        tmp = {}
        tmp['Card_no'] = parser['borrowers'][1]['ID0000id'][i]
        tmp['ssn'] = parser['borrowers'][1]['ssn'][i]
        tmp['first_name'] = parser['borrowers'][1]['first_name'][i]
        tmp['last_name'] = parser['borrowers'][1]['last_name'][i]
        tmp['email'] = parser['borrowers'][1]['email'][i]
        tmp['street_address'] = parser['borrowers'][1]['address'][i]
        tmp['city'] = parser['borrowers'][1]['city'][i]
        tmp['state'] = parser['borrowers'][1]['state'][i]
        tmp['phone'] = parser['borrowers'][1]['phone'][i]
        borrower.append(tmp)

    QMessageBox.information(None,'Status','File Parsing Completes!\n Start inserting data into MySQL')
    # Start inserting data

    # create statement
    add_book =(
        "INSERT INTO `book` "
        "(`Isbn`,`Title`,`Book_authors`) "
        "VALUES (%s,%s,%s)"
    )

    add_authors = (
        "INSERT INTO `authors` "
        "(`FName`,`MName`,`LName`) "
        "VALUES (%s,%s,%s)"
    )

    add_book_authors=[
        "INSERT INTO `book_authors` "
        "(`Isbn`,`Author_id`) "
        "VALUES ("
        "(SELECT `Isbn` FROM `book` WHERE `Isbn` = %s),"
        "(SELECT `Author_id` FROM `authors` WHERE (`FName` = %s COLLATE utf8_bin AND `MName` = %s COLLATE utf8_bin AND `LName` = %s COLLATE utf8_bin)) "
        ")",

        "INSERT INTO `book_authors` "
        "(`Isbn`,`Author_id`) "
        "VALUES ("
        "(SELECT `Isbn` FROM `book` WHERE `Isbn` = %s),"
        "(SELECT `Author_id` FROM `authors` WHERE (`FName` = %s COLLATE utf8_bin AND `MName` is NULL AND `LName` = %s COLLATE utf8_bin)) "
        ")",

        "INSERT INTO `book_authors` "
        "(`Isbn`,`Author_id`) "
        "VALUES ("
        "(SELECT `Isbn` FROM `book` WHERE `Isbn` = %s),"
        "(SELECT `Author_id` FROM `authors` WHERE (`FName` = %s COLLATE utf8_bin AND `MName` is NULL AND `LName` is NULL)) "   #COLLATE utf8_bin helps to distinguish between latin and english characters
        ")"
    ]

    add_library_branch = (
        "INSERT INTO `library_branch` "
        "(`Branch_id`,`Branch_name`,`Street_Address`,`Zip`) "
        "VALUES (%s,%s,%s,%s)"
    )

    add_book_copies = (
        "INSERT INTO `book_copies` "
        "(`Isbn`,`Branch_id`,`No_of_copies`) "
        "VALUES ("
        "(SELECT `Isbn` FROM `book` WHERE `Isbn` = %s),"
        "(SELECT `Branch_id` FROM `library_branch` WHERE `Branch_id` = %s),"
        "%s"
        ")"
    )

    add_borrower = (
        "INSERT INTO `borrower` "
        "(`Card_no`,`Ssn`,`Fname`,`Lname`,`email`,`Street_Address`,`City`,`State`,`Phone`) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    )


    keywordList = [] # list of keywords for fuzzyfinder and spell corrector


    for row in book:
        tmp = (row['Isbn'],row['Title'],row['Book_authors'])

        keywordList.append(row['Isbn'])
        keywordList.append(row['Title'])

        cursor.execute(add_book,tmp)

    cnx.commit()                         # important step, transaction will be buffered without execution if missing it
    QMessageBox.information(None,'Status','book table data injection Completes!')

    for row in Isbn_and_author[0]:
        if row:
            tmp = row.split(' ')

            keywordList += tmp

            if len(tmp) == 1:
                data = (tmp[0],None,None)
            elif len(tmp) == 2:
                data = (tmp[0],None,tmp[1])
            else:
                data = (tmp[0],tmp[1],' '.join(tmp[2:]))
            cursor.execute(add_authors,data)
    cnx.commit()
    QMessageBox.information(None,'Status','authors table data injection Completes!')


    for key in Isbn_and_author[1]:
        tmp = Isbn_and_author[1][key]
        for each in tmp:
            if each:
                name_parts = each.split(' ')
                if len(name_parts) == 1:
                    data = (key, name_parts[0])
                    cursor.execute(add_book_authors[2],data)
                elif len(name_parts) == 2:
                    data = (key, name_parts[0],name_parts[1])
                    cursor.execute(add_book_authors[1],data)
                else:
                    data = (key, name_parts[0],name_parts[1],' '.join(name_parts[2:]))
                    cursor.execute(add_book_authors[0],data)
    cnx.commit()
    QMessageBox.information(None,'Status','book_authors table data injection Completes!')

    for row in library_branch:
        data=(int(row['branch_id']),row['branch_name'],row['address'][0],row['address'][1])

        keywordList += list(data)

        cursor.execute(add_library_branch,data)
    cnx.commit()
    QMessageBox.information(None,'Status','library_branch table data injection Completes!')

    for row in borrower:
        data=(row['Card_no'],row['ssn'],row['first_name'],row['last_name'],row['email'],row['street_address'],row['city'],row['state'],row['phone'])

        keywordList += list(data)

        cursor.execute(add_borrower,data)
    cnx.commit()
    QMessageBox.information(None,'Status','borrower table data injection Completes!')

    for row in book_copies:
        data = (row['Isbn'],row['branch_id'],row['no_of_copies'])
        cursor.execute(add_book_copies,data)
    cnx.commit()
    QMessageBox.information(None,'Status','book_copies table data injection Completes!')


    writeKeyWordList(keywordList)


def filenameFinder(url):
    idx = url.rfind('/')
    url = url[idx+1:]
    return url[:url.rfind('.')]

def writeKeyWordList(list):
    #print(list)
    with open(os.getcwd()+'/keyword.csv',encoding='utf8',newline='',mode='w') as csvfile:
        writer = csv.writer(csvfile,delimiter='\n')
        writer.writerow(list)
    QMessageBox.information(None,'File Creation','keywordFile creation completes')
