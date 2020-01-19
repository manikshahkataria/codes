from tkinter import *
import tkinter.messagebox
import LibBkDatabase


class library:
    def __init__(self, root):
        self.root = root
        self.root.title("libary management")
        self.root.geometry("1350x750+0+0")

        fna = StringVar()
        sna = StringVar()
        Adr1 = StringVar()
        MNo = StringVar()
        BkID = StringVar()
        Bkt = StringVar()
        Atr = StringVar()
        DBo = StringVar()
        Ddu = StringVar()
        LrF = StringVar()
        
        DoD = StringVar()
        Donl = StringVar()
        #___________________________________________________function_______________________________________________________

        def iExit():
            iExit=tkinter.messagebox.askyesno("libary management","confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return
        def ClearData():
            self.txtFirstName.delete(0,END)
            self.txtSurName.delete(0,END)
            self.txtAdress.delete(0,END)
            self.txtMobile.delete(0,END)
            self.txtBookid.delete(0,END)
            self.txtBookt.delete(0,END)
            self.txtauthor.delete(0,END)
            self.txtdateReturn.delete(0,END)
            self.txtdateBorrow.delete(0,END)
            self.txtlateFee.delete(0,END)
            self.txtDate_over_due.delete(0,END)
            self.txtselling_Price.delete(0,END)

        def addData():
            if(len(fna.get())!=0):
                LibBkDatabase.addDataRec(fna.get(),sna.get(),Adr1.get(),MNo.get(),BkID.get(),Bkt.get(),
                                         Atr.get(),DBo.get(),Ddu.get(),LrF.get(),DoD.get(),Donl.get())
            booklist.delete(0,END)
            booklist.insert(END,(fna.get(),sna.get(),Adr1.get(),MNo.get(),BkID.get(),Bkt.get(),
                                         Atr.get(),DBo.get(),Ddu.get(),LrF.get(),DoD.get(),Donl.get()))
        def DisplayData():
            booklist.delete(0,END)
            for row in LibBkDatabase.viewData():
                booklist.insert(END,row)
        def SelectedBook(event):
            global sb
            searchBk = booklist.curselection()[0]
            sb=booklist.get(searchBk)

            self.txtFirstName.delete(0,END)#if after the dispaly of data
            self.txtFirstName.insert(END,sb[0])#on clicking on data that data
            self.txtSurName.delete(0,END)#should diplay in each collmn
            self.txtSurName.insert(END,sb[1])#it is done by listbox down in scroll bar section
            self.txtAdress.delete(0,END)
            self.txtAdress.insert(END,sb[2])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,sb[3])
            self.txtBookid.delete(0,END)
            self.txtBookid.insert(END,sb[4])
            self.txtBookt.delete(0,END)
            self.txtBookt.insert(END,sb[5])
            self.txtauthor.delete(0,END)
            self.txtauthor.insert(END,sb[6])
            self.txtdateReturn.delete(0,END)
            self.txtdateReturn.insert(END,sb[7])
            self.txtdateBorrow.delete(0,END)
            self.txtdateBorrow.insert(END,sb[8])
            self.txtlateFee.delete(0,END)
            self.txtlateFee.insert(END,sb[9])
            self.txtDate_over_due.delete(0,END)
            self.txtDate_over_due.insert(END,sb[10])
            self.txtselling_Price.delete(0,END)
            self.txtselling_Price.insert(END,sb[11])


        def DeleteData():
            if(len(fna.get())!=0):
                
            
            
        

        
        # --------------------------------------frame--------------------------#
        MainFrame = Frame(self.root)
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=40, pady=8, bg="blue", relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame,font=('arial',46,'bold'),text='libary management' )
        self.lblTit.grid(sticky=W)
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=100, padx=20, pady=20, bg="blue", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        FrameDetail = Frame(MainFrame, bd=0, width=1350, height=50, padx=20,   relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=1, width=1350, height=400, padx=20, pady=20,  relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT=LabelFrame(DataFrame, bd=1,width=800,height=300,padx=20,pady=20,relief=RIDGE
                                 ,font=('arial',12,'bold'),text='libary management',bg='blue' )
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=20, pady=3, relief=RIDGE
                                   , font=('arial', 12, 'bold'), text='Book Detail', bg='blue')
        DataFrameRIGHT.pack(side=RIGHT)
        #----------------------------------------label entry-----------------------------
        self.FirstName=Label(DataFrameLEFT,font=('arial',12,'bold'),text="FirstName",padx=2,pady=2,
                             bg='blue')
        self.FirstName.grid(row=0,column=0,sticky=W)
        self.txtFirstName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=fna,width=25)

        self.txtFirstName.grid(row=0, column=1,)


        self.SurName=Label(DataFrameLEFT,font=('arial',12,'bold'),text="SurName",padx=2,pady=2,
                             bg='blue')
        self.SurName.grid(row=1,column=0,sticky=W)
        self.txtSurName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=sna,width=25)

        self.txtSurName.grid(row=1, column=1,)



        self.Adress=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Adress",padx=2,pady=2,
                             bg='blue')
        self.Adress.grid(row=2,column=0,sticky=W)
        self.txtAdress = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Adr1,width=25)

        self.txtAdress.grid(row=2, column=1,)




        self.Mobile=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Phone no",padx=2,pady=2,
                             bg='blue')
        self.Mobile.grid(row=3,column=0,sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=MNo,width=25)

        self.txtMobile.grid(row=3, column=1,)



        self.Bookid=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Bookid",padx=2,pady=2,
                             bg='blue')
        self.Bookid.grid(row=4,column=0,sticky=W)
        self.txtBookid = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=BkID,width=25)

        self.txtBookid.grid(row=4, column=1,)


        self.Bookt=Label(DataFrameLEFT,font=('arial',12,'bold'),text="BookTitle",padx=2,pady=2,
                             bg='blue')
        self.Bookt.grid(row=5,column=0,sticky=W)
        self.txtBookt = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Bkt,width=25)

        self.txtBookt.grid(row=5, column=1,)




        
        self.author=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Author",padx=2,pady=2,
                             bg='blue')
        self.author.grid(row=0,column=3,sticky=W)
        self.txtauthor = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Atr,width=25)

        self.txtauthor.grid(row=0, column=4,)



        self.dateBorrow=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Date_of_Borrow",padx=2,pady=2,
                             bg='blue')
        self.dateBorrow.grid(row=1,column=3,sticky=W)
        self.txtdateBorrow = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DBo,width=25)

        self.txtdateBorrow.grid(row=1, column=4)








        
        self.dateReturn=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Date_of_Return",padx=2,pady=2,
                             bg='blue')
        self.dateReturn.grid(row=2,column=3,sticky=W)
        self.txtdateReturn = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Ddu,width=25)

        self.txtdateReturn.grid(row=2, column=4,)





        
        self.lateFee=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Late_Fee",padx=2,pady=2,
                             bg='blue')
        self.lateFee.grid(row=3,column=3,sticky=W)
        self.txtlateFee = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=LrF,width=25)

        self.txtlateFee.grid(row=3, column=4,)






        
        self.Date_over_due=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Date_over_due",padx=2,pady=2,
                             bg='blue')
        self.Date_over_due.grid(row=4,column=3,sticky=W)
        self.txtDate_over_due = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DoD,width=25)

        self.txtDate_over_due.grid(row=4, column=4,)





        
        self.selling_price=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Price",padx=2,pady=2,
                             bg='blue')
        self.selling_price.grid(row=5,column=3,sticky=W)
        self.txtselling_Price= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Donl,width=25)

        self.txtselling_Price.grid(row=5, column=4,)
