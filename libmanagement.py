from tkinter import *
import tkinter.messagebox


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
        Donl = StringVar()
        DoD = StringVar()
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
                                 ,font=('arial',12,'bold'),text='libary management INFO',bg='blue' )
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=20, pady=3, relief=RIDGE
                                   , font=('arial', 12, 'bold'), text='Book Detail', bg='blue')
        DataFrameRIGHT.pack(side=RIGHT)
        #----------------------------------------label entry-----------------------------
        self.FirstName=Label(DataFrameLEFT,font=('arial',12,'bold'),text="FirstName",padx=2,pady=2,
                             bg='blue')
        self.FirstName.grid(row=0,column=0,sticky=W)
        self.FirstName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=fna,width=25)

        self.FirstName.grid(row=0, column=1,)



if __name__=='__main__':
    root=Tk()
    application=library(root)
    root.mainloop()
