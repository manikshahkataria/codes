import sqlite3

def ConnectData():
    con=sqlite3.connect("F:\\python program\\libbooks.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS libbooks(fna text,sna text,Adr1 text,MNo text,BkID text,Bkt text,Atr text,DBo text,Ddu text,LrF text,DoD text,Donl text)")
    con.commit()
    con.close()
def addDataRec(fna,sna,Adr1 ,MNo ,BkID,Bkt ,Atr ,DBo,Ddu ,LrF ,DoD,Donl):
    con = sqlite3.connect("F:\\python program\\libbooks.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS libbooks(fna text,sna text,Adr1 text,MNo text,BkID text,Bkt text,Atr text,DBo text,Ddu text,LrF text,DoD text,Donl text)")
    cur.execute("INSERT INTO libbooks(fna,sna,Adr1 ,MNo ,BkID,Bkt ,Atr ,DBo,Ddu ,LrF ,DoD,Donl) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(fna,sna,Adr1 ,MNo ,BkID,Bkt ,Atr ,DBo,Ddu ,LrF ,DoD,Donl))
    con.commit()
    con.close()
def viewData():
    con = sqlite3.connect("F:\\python program\\libbooks.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM libbooks")
    rows=cur.fetchall()
    con.close()
    return rows
ConnectData()