#------------------------------------------------------------scroll bar book display area--------------------------------------------------------
        scrollbar=Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky="ns")
        booklist=Listbox(DataFrameRIGHT,width=45,height=15, font=('arial', 12, 'bold'),yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)

#__________________________________________________________________button____________________________________________________________

        self.btnAdd=Button(ButtonFrame,width=15,height=2,font=('arial', 12, 'bold'),text="Add DATA",command=addData)
        self.btnAdd.grid(row=0,column=0)

        self.btnDelete=Button(ButtonFrame,width=15,height=2,font=('arial', 12, 'bold'),text="DELETE DATA",command=)
        self.btnDelete.grid(row=0,column=1)

        self.btnSearch=Button(ButtonFrame,width=15,height=2,font=('arial', 12, 'bold'),text="SEARCH DATA")
        self.btnSearch.grid(row=0,column=2)

        self.btnClear=Button(ButtonFrame,width=15,height=2,font=('arial', 12, 'bold'),text="CLEAR DATA",command=ClearData)
        self.btnClear.grid(row=0,column=3,)

        
        self.btnUpdate=Button(ButtonFrame,width=15,height=2,font=('arial', 12, 'bold'),text="UPDATE DATA")
        self.btnUpdate.grid(row=0,column=4)

        self.btnDisplay=Button(ButtonFrame,width=15,height=2,font=('arial', 12, 'bold'),text="DISPLAY DATA",command=DisplayData)
        self.btnDisplay.grid(row=0,column=5)


        self.btnExit=Button(ButtonFrame,width=15,height=2,font=('arial', 12, 'bold'),text="EXIT ",command=iExit)
        self.btnExit.grid(row=0,column=6)

if __name__=='__main__':
    root=Tk()
    application=library(root)
    root.mainloop()


