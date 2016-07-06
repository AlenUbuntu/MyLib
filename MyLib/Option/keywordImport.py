import mysql.connector
import sys
import csv

# Customer Parameters

DB_NAME = 'Library'
username = 'root'
passwd = 'qwe5813653'
host = '127.0.0.1'
url = 'Option/keyword.csv'


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

TABLES={}
TABLES['KeywordList']=(
    "CREATE TABLE `KeywordList` ("
    "`id` int AUTO_INCREMENT,"
    "`word` VARCHAR(255) NOT NULL,"
    "PRIMARY KEY (`id`)"
    ")"
)
cursor.execute(TABLES['KeywordList'])
add_word = (
    "INSERT INTO `KeywordList` "
    "(`word`) "
    "VALUES (%s)"
)

for row in open(url):
    tmp = row.rstrip('\n')
    cursor.execute(add_word,(tmp,))

cnx.commit()
cursor.close()
cnx.close()
