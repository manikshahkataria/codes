import os
a=dict()


rno=[]

def menu():

    user_input = input("enter '1' to add record,'2' to show the record,'3' to show some specific roll no record ,'4'to delete the record,'5'to exit")
    while user_input != '5':
        if user_input == '1':
            add_record(rno)
        elif user_input == '2':
            show_record()1
        elif user_input == '3':
            show_specific_record('rno')
        elif user_input=='4':
            delete_record()
        else:
            print('try again')

        user_input = input("enter '1' to add record,'2' to show the record,'3' to show some specific roll no record ,'4'to delete the record,'5'to exit")


def add_record(rno):
    f1=open("e:\\record1.txt",'w')
    a=dict()
    n=int(input('how many record u want to enter'))
    for i in range(n):
        rno=int(input('enter the Roll no'))
        b=[]
        b.append(input('enter name'))
        b.append (int(input('enter phone-no ')))
        b.append(int(input('enter marks')))
        a[rno]=b

        print(a,file=f1)
    return rno
    f1.close()

def show_record():
    f2=open("e:\\record1.txt",'r')
    for s in f2:
        print(s)
    f2.close()
def show_specific_record(rno):
    n=int(input('enter rollno to be searched'))
    f3=open("e:\\record1.txt",'r')
    l=f3.readline()
    print(l)
    print("hello1")
    k=dict(l)
    print(k)
    print("hello2")

    if n==[rno]:
        print(l[rno])
    else:
        print('not found')
    f3.close()
def delete_record():
    f4=open("e:\\record1.txt",'r')

    k=int(input('enter the rno u want to delete'))
    if k==rno:
        del a[rno]
        show_record()
    f4.close()


menu()