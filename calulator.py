from tkinter import*
op1=""
op=""
op2=""
def action(event):
    global op1,op,op2
    b=event.widget
    textDisplay.insert("end",b.cget("text"))
   
def paction(event):
    global op1,op,op2
    op1=t1.get()
    t1.delete(0,"end")
    b=event.widget
    op=b.cget("text")
    

def equal(event):
     global op1,op,op2
     op2=t1.get()
     t1.delete(0,'end')
     g=eval(op1+op+op2)
     textDisplay.insert(0,g)
def btnClear():
    global operator
    operator=''
    text_input.set('')

'''
from tkinter import *
def btnClick(numbers):
    global operator
    operator=operator+ str(numbers)
    text_input.set(operator)
def btnClear():
    global operator
    operator=''
    text_input.set('')
def btnEquals():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=''
'''


cal=Tk()
cal.title('calculator')


textDisplay=Entry(cal,font=('arial',20,'bold'), textvariable= text_input,bd=30,
                  insertwidth=3,bg='cyan',justify='right').grid(columnspan=4)
button7=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',
               command=lambda :action(7))
button7.grid(row=1,column=0)

button8=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',
               command=lambda :action(8))
button8.grid(row=1,column=1)

button9=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',
               command=lambda :action(9))
button9.grid(row=1,column=2)

buttonAdd=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='+',
               command=lambda :paction('+'))
buttonAdd.grid(row=1,column=3)
########################################################
button4=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='4',
               command=lambda :action(4))
button4.grid(row=2,column=0)

button5=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='5',
               command=lambda :action(5))
button5.grid(row=2,column=1)

button6=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='6',
               command=lambda :action(6))
button6.grid(row=2,column=2)

buttonSub=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='-',
               command=lambda :paction('-'))
buttonSub.grid(row=2,column=3)
#############################################################
button1=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='1',
               command=lambda :action(1))
button1.grid(row=3,column=0)

button2=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='2',
               command=lambda :action(2))
button2.grid(row=3,column=1)

button3=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='3',
               command=lambda :action(3))
button3.grid(row=3,column=2)

buttonMul=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='*',
               command=lambda :paction('*'))
buttonMul.grid(row=3,column=3)
#################################################################
button0=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='0',
               command=lambda :action(0))
button0.grid(row=4,column=0)

buttonclr=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='C',
               command=btnClear)
buttonclr.grid(row=4,column=1)

buttonequ=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='=',
               command=equal)
buttonequ.grid(row=4,column=2)

buttonDiv=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='/',
               command=lambda :paction('/'))
buttonDiv.grid(row=4,column=3)







cal.mainloop()
