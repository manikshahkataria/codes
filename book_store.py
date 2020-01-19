import sqlite3
import datetime
d=datetime.datetime.now()
print(d.today())
db=sqlite3.connect("e:\\kiki.db")
db.execute("create table if not exists Book(Bookid int primary key,BookName text,Author text,Qty int,price int)")
db.execute("create table if not exists Customer(Cust_id int primary key,Cust text,Pho int,address text) ")
db.execute("create table if not exists Transact(Tansaction_id int primary key,Bookid int,Cust_id int,Issue_date int,return_date)")
n=0


def meanu():
    n=int(input("press '1' for adding book,press '2' for searching a book,press '3' for delete a book,press '4' for add new custmer,
    press 5 for search a custmer"
    ))
    print('press 1 for adding book')
    print('press 2 for searching a book')
    print('press 3 for delete a book')
    print('press 4 for add new custmer ')
    print('press 5 for search a custmer')
    print('press 6 for delete a customer')
    print('press 7 for issue a book')
    print('press 8 for return book')
    print('press 9 to show all defaulters ')
    print('press 10 to show all books')
n=int(input("enter your choice"))



if n==1:
            Bookid=int(input('enter the Bookid :'))
            BookName=input('enter the name of book:')
            Author=input('enter the name of author :')
            Qty=int(input('enter number of books'))
            price=int(input('enter price for the book'))
            db=sqlite3.connect('e:\\kiki.db')
            db.execute('insert into Book values(?,?,?,?,?)',(Bookid,BookName,Author,Qty,price))
            print('add succsfully')

            db.commit()

if n==2:
            print('search based on ')
            print('press c for book id wise  ')
            print('b for book name  ')
            print('a for author  name ')
            x=(input('enter choice'))
            db=sqlite3.connect('e:\\kiki.db')

            if x=='c':
                bookid=int(input('enter booid to be searched'))
                cursor=db.execute('select * from Book where Bookid=?',(Bookid,))
                for row in cursor:
                    print(Row)
            db.commit()
            if x=='b':
                BookName=input('enter book name:')
                cursor=db.execute("select * from Book where BookName=?",(BookName,))
                for Row in cursor:
                    print(Row)
            db.commit()
            if x=='a':
                Authr=input('enter Author name:')
                cursor=db.execute("select * from Book where Author=?",(Authr,))
                for Row in cursor:
                    print(Row)
            db.commit()

if n==3:
            db=sqlite3.connect('e:\\kiki.db')
            Bookid=int(input('enter Book_id to be deleted'))
            db.execute('delete from Book where Bookid=?',(Bookid,))
            db.commit()

if n==4:   #add the coustomer
            Cust_id=int(input('enter coustmer id' ))
            Cust_Name=input('enter coustmer name')
            Pho=int(input('enter pno'))
            address=input('enter add of coustomer')
            db.execute('insert into Customer values(?,?,?,?)',(Cust_id,Cust_Name,Pho,address,))
            db.commit()

if n==5:   #search cust
            Name=input('enter customer name:')
            cursor=db.execute("select * from Customer where Cust =?",(Name,))
            for Row in cursor:
                print(Row)
            db.commit()
if n==6: #del custo
            name=input("enter the name of customer which you want to delete ")
            db.execute('delete from Customer where Cust =?',(name,))
            db.commit()
if n==7: #issue


            db=sqlite3.connect('e:\\kiki.db')
            bookid=int(input('enter the id of book u want to return'))
            db.execute('delete from Transact where Bookid =?',(bookid,))
            db.commit()

if n==9:
            db.row_factory=sqlite3.Row
            cursor=db.execute('select * from Transact')
            for Row in cursor:
                print (Row['Transaction_id'],Row['Bookid'],Row['Cust_id'],Row['Issue_date'],Row['Return_date'])
            db.commit()

if n==10:
    db = sqlite3.connect('e:\\kiki.db')
    db.row_factory = sqlite3.Row
    cursor = db.execute('select * from Book')
    k=0
    for Row in cursor:
        print(Row["Bookid"], Row["BookName"], Row['Author'], Row['Qty'], Row['price'])
        k=k+1
print()
db.commit()

