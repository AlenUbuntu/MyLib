from PyQt5.QtWidgets import QMessageBox

def findLoan(sql,book_idList=None,card_no=None,OverdueFlag=False,fullRecord=False):
    if not book_idList and (not card_no):
        QMessageBox.critical(None,'Error','Unavailable to locate due to lack of information!')
    else:
        if card_no and not book_idList:
            if not OverdueFlag and not fullRecord:
                query = (
                    "SELECT bl.Loan_id,bl.Book_id,bl.Card_no,bl.Date_out,bl.Due_date,bl.Date_in "
                    "FROM book_loans AS bl,borrower AS b "
                    "WHERE bl.Card_no=b.Card_no "
                    "AND b.Card_no=%s "
                    "AND Date_in IS NULL;"
                )
            elif not fullRecord:
                query = (
                    "SELECT bl.Loan_id,bl.Book_id,bl.Card_no,bl.Date_out,bl.Due_date,bl.Date_in "
                    "FROM book_loans AS bl,borrower AS b "
                    "WHERE bl.Card_no=b.Card_no "
                    "AND b.Card_no=%s "
                    "AND (NOW() > bl.Due_date AND bl.Date_in IS NULL);"
                )
            elif not OverdueFlag and fullRecord:
                query = (
                    "SELECT bl.Loan_id,bl.Book_id,bl.Card_no,bl.Date_out,bl.Due_date,bl.Date_in "
                    "FROM book_loans AS bl,borrower AS b "
                    "WHERE bl.Card_no=b.Card_no "
                    "AND b.Card_no=%s "
                )
            return sql.query(query,(card_no,))
        elif book_idList and (not card_no):
            if not OverdueFlag:
                query = (
                    "SELECT bl.Loan_id,bl.Book_id,bl.Card_no,bl.Date_out,bl.Due_date,bl.Date_in "
                    "FROM book_loans AS bl,book_copies AS b "
                    "WHERE bl.Book_id=b.Book_id "
                    "AND Date_in IS NULL "
                    "AND ((b.Book_id=%s) "
                )
            else:
                query = (
                    "SELECT bl.Loan_id,bl.Book_id,bl.Card_no,bl.Date_out,bl.Due_date,bl.Date_in "
                    "FROM book_loans AS bl,book_copies AS b "
                    "WHERE bl.Book_id=b.Book_id "
                    "AND (NOW() > bl.Due_date AND bl.Date_in IS NULL) "
                    "AND ((b.Book_id=%s) "
                )
            statement = "OR (b.Book_id=%s) "
            i=0
            param=[]
            for each in book_idList:
                if i==0:
                    pass
                else:
                    query += statement
                param.append(each)
                i+=1
            query += ');'
            return sql.query(query,tuple(param))
        else:
            if not OverdueFlag:
                query = (
                    "SELECT bl.Loan_id,bl.Book_id,bl.Card_no,bl.Date_out,bl.Due_date,bl.Date_in "
                    "FROM book_loans AS bl,book_copies AS bc, borrower AS b "
                    "WHERE bl.Book_id=bc.Book_id "
                    "AND bl.Card_no=b.Card_no "
                    "AND b.Card_no=%s "
                    "AND Date_in IS NULL "
                    "AND ((bc.Book_id=%s) "
                )
            else:
                query = (
                    "SELECT bl.Loan_id,bl.Book_id,bl.Card_no,bl.Date_out,bl.Due_date,bl.Date_in "
                    "FROM book_loans AS bl,book_copies AS bc, borrower AS b "
                    "WHERE bl.Book_id=bc.Book_id "
                    "AND bl.Card_no=b.Card_no "
                    "AND b.Card_no=%s "
                    "AND (NOW() > bl.Due_date AND bl.Date_in IS NULL) "
                    "AND ((bc.Book_id=%s) "
                )

            statement = "OR (bc.Book_id=%s) "
            i=0
            param=[]
            param.append(card_no)
            for each in book_idList:
                if i==0:
                    pass
                else:
                    query += statement
                param.append(each)
                i+=1
            query += ');'
            print(query)
            return sql.query(query,tuple(param))

def findOverDue(sql,book_idList=None,card_no=None):
    return findLoan(sql,book_idList,card_no,True)

def checkOverdue(sql,loan_id):
    query = (
        "SELECT * FROM book_loans "
        "WHERE loan_id=%s "
        "AND NOW()>Due_date "
        "AND Date_in IS NULL;"
    )
    res = sql.query(query,(loan_id,))
    if res:
        return True
    else:
        return False

def findFine(sql,loan_idList,flag = False):
    # Paid=0  -> unpaid
    # Paid=1  -> paid
    query = (
        "SELECT f.Loan_id,f.Fine_amt,f.Paid "
        "FROM fines AS f,book_loans AS bl "
        "WHERE f.loan_id=bl.loan_id "
        "AND f.Paid=0 "
        "AND ((f.loan_id=%s) "
    )
    query_2 = (
        "SELECT f.Loan_id,f.Fine_amt,f.Paid "
        "FROM fines AS f,book_loans AS bl "
        "WHERE f.loan_id=bl.loan_id "
        "AND ((f.loan_id=%s) "
    )
    statement = "OR (f.loan_id=%s) "
    i = 0
    param = []
    for each in loan_idList:
        if i==0:
            pass
        else:
            if not flag:
                query += statement
            else:
                query_2 += statement
        param.append(each)
        i+=1
    if not flag:
        query += ');'
        return sql.query(query,tuple(param))
    else:
        query_2 += ');'
        return sql.query(query_2,tuple(param))
