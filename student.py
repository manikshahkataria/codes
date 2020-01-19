import os
record=[]
roll=0
def menu():

    user_input = input("enter 'a' to add record,'b' to show the record,'c' ,'d'to delete the record,'q'to exit")
    while user_input != 'q':
        if user_input == 'a':
            add_record()
        elif user_input == 'b':
            show_record()
        elif user_input == 'd':
            delete_record()
        else:
            print('try again')

        user_input = input("enter 'a' to add record,'b' to show the record,'d'to delete the record,'q'to exit")

def add_record():
    n=int(input('enter how many data u want to enter '))
    f=open("e:\\record.txt",'w')
    for i in range(0,n):
        roll = int(input('enter roll no of student'))

        name = input('enter the name of student')

        section = input('enter the section of student')

        print(roll,file=f)
        print(name,file=f)
        print(section,file=f)

    f.close()
def show_record():
    f1=open("e:\\record.txt",'r')
    for s in f1:
        print(s)
    f1.close()
def delete_record():
    rn=int(input('enter the roll no of student wich u want to delete the record' ))
    f2=open("e:\\record.txt",'r')
    for k in f2:
        if rn!=roll:
            f3 = open("e:\\update.txt", 'w')

            for k in f3:
                print(k)





            f3.close()
        else:
            break
    f2.close()


menu()