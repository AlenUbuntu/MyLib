import mysql.connector
import sys
# Customer Parameters

DB_NAME = 'Library'
username = 'root'
passwd = 'qwe5813653'
host = '127.0.0.1'

loan_data = [
    {'Isbn':'0195153448','card_no':'ID000003','branch_id':1 },
    {'Isbn':'0002005018','card_no': 'ID000006','branch_id':1},
    {'Isbn':'0060973129','card_no': 'ID000009','branch_id':1},
    {'Isbn':'0393045218','card_no': 'ID000015','branch_id':1},
    {'Isbn':'0425176428','card_no': 'ID000017','branch_id':1}
]

fine_data = [
    {'loan_id':1,'fine_amt':100,'paid':0},
    {'loan_id':2,'fine_amt':200,'paid':0},
    {'loan_id':3,'fine_amt':300,'paid':0},
    {'loan_id':4,'fine_amt':400,'paid':1},
    {'loan_id':5,'fine_amt':500,'paid':0}
]


cnx = mysql.connector.connect(
    user=username,
    password=passwd,
    host=host
)

cursor = cnx.cursor(buffered = True)
#cursor.execute(
#    "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME)
#)
cnx.database = DB_NAME

add_loan = (
    "INSERT INTO `book_loans` "
    "(`Book_id`,`Card_no`) "
    "VALUES ("
    "(SELECT `Book_id` FROM `book_copies` WHERE `Isbn` = %s AND `Branch_id`=%s),"
    "(SELECT `Card_no` FROM `borrower` WHERE `Card_no` = %s)"
    ");"
)

add_fine = (
    "INSERT INTO `fines` "
    "(`loan_id`,`Fine_amt`,`Paid`) "
    "VALUES ("
    "(SELECT `loan_id` FROM `book_loans` WHERE `loan_id` = %s), "
    "%s,%s"
    ");"
)

for row in loan_data:
    data = (row['Isbn'],row['branch_id'],row['card_no'])
    cursor.execute(add_loan,data)
cnx.commit()

for row in fine_data:
    data = (row['loan_id'],row['fine_amt'],row['paid'])
    cursor.execute(add_fine,data)

cnx.commit()

cursor.close()
cnx.close()
