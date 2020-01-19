import sqlite3
db=sqlite3.connect("e:\\kaki.db")
db.execute("create table if not exists student(rno int primary key,name text,marks float)")
rno=int(input("enter the rno"))
name=input('enter name')
marks=float(input('enter marks'))
db.execute("insert into student values(?,?,?)",(rno,name,marks))
db.commit()
db.close()


db=sqlite3.connect("e:\\kaki.db")
cusor=db.execute("select * from student")
for row in cusor:
    for r in row:
        print(r,end="\t")
    print()
db.close()