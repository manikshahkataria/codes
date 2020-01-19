import datetime
import sqlite3
def AddBook(db):         #for add of book
    Bookid = int(input('enter the Bookid :'))
    BookName = input('enter the name of book:')
    Author = input('enter the name of author :')
    Qty = int(input('enter number of books'))
    price = int(input('enter price for the book'))
    db.execute('insert into books values(?,?,?,?,?)', (Bookid, BookName, Author, Qty, price))
    db.commit()
    print ('data add sucessfully')

def CheckQuantity(db,bid):     #if issue is called then chaek avialablity bid =book id
    cursor=db.execute('select quantity from books where id=?',(bid,))
    k=0
    for rows in cursor:
        if int(rows[0])>0:
            return True
        else:
            return False
def UpdateBookI(db,bid):
    cursor=db.execute('update books set quantity=quantity-1 where id =?',(bid,))
    db.commit()
def UpdateBookR(db,bid):
    cursor=db.execute('update books set quantity=quantity+1 where id =?',(bid,))
    db.commit()
def IssueBook(db):
    id=int(input('enter transactin id'))
    bid=int(input('enter book id '))
    cid=int(input('enter coustomer id'))
    Idate=datetime.datetime.now()
    Rdate='notavi'
    if CheckQuantity(db,bid)==True:
        db.execute('insert into transactions values(?,?,?,?,?)',(id,bid,cid,Idate,Rdate,))
        print ('issued sucessfully')
        UpdateBookI(db,bid)
    else:
        print ('not sufficent quatiy')
    db.commit()

def ReturnBook(db):
    id=int(input('enter transactin id'))
    Rdate=datetime.datetime.now()
    db.execute('update transactions set rdate=? where id=?',(Rdate,id))
    cursor=db.execute('select bid from transactions where id=?',(id,))
    bid=0
    for row in cursor:
        bid=int(row[0])
    UpdateBookI(db,bid)
    db.commit()
def DispAllBooks(db):
    cursor = db.execute('select * from books')
    for Row in cursor:
        print(Row[0], Row[1], Row[2], Row[3], Row[4])
    print ()
def DispBook(db):
    name=input('enter book name')
    cursor=db.execute('select * from books where name=?',(name,))
    k=0
    for Row in cursor:
        print(Row[0], Row[1], Row[2], Row[3], Row[4])
        k=k+1
    if k==0:
        print ('no match')
def ShowDefaulters(db):
    cursor = db.execute("select * from transactions where rdate='notavi'")
    k = 0
    for Row in cursor:
        print(Row[0], Row[1], Row[2], Row[3], Row[4])

def AddCustomer(db):
    Cust_id = int(input('enter coustmer id'))
    Cust_Name = input('enter coustmer name')
    Pho = int(input('enter pno'))
    address = input('enter add of coustomer')
    db.execute('insert into Customers values(?,?,?,?)', (Cust_id, Cust_Name, Pho, address,))
    db.commit()
def DeleteCustomer(db):
    Cust_id = int(input("enter the id of customer which you want to delete "))
    db.execute('delete from Customers where id =?', (Cust_id,))
    db.commit()
    print('deleted sucessfully')
def DeleteBook(db):
    Bookid = int(input('enter Book_id to be deleted'))
    db.execute('delete from Books where id=?', (Bookid,))
    db.commit()
    print('deleted sucessfully')
def DispCustomer(db):
    Name = input('enter customer name:')
    cursor = db.execute("select * from Customers where name =?", (Name,))
    k = 0
    for Row in cursor:
        print(Row[0], Row[1], Row[2], Row[3])
        k = k + 1
    if k == 0:
        print ('no match')
    db.commit()

db=sqlite3.connect('LMS.db')
db.execute('create table if not exists Books(id int primary key,name text,author text,quantity int,priced int)')
db.execute('create table if not exists Customers(id int primary key,name text,pno int,address text)')
db.execute('create table if not exists Transactions(id int primary key,bid int,cid int,idate text,rdate text)')


ch=1

while ch!=11:
    print('press 1 for adding book')
    print('press 2 for searching a book')
    print('press 3 for delete a book')
    print('press 4 for add new customer ')
    print('press 5 for search a customer')
    print('press 6 for delete a customer')
    print('press 7 for issue a book')
    print('press 8 for return book')
    print('press 9 to show all defaulters ')
    print ('press 10 to show all books')
    print('press 11 to exit')
    ch = int(input("enter your choice"))
    if ch==1:
        AddBook(db)
    elif ch==2:
        DispBook(db)
    elif ch==3:
        DeleteBook(db)
    elif ch==4:
        AddCustomer(db)
    elif ch == 5:
        DispCustomer(db)
    elif ch==6:
        DeleteCustomer(db)
    elif ch==7:
        IssueBook(db)
    elif ch==8:
        ReturnBook(db)
    elif ch==9:
        ShowDefaulters(db)
    elif ch==10:
        DispAllBooks(db)


